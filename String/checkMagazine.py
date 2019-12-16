# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 16:48:56 2019

@author: 29132
"""
def getwordsnum(string):
    dict1={}
    for i in string:
        dict1[i]=0
    for i in string:
        dict1[i]+=1
    return dict1
def checkMagazine(magazine, note):
    hash1=getwordsnum(magazine)
    hash2=getwordsnum(note)
    for i in hash2.keys():
        if i not in hash1.keys():
            print('No')
            return
        else:
            if hash2[i]>hash1[i]:
                print('No')
                return
            else:
                continue
    print('Yes')
    
magazine='apgo clm w lxkvg mwz elo bg elo lxkvg elo apgo apgo w elo bg'
note='elo lxkvg bg mwz clm w'
#magazine='give me one grand today night'
#note='give one grand today'
magazine=magazine.split(' ')
note=note.split(' ')
hash1=getwordsnum(magazine)
hash2=getwordsnum(note)
result=checkMagazine(magazine, note)

