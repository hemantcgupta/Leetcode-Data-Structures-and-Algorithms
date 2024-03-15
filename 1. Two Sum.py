# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 20:02:21 2023

@author: Hemant
"""

def twoSum(nums, target):
    num_to_index = {}  
    for i, num in enumerate(nums):
        remaning = target - num
        if remaning in num_to_index:
            return [num_to_index[remaning], i]
        num_to_index[num] = i
    return None

nums = [2, 7, 11, 15]
target = 22
result = twoSum(nums, target)
print(result) 
