# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""
"Hash table Bucket"
my_list = [None,None,None,None,None,None,None,None,None,None] 

"Hash Function"
def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)
        
    return sum_of_chars % 10
print("'Bob' has hash code:", hash_function('Bob'))
    
  




"Inserting an Element"

def add(name):
   index = hash_function(name)
   my_list[index] = name
    
add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
print(my_list)




