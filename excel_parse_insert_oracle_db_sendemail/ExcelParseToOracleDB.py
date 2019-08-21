import sys, os, csv , cx_Oracle , xlrd, socket, smtplib, logging, sys
from email.mime.text  import MIMEText
from datetime import datetime, timedelta

# Log configuration
logging.basicConfig(filename="general_table_name.log", filemode='a', level=logging.DEBUG, format = "%(asctime)s:%(levelname)s:%(message)s")
logging.debug(" --- Script started --- ")
# Set excel file path
src = '../excel_parse/DB_Test_Excels/table_name_list.xlsx'
os.environ["NLS_LANG"] = ".AL32UTF8"

def email_send(content):
    ### Define Email variables
    smtpaddress = "192.168.1.1"
    smtpport = 25
    from_adr = "test@gmail.com"
    user_pass = ""
    send_adr = ["babak.mammadov@gmail.com"]
    subject = " Test Project Import Excel To  Status Script"
    #content = """ It is test email. """
    timeout_value = 30 # seconds
    ###  Send Email with try&except
    try:
        mail = MIMEText(content, "html", "utf-8")
        mail["From"] = from_adr
        mail["Subject"] = subject
        mail["To"] = ",".join(send_adr)
        mail = mail.as_string()
        socket.setdefaulttimeout(timeout_value)
        s = smtplib.SMTP(smtpaddress,smtpport)
        #s.starttls()                          # Disable it because local email doesn't support tls auth
        #s.login(from_adr, user_pass)          # Disable it because local email doesn't support auth
        s.sendmail(from_adr, send_adr, mail)
        logging.debug(" EMail Sent.")
        #print("EMail Sent.")
        s.quit()
    except Exception as e:
        # Print any error messages to stdout
        logging.debug(' Mail sending host %s and port %s error : %s', smtpaddress, smtpport, e)

# Define oracle connection script
def oracle_conn():
    db_serv = '192.168.1.2'
    db_port = '1521'
    try:
        ### Oracle Connection
        dsn_tns = cx_Oracle.makedsn('192.168.1.2', '1521', service_name='test')
        connection = cx_Oracle.connect(user=r'table_name', password='pass', dsn=dsn_tns)
        cursor = connection.cursor()
        logging.debug(' Connection to oracle db to Success  %s and port %s', db_serv, db_port)
        return cursor, connection
    except Exception as e:
        # Print any error messages to stdout
        logging.debug(' Connection to oracle db  %s and port %s error as  : %s', db_serv, db_port, e)
        logging.debug(' --- Script stopped with following error --- ')
        email_send("  {} Connection to oracle db {}  and port {} error as {} :".format(datetime.today(), db_serv, db_port, e))
        exit()

def execute_query():
    # Define Insert query and oracle connection function
    query = "insert into table_name.table_name_LOAD values('{}', '{}','{}', '{}', '{}')"
    cursor , connection = oracle_conn()
    ### Define Excel
    book = xlrd.open_workbook('../excel_parse/_Test_Excels/table_name_list.xlsx')
    ###  Set default index
    sh = book.sheet_by_index(0)
    ### Find cols and rows size on Excel
    num_cols = sh.ncols
    num_rows = sh.nrows
    #print("Excel row count:", num_rows)
    query_count = 1
    ### Iterate over excel row list
    for row_id in range(1,num_rows):
        row = [int(cell.value) if isinstance(cell.value, float) else cell.value for cell in sh.row(row_id)]
        id=row[0]
        name=row[1]
        name_col=row[2]
        number=row[3]
        file_id=row[4]
        try:
            cursor.execute(query.format(id,name,name_col,number,file_id).encode('utf-8'))
            connection.commit()
            query_count = query_count + 1
        except Exception as e:
            connection.rollback()
            query_count = query_count - 1
            logging.debug(' Problem happen insert query: %s', e)
            logging.debug(' Query: %s', query.format(id,name,name_col,number,file_id))
            logging.debug(' --- Script stopped with following error --- ')
            email_send(" {} Problem happen when inserting query to db , please contact DevOps team".format(datetime.today()))
            exit()
    connection.close()
    if query_count == num_rows:
        logging.debug(' All Excel Row Imported to DB succesfuly')
        logging.debug(' --- Script finished ---')
        email_send(" {} All Excel Row Imported to DB succesfuly".format(datetime.today()))
        try:
            # Call database table_name procedure for insert and update
            cursor.callproc('pkg_table_name.load_table_name_data')
            cursor.execute("truncate table table_name.table_name_LOAD")
        except Exception as e:
            logging.debug(' Problem happen truncate table query: %s', e)
    else:
        logging.debug(' Problem happen when inserting upper query')
        email_send(" {} Problem happen when inserting query to db , please contact DevOps team".format(datetime.today()))


# Check excel file if it is exist execute parse operation and change excel file name  or write log
def checkfile_Excel():
    if os.path.isfile(src):
        execute_query()
        os.system('cd /home/oracle/excel_parse/_Test_Excels ; mv table_name_list.xlsx   table_name_list_$(date +%F-%S-%M-%H).xlsx')
    else:
        logging.debug(' New Excel file does not exist')

checkfile_Excel()