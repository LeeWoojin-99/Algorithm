entry=input().upper()
dic={}
for i in entry:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
max_key=max(dic, key=dic.get)
max_value=dic[max_key]
dic.pop(max_key)
if max_value in dic.values():
    print("?")
else:
    print(max_key)

#정답
