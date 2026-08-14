num=int(input("ENTER THE NUMBER:"))
digit=list(str(num))
sum=0
for i in digit:
    pow=(digit.index(i))+1
    sum+=int(i)**pow
    
if sum==num:
    print(num,"IS A DISARIUM NUMBER")
else:
    print(num,"IS NOT A DISARIUM NUMBER")
