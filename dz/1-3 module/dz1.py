

# print('x y z w')
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 if (x or y) and not(y == z) and not(w):
#                     print(x,y,z,w)

# def f(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     if n == 3:
#         return 1
#     if n > 3:
#         return f(n-3) + f(n-2) + f(n-1)
# print(f(11))

# s = '1'*100
# while int(s)>0 and '111' in s:
#     s = s.replace('11', '2',1)
#     s = s.replace('22','1',1)
# print(s)

# f=''
# s= 49**8 + 7**24 - 7
# while s>0:
#     a = s%7
#     f = str(a)+f
#     s = s//7
# print(f)
for a in range(1,100):
    for x in range(100):
        for y in range(100):
            if ((4*x + 3*y < a)or (x>=y)or (y>=13))==1:
                print(a)

# from turtle import*
#
# r = 15
# tracer(0)
#
# for i in range(4):
#     fd(10*r)
#     rt(60)
#     fd(10)
#     rt(120)
# up()
#
# for x in range(-30,30):
#     for y in range(-30,30):
#         goto(x*r,y*r)
#         dot(3, 'pink')
#
# update()
# k=0
# for f1 in 'regina':
#     for f2 in 'regina':
#         for f3 in 'regina':
#             for f4 in 'regina':
#                 for f5 in 'regina':
#                     s = f1+f2+f3+f4+f5
#                     if s.count('r')==1 and s.count('g')==1 and s.count('n')<=1:
#                         k+=1
# print(k)

# for n in range(1,100):
#     r = bin(n)[2:]
#     s=0
#     for j in range(len(r)):
#         s += int(r[j])
#     r += str(s%2)
#     f=0
#     for t in range(len(r)):
#         f+= int(r[t])
#     r+=str(f%2)
#     y = int(r,2)
#     if y>85:
#         print(n)

