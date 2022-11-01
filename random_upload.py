import os
from random import choice, randint
import string
from time import sleep
import requests

def uploader(data ,url):
    myobj = {'mydata': data}
    requests.post(url, json = myobj)

def main():
    urls = os.environ['URLS']
    url_list = urls.split(",")
    ascii_letters = 10 * string.ascii_letters
    while True:
        sleep(randint(60,60*5))

        val = ""
        for i in range(0,randint(2000,500000)):
            val += ascii_letters

        url = choice(url_list)
        uploader(val,url)

if __name__=="__main__":
    main()