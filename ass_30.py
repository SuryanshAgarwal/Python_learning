import numpy


# def sdigits_snu(num):
#     if num <= 0:
#         return None
#     else:
#         num_c =  num
#         s=0
#         while num>0:
#             s += (num%10)
#             num = num//10
#         print(num_c-s)
#         sdigits_snu(num_c-s)    

# sdigits_snu(21)

import math
def isPrime(n):
    if n==1:
        return False
    elif n==2:
        return True
    elif n>2 and n%2==0:
        return False
    else:
        greatest_divisor = math.floor(math.sqrt(n))
        for i in range(3,greatest_divisor,2):
            if n%i == 0:
                return False
        return True
        
for i in range(1,20):
    print(i,isPrime(i))
# def palindrom(num):
#     n = num
#     b = 0
#     while n>0:
#         a = n%10
#         n = n//10
#         b = b*10 +a
#     if num == b:
#         return num
#     else:
#         s = b+num
#         palindrom(s)
    
# num = palindrom(152)
# print(num)

# arr = [1,2,3,4]
# arr.reverse()
# n=1234
# k= str(n)
# m = int(k[::-1])
# n += m
from operator import itemgetter
temp_tupple = [(1,'a'),(2,'b'),(9,'i'),(4,'d')]
temp_tupple.sort(key=itemgetter(1))
print(temp_tupple)
arr = [1,2,6,3,5]
arr.sort()
print(arr)

original_list = [10, 22, 44, 23, 4]
new_list = original_list
print(new_list)

import itertools
original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
new_merged_list = list(itertools.chain(*original_list))
print(new_merged_list)


import random
color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
print(random.choice(color_list))

print(color_list[random.randint(0,len(color_list)-1)])
L = [12,42,57,1]
a = ''.join(map(str,L))