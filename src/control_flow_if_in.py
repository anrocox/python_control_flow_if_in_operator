#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 22, 2014

@author: anroco

In Python, how to use the in operator in an if statement?

En Python, ¿Cómo usar el operador in en una sentencia if?
'''

#the in operator check if a object exists within an iterable object container

#create a string
s = 'hello'

#check if s is equal to any of the values hello, hi or hallo
if s == 'hello' or s == 'hi' or s == 'hallo':
    print(s + '!, How are you?')

#create a list
l = ['hello', 'hi', 'hallo']

#use the in operator to replace various expressions that use the or operator
if s in l:
    print(s + '!, How are you?')
