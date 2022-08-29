n=int(input())
max=0
smax=0
list1=[]
for i in range(n):
    a=int(input("  "))
    list1.append(a)
j=0
while j<len(list1):
    if list1[j]>max:
        max=list1[j]
    if list1[j]>smax and list1[j]<max:
        smax=list1[i]
    j=j+1
print(smax)    
    

