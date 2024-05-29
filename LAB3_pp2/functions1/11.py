s = str(input())

def palindrome(s):
    if s == s[::-1]: #[::-1] - reverse 
        return True
    else:
        return False

print(palindrome(s))