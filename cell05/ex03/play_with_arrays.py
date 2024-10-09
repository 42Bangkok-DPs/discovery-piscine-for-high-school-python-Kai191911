#!/usr/bin/env python3
num_list = [2,8,9,48,8,22,-12,2]
set_num_list = set(num_list)

num = [num + 2 for num in set_num_list if num > 5]

print(num)