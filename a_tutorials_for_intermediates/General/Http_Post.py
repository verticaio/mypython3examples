import requests

API_ENDPOINT = "https://hook.io/gelemli/red_mine"
API_KEY = "XXXXXXXXXXXXXXXXX"


source_code = '''
print("Hello, world!")
a = 1
b = 2
print(a + b)
'''

# data to be sent to api
data = {'api_dev_key': API_KEY,
        'api_option': 'paste',
        'api_paste_code': source_code,
        'api_paste_format': 'python'}

r = requests.post(url=API_ENDPOINT, data=data)

pastebin_url = r.text
print("The pastebin URL is:%s" %pastebin_url)