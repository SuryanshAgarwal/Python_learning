import operator

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = sorted(d.items(), key=operator.itemgetter(0),reverse=True)
print('Dictionary in descending order by value : ',sorted_d)


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}

for d in (dic1, dic2, dic3):
    dic4.update(d)
    

def is_value_present(dic4,x):
    if x in dic4.items():
        return True
    else:
        return False

print(is_value_present(dic4,40))

def create_dict(n):
    dic5 = {x:x**2 for x in range(1,n+1)}
    return dic5

print(create_dict(5))

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}

d2.update(d1)
print(d2)

student_data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}
result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
    else:
        print(value.keys())

# print(result)