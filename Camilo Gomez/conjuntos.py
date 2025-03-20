import random
A=set([random.randint(1,10)for i in range(1,10)])
A.remove(random.randint(1,10))
print("A=",A)
B={2,4,6}
print("B=",B)
print("A tiene",len(A),"elementos")
