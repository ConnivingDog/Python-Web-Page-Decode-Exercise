#!/bin/python3

import os
import sys
import time
import requests
import io

from bs4 import BeautifulSoup
from classes.interface import Interface

def SetURL():
    try:
        user_url = input('Enter new URL http:// ')
        user_url = 'http://' + user_url
        return user_url

    except expression as identifier:
        print('There''s a problem with the URL...')

def SetFileName():
    user_file = input('Enter new file name : ')
    return user_file + '.html'

# parsing and BS objects

url = SetURL()
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, features='html.parser')

#

def main():
    os.system('cls')
    Interface.PrintMenu()
    activity = int(input('Enter activity : '))
    Selector(activity)
    os.system('cls')
    main()

def Prettify():
    filename = SetFileName()
    fo = open (filename,'w+', encoding = 'utf-8')
    fo.write(soup.prettify())
    fo.closes

# Selector methods. Determines wich method to run

def Selector(Activity):
    if Activity == 1:
        Prettify()
    elif Activity == 2:
        Interface.PrintMenu()
        FmsActivity = int(input('Enter search type : '))
        FindMenuSelector(FmsActivity)
    elif Activity == 3:
        filename = SetURL()
    elif Activity == 4:
        SetFileName()
    elif Activity == 5:
        pass
    else:
        os.system('cls')
        quit()

def FindMenuSelector(FmsActivity):
    if FmsActivity == 1:
        filename = SetFileName()
        fo = open (filename,'a+', encoding = 'utf-8')
        ptag = input('Enter tag : ')
        fo.write(str(soup.find(ptag)))
        fo.write('\n\n')
        fo.close

    elif FmsActivity == 2:        
        filename = SetFileName()
        fo = open (filename,'a+', encoding = 'utf-8')
        extension = input('Enter file extension (.***) : ')
        fo.write(str(soup.find(extension)))
        fo.write('\n\n')
        fo.close
        
    else:
        main()

os.system('cls')
main()