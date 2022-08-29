n=int(input())
for i in range(n):
    x=int(input())
    y=int(input())
    if x<y:
        print("FIRST")
    if x==y:
        print("ANY")
    if x>y:
        print("SECOND")