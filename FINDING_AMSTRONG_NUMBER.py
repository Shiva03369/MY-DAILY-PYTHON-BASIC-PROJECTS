numa=int(input("ENTER THE NUMBER"))
l=len(str(numa))
digits=list(str(numa))
sum=0
for i in digits:
    i=int(i)
    sum=sum+(i**l)
if int(sum)==numa:
    print(numa,"Is An AMSTRONG NUMBER")
else:
    print(numa,"IS NOT AN AMSTRONG NUMBER")
