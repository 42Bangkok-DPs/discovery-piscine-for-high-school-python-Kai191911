#!/usr/bin/env python3
num_list = [2,8,9,48,8,22,-12,2]
new_list = [num +2 for num in num_list if num > 5]


print("Original array :", num_list)
print("New array :", new_list)