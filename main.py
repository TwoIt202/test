import urllib.request

url = "https://github.com/TwoIt202/test/blob/main/test.py"
urllib.request.urlretrieve(url, 'test.py')