n = int(input("Enter a number for sequence: "))

a, b = 0, 1
count = 0

print("Fibonacci sequence:")
while count < n:
    print(a,end=" ")
    a, b = b,a+b
    count+=1

def fiboRecursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fiboRecursive(n - 1) + fiboRecursive(n - 2)

print()
n = int(input("Enter a number for nth term: "))
print(n,"th term is")
print(fiboRecursive(n))
