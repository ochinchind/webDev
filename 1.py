a = 47
cnt=0
while (a>0):
    if(a%2 == 0):
        a/=2
    a-=5
    cnt+=1
print(cnt)