from __future__ import print_function

num=90

prime=True

for number in range(2,10) :
    if num%number ==0 and num!=number :
      print(num ,"equal " ,number ," * ",num/number )
      prime=False
      break
    


if prime:
    print(num  ,  " this is Prime number . ")
else:
    print(num ,  "this is Not Prime number")


