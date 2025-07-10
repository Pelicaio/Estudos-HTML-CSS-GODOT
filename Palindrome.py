# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 14:26:42 2025

@author: caioq
"""
"Palindrome - When the integer reads the same number forward and backward"



def isPalindrome(self, x: int) -> bool:
    
    
    if x < 0: return False
    
    div = 1
    while x >= 10 * div:
        div *= 10
    
    while x:
        right = x % 10
        left = x//div
        
        if left != right: return False
        
        x = (x % div) // 10
        div = div / 100
        
    return True
            
            