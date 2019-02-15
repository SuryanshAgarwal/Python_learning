def ndegrees(num):
    ans = True
    n, tempn,i = 2, 2, 1
    while ans:
        if str(tempn) in num:
            i += 1
            tempn = pow(n, i)
        else:
            ans = False
    return i-1
print(ndegrees("2481632"))
print(ndegrees("28163264"))


def factendzero(n):
  x = n // 5
  y = x 
  while x > 0.01:
    x /= 5
    y += int(x)
  return y
       
print(factendzero(5))
print(factendzero(12))
print(factendzero(100))

def number_of_notes(amount):
    n_500 = amount//500
    amount = amount % 500
    n_200 = amount//200
    amount = amount%200

    return n_500, n_200

print(number_of_notes(200))

def new_list(n):
    temp = []
    a,b,c,d = 1,1,1,1
    temp.extend([a,b,c,d])
    while(n>0):
        e=a+b+c+d
        temp.append(e)
        a,b,c,d = temp[-1], temp[-2], temp[-3], temp[-4]
        n-=1
    return temp

array = new_list(6)
        
def sdigits_snu(num):
    if num <= 0:
        return None
    else:
        num_c =  num
        s=0
        while num>0:
            s += (num%10)
            num = num//10
        print(num_c-s)
        sdigits_snu(num_c-s)    

sdigits_snu(21)


def divisor(n):
  
  x = len([i for i in range(1,n+1) if not n % i])
  return x

print(divisor(15))

import itertools
def sum_distinct_pairs(arr):
    perm = itertools.permutations(arr)


def ap_or_gp(arr):
    l = len(arr)
    for i in range(l):
        if i>0 and i<l-1:
            label = None
            d1 = arr[i]-arr[i-1]
            d2 = arr[i+1]-arr[i]
            d3 = arr[i+1]-arr[i-1]
            if( d1==d2) and (d3== 2*d1) and (d3 ==2*d2):
                label = "AP"

            r1 = arr[i]/arr[i-1]
            r2 = arr[i+1]/arr[i]
            r3 = arr[i+1]/arr[i-1]
            if (r1 == r2) and (r3==2*r2) and (r3==2*r1):
                label = "GP"
    if label == "AP":
        return d1
    elif label == "GP":
        return r1
    else:
        return None

series = ap_or_gp([1,2,3,8])