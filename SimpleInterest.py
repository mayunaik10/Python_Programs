#Q2.Calculate and return simple interest
def SI(a, b, c):
    return (a*b*c)/100

print(end="Enter the Amount: ")
p = int(input())
print(end="Enter the Rate of Interest: ")
r = float(input())
print(end="Enter the Time: ")
t = float(input())
si = SI(p, r, t)
print("\nSimple Interest = " + str(si))