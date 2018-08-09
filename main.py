#!/bin/python3

import os
import sys
import time
import requests
import io

from bs4 import BeautifulSoup

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
filename = SetFileName()
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, features='html.parser')

#

def main():
    os.system('cls')
    PrintMenu()
    activity = int(input('Enter activity : '))
    Selector(activity)
    os.system('cls')
    main()

def Prettify():
    fo = open (filename,'w+', encoding = 'utf-8')
    fo.write(soup.prettify())
    fo.close

# Selector methods. Determines wich method to run

def Selector(Activity):
    if Activity == 1:
        Prettify()
    elif Activity == 2:
        PrintFindMenu()
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
        fo = open (filename,'a+', encoding = 'utf-8')
        ptag = input('Enter tag : ')
        fo.write(str(soup.find(ptag)))
        fo.write('\n\n')
        fo.close
    elif FmsActivity == 2:
        fo = open (filename,'a+', encoding = 'utf-8')
        extension = input('Enter file extension (.***) : ')
        fo.write(str(soup.find(extension)))
        fo.write('\n\n')
        fo.close
    else:
        main()

#Menus

def PrintMenu():
    print('[1]. Get HTML')
    print('[2]. Find')
    print('[3]. Set URL')
    print('[4]. Set File Name')
    print('[5]. --')
    print('[6]. Exit\n')

def PrintFindMenu():
    os.system('cls')
    print('[1]. Tag')
    print('[2]. File Type (.***)')
    print('[3]. Back\n')

os.system('cls')
main()