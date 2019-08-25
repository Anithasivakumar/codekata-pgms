j=int(input())
s=0
while(j>0):
  r=j%10
  s=s+r*r
  j=j//10
print(s)
