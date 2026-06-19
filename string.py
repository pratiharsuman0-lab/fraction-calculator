'''suman=['anil','amol','aditya','avi','alika']

print(suman)
suman.insert(2,'anju')
print(suman)
suman.append('zulu')
print(suman)
suman.remove('avi')
print(suman) 
i=suman.index('anil')
suman[0]='anil kumar'
print(suman)
suman.sort()
print(suman)
suman.reverse()
print(suman)'''

'''p='suman'
print(p.isalpha())
print(p.isnumeric())
print(len(p))
print(round(p))
'''
'''i=5
for i in range (1,10):
     print("5 X",{i}, "=", 5*i)'''


def multi(item):
 p=1
 for i in item:
        p=p*i

 return p
    
r = multi([1,2,-8])
print(r)