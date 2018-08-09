#!/bin/python3

import os
import sys
import time
import requests
import io

from bs4 import BeautifulSoup

url = 'http://github.com'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html)

def main():
    SetURL()
    os.system('cls')
    PrintMenu()
    activity = int(input('Enter activity : '))
    Selector(activity)
    os.system('cls')
    main()

def Prettify():
    fo = open ('parsed.html','w+', encoding = 'utf-8')
    fo.write(soup.prettify())
    fo.close

def SetURL():
    url = str(input('Enter new URL : '))
    return

#Determines wich method to run
def Selector(Activity):
    if Activity == 1:
        Prettify()
    elif Activity == 2:
        pass
    elif Activity == 3:
        pass
    elif Activity == 4:
        pass
    elif Activity == 5:
        pass
    else:
        os.system('cls')
        quit()
    

def PrintMenu():
    print('[1]. Get HTML')
    print('[2]. Custom Find')
    print('[3]. Set URL')
    print('[4]. --')
    print('[5]. --')
    print('[6]. Exit\n')

main()