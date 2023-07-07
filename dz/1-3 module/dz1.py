

def g(n):
    if n == n[::-1]:
        return True
    else:
        return False

n = str(input())
l = g(n)
print(l)

