'''
Title     : sWAP cASE
Subdomain : Strings
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/swap-case/problem
'''
__author__ = 'arsho'
def swap_case(s):
    newstring = ""
    
    for item in s:
        if item.isupper():
            newstring += item.lower()
        else:
            newstring += item.upper()
            
    return newstring
