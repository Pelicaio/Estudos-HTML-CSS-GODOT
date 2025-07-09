# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 09:50:25 2025

@author: caioq
"""




def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  

nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)
print(result)  
