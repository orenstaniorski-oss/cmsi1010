def sum_of_digits(n):
    if n==0:
        return 0
    else:
        return sum_of_digits(n//10)+n%10

def factorial(n):
    if n==0:
        return 1
    else:
        return factorial(n-1) * n

def is_palindrome(s):
    if len(s)<=1:
        return True
    elif s[0]!=s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])

def print_count_down(n):
    if n<=0:
        print("BOOM")
    else:
        print(n)
        return print_count_down(n-1)

print_count_down(0)