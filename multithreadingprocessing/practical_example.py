import os
import time
import sys
import ssl
import imaplib
import multiprocessing
import numpy as np

# Credentials and paths
IMAP_SERVER = "imap.yandex.com" # imap server for yandex, choose the one you wish to use.
EMAIL_ACCOUNT = "" # enter the credentials
PASSWORD = ""
OUTPUT_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'downloaded_emails') # save mails here

# To parallelise:
'''1. each worker connects individually with the imap server.
2. each worker has a sublist of emails (ids/counts) it should download.
3. each worker then downloads every email in their sublist of ids and terminates'''

def connect():
    '''
    This function is used to establish connection with the imap server.
    '''
    counter = 5 # retry counter in case connection does not succeed in the first try.
    while counter > 0:
        try:
            M = imaplib.IMAP4_SSL(IMAP_SERVER)
            M.login(EMAIL_ACCOUNT, PASSWORD)
            print('Login success!')
            break
        except (ssl.SSLEOFError, imaplib.IMAP4.abort) as e:
            print('Login fail!')
            counter -= 1
            continue
    return M

def splitter(list_ids, NUM_WORKERS):
    list_list_ids = []
    for i in np.array_split(list_ids, NUM_WORKERS):
        list_list_ids.append(list(i))
    return list_list_ids

def perform_download(M, sublist_of_ids):
    for c in sublist_of_ids: # iteration over the sublist of mail-ids
        _, data = M.fetch(c.decode(), '(RFC822)')
        f = open('%s/%s.eml' % (OUTPUT_DIRECTORY, str(c.decode())), 'wb')
        f.write(data[0][1])
        f.close()
    M.close()
    M.logout()
    print('Connection closed!')

def mp_process(sublist):
    ''' A wrapper function within which a particular worker establishes a connection with 
    the imap server and calls the function to download emails corresponding the list of 
    ids for this particular worker.
  '''
    process_imap = connect()
    _, _ = process_imap.select()
    return perform_download(process_imap, sublist)

def get_mails(ids, poolsize):
    ''' A function to initialize the pool of workers and call the wrapper function mp_process. 
    The input 'ids' is a list of sublists'''
    pool = multiprocessing.Pool(poolsize)
    s = pool.map(mp_process, ids)
    print('Active children count: %d ' %len(multiprocessing.active_children()))
    pool.close()
    pool.join()
    return 'OK'

# Do a single connection and get all ids
def get_all_ids():
    M = connect()
    _, _ = M.select()
    rv, ids = M.search(None, "ALL")
    return ids


if __name__ == '__main__':
    ids = get_all_ids()
    print('Getting into multiprocessing part')

    # Define number of workers to be 2*CPU
    NUM_WORKERS = multiprocessing.cpu_count() * 2
    print('worker count: %d' % NUM_WORKERS)

    # splitting the mails ids into chunks of len_each_block mail ids.
    list_ids = ids[0].split()
    list_list_ids = splitter(list_ids, NUM_WORKERS)

    # call multiprocessing function
    t1 = time.time()
    get_mails(list_list_ids, NUM_WORKERS) # splitting and controlling process count (Faster)
print(time.time() - t1)




### LINKs
#https://medium.com/idealo-tech-blog/parallelisation-in-python-an-alternative-approach-b2749b49a1e
