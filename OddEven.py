lower=int(input("Enter the lower limit: "))
upper=int(input("Enter the upper limit: "))

print("Even numbers: ")
for i in range(lower,upper+1):
    if(i%2==0):
        print(i)
print("Odd numbers: ")
for i in range(lower,upper+1):
    if(i%2==1):
        print(i)