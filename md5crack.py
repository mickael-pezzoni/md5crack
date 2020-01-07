#!/usr/bin/env python
# coding: utf-8

import hashlib
from colorama import Fore, Back, Style


def compareHash(hashWord, hashTarget):
    return hashWord == hashTarget


nbError = 0
nbFail = 0
hashTarget =  input('Hash >')
if (hashTarget == ''):
    hashTarget = '55b1f0cf0959941c96a70f977892a9f9'
wordlist = input('Wordlist >')
if (wordlist == ''):
    wordlist = '/home/micka/dev/wordlist/Wordlist-sample'
successWord = list()
with open(wordlist, 'r') as file:
    try:
        for line in file:
            word = line.replace('\n', '')
            hashWord = hashlib.md5(word.encode('utf-8')).hexdigest()
            if (compareHash(hashWord, hashTarget)):
                successWord.append(word)
                print(word + Fore.GREEN + ' [OK] ' + Style.RESET_ALL)
                break
            else:
                nbFail += 1
                print(word + Fore.RED + ' [FAIL] ' + Style.RESET_ALL)
    except UnicodeDecodeError as err:
        nbError += 1
        pass
    
    
print(Fore.RED + '\n-------- FAIL -------------\n')
print('nb : ' + str(nbFail) + Style.RESET_ALL)
print(Fore.RED + '\n-------- ERREUR -------------\n')
print('nb : ' + str(nbError) + Style.RESET_ALL)
print( Fore.GREEN + '\n-------- CORRECTE -----------\n')
print('\n'.join([ '+ ' + elt for elt in successWord]) + Style.RESET_ALL)