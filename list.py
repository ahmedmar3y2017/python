from __future__ import print_function


list=["ahmed","mohamed" ,"mar3y"]
length=len(list)
print(length)
print(list.index("mar3y"))

for i in range(0,length):
    print(i ,"   :   ", list[i])


index1 = raw_input("Enter the Index you want : ")

index2 =int(index1);

name1=raw_input("Enter the name : ")

list[index2]=name1

print(list)

name2 = raw_input("Enter the name to append")
list.append(name2)
print(list)

name3 =raw_input("Enter the name to remove")

list.remove(name3)
print(list)









