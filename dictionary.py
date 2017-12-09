from __future__  import print_function

dic={"name"  : "ahmed" ,"address" : "tanta" ,"age" : 20}

print(dic)
print(dic.keys())
del dic["name"]
for i in dic :
    print(dic[i])

