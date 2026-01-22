binary=input("Enter in binary:")
decimal=input("Enter the decimal:")
i=0
count=0
while(i<len(binary)):
    if(binary[i]==decimal):
        count=count+1
    i=i+1
print("The total number of times",decimal,"has occured=", count)