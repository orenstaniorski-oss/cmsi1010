def blocks(n):
    return 0 if n <= 0 else blocks(n - 1) + n

print(blocks(8))
print(blocks(0))
print(blocks(-1))
print(blocks(1))

def sum_of_digits(n):
    return n if n<=10 else sum_of_digits(n//10)+n%10

print(sum_of_digits(1234))

def factorial(n):
    return 1 if n<1 else factorial(n-1)*n

print(factorial(4))

def is_palindrome(s):
    n=len(s)
    return True if n<1 else s[n//2-1]==s[n//2+1]

print(is_palindrome('racecar'))