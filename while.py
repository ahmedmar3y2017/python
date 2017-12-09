from __future__ import print_function

sum=0
add=-1
while add !=0 :
    print("The Sum is  : " ,sum , end='\n')
    print("Enter the Number : " , end='')
    input=raw_input("type 0 to stop app")
    add=int(input)
    sum+=add
