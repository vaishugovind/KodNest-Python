#read values
limit= int(input())
target=int(input())

#initializing values
count=0
total=0
found=False

#examine every number
for i in range(1,limit+1):
    #check multiple of three
    if i%3==0:
        count+=1
        total+=i
    if i== target:
        found=True
#Display the count ,total and search reasult
print("count:" ,count)
print("total:" ,total)
if found:
    print("Target found: 'Yes'")
else:
    print("Target not found: 'No'")


        
        
    