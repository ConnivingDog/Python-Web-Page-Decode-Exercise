#!/bin/python3

import os
import sys
import time
import requests

from bs4 import BeautifulSoup

def main():
    #os.system('cls')

    url = 'http://github.com'
    r = requests.get(url)
    r_html = r.text

    soup = BeautifulSoup(r_html)

    print(soup.find_all('img'))
    #main()

def GetText():
    print(soup.get_text)

def Prettify():
    print(soup.prettify())

main()