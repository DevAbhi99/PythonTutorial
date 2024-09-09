#While loop 

#print number from 1 to 10 using while loop

i=1

while i<=10:
    print(i)
    i=i+1



#For loop

#print number from 1 to 10 using for loop

for k in range(1,11):
    print(k)



#Break and Continue


#1) Break
for j in range(1,11):
    
    print(j)
    if j==5:
        break


#2) Continue



for index in range(1,11):

    if j==3:
        continue
    print(index)




#Looping through array


arr=[1,2,3,4,5,6,7,8,9,10]


target=input("Enter a target!")



for it in arr:
    if it==(int)(target):
        print("Found!")

