from math import sqrt
import math
num=int(input())
sqrt_number=list()
for i in range(num):
    number=int(input())
    number=abs(number)
    sqrt_number.append(str(sqrt(number)))

  
for i in sqrt_number:
    d=i.find('.')
    if len(i[d+1:])==1:
        print(f'{i[:d]}.0000')
    else:
        if len(i[:d])==1:
            print(f'{i[:6]}')
        else:
            print(f'{i[:7]}')
  


