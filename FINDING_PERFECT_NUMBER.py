#Check for Perfect Number
n=int(input("ENTER THE NUMBER:"))
sum=0
i=1
while i<n:
    if n%i==0:
        sum+=i
    i+=1
if n==sum:
    print(n,"IS A PERFECT NUMBER")
else:
    print(n,"IS NOT A PERFECT NUMBER")
    
