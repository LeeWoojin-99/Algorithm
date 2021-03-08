
import pickle

f=open("test.txt","wb")
data={1:"halo",2:"world"}
pickle.dump(data, f)
f.close

f=open("test.txt","rb")
data=pickle.load(f)
print(data)
f.close