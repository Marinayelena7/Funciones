#programa para ver el mayor de tres

def mayordetres(a, b, c):
    if(a>b):
        if(a>c):
            return a 
        else:
            return c
    else:
        if(b>c):
            return b
        else:
            return c

print (mayordetres(1,2,3))

