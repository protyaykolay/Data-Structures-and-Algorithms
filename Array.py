import array

val = array.array('i',[1,2,3,4,5,6])

for i in range(0,6):
    print(val[i],end=" ")
    
print('\n')

for x in val:
    print(x,end=" , ")
    
print('\n')
    
print('#############################################################')

import array as arr

val = arr.array('i',[1,2,3,4,5,6])

for i in range(0,6):
    print(val[i],end=" ")
    
print('\n')

for x in val:
    print(x,end=" , ")
    
print('\n')
    
print('#############################################################')

from array import *

val = array('i',[1,2,3,4,5,6,7,8,9])

for i in range(0,6):
    print(val[i],end=" ")
    
print('\n')
    
for i in range(0,len(val)):
    print(val[i],end=" ")
    
print('\n')

for x in val:
    print(x,end=" , ")
    
print('\n')

val.insert(1,50)
val.append(100)
val[2] = 200

for i in range(0,len(val)):
    print(val[i],end=" ")

print('\n')

print(val.typecode)

val.reverse()

for i in range(0,len(val)):
    print(val[i],end=" ")
    
print('\n')

print('#############################################################')

from array import *

val = array('d',[1,2,3,4,5,6,7,8,9.5])

for i in range(0,6):
    print(val[i],end=" ")
    
print('\n')
    
for i in range(0,len(val)):
    print(val[i],end=" ")
    
print('\n')

for x in val:
    print(x,end=" , ")
    
print('\n')

print('#############################################################')

from array import *

val = array('u',['a','b','c'])
    
print('\n')
    
for i in range(0,len(val)):
    print(val[i],end=" ")
    
print('\n')

for x in val:
    print(x,end=" , ")
    
print('\n')

print('#############################################################')

from array import *

val = array('i',[1,2,3,4,5,6,7,8,9])

copyArray = array(val.typecode,(x for x in val))
# copyArray = array(val.typecode,(x*2 for x in val))

copyArray.pop(3)
copyArray.pop()
copyArray.remove(5)

for i in range(0,len(copyArray)):
    print(copyArray[i],end=" ")

print('\n')
    
print('#############################################################')

from array import *

val = array('i',[1,2,3,4,5,6,7,8,9])

abc = val[2:5]
abc = val[2:-3]
abc = val[::-1]

for i in range(0,len(abc)):
    print(abc[i],end=" ")

print('\n')
    
print('#############################################################')

from array import *

arr = array('i',[])

n = int(input("Enter a number : "))

for i in range(0,n):
    arr.append(int(input("Enter next input : ")))
    
for x in arr:
    print(x,end=" ")

print('\n')
    
print('#############################################################')

from array import *

arr = array('i',[12,23,45,234,134,235])

i = arr.index(45)   
i = arr.index(134)

print(i)

print('\n')
    
print('#############################################################')

from numpy import *

val = array([1,2,4.5,'a'])
val = array([1,2,4],float)

for x in val:
    print(x,end=" ")

print('\n')
    
print('#############################################################')

from numpy import *

val = linspace(10,20,5)

for x in val:
    print(x,end=" ")

print('\n')

print('#############################################################')

from numpy import *

val = arange(10,20,2)

for x in val:
    print(x,end=" ")

print('\n')
    
print('#############################################################')    
    
from numpy import *

val = logspace(10,20,2)

for x in val:
    print(x,end=" ")

print('\n')
    
print('#############################################################') 

from numpy import *

val = zeros(10)
val = ones(10)
val = full(10,5)

for x in val:
    print(x,end=" ")

print('\n')

print('#############################################################') 

from numpy import *

zero = array(10)
print(zero)

print('\n')

one = array([1,2,3,4,5]) 
print(one)

print('\n')

two = array([[1,2,3],[4,5,6],[7,8,9]])
print(two)

print('\n')

three = array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(three)
