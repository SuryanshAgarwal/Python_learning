def funca():
    valur = 56
    
    def funcb():
        print(valur)

    funcb()

funca()

a=7
print(a)
def argument_by_ref(a):
    a=9
    print(a)
argument_by_ref(a)

print(a)