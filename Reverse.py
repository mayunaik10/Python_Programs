#Q.2 Print an n digit number in reverse order
num=int(input("Enter the the number to be reversed:  "))
rev = 0
while num != 0:
 digit = num % 10
 rev = rev* 10 + digit
 num //= 10
print("Reversed Number: " + str(rev))