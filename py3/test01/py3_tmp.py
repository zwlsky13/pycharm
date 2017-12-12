# a=[]
# if a:
#     print("yes")
# else:
#     print("NO")

# for i in range(1,10):
#     print(' '*(10-i)+'*'*i)
# a=[[1,2],3,4]
# b=a
# b[1]=5
# print(a)
# print(b)
# a=[1,2,3,4,5,3,5,6]
# c=[1,3,6,7,8,9]
# a=set(a)
# c=set(c)
# b=set(a)
# d={12:b}
# b.update({1,'dsa'})
# b.add('dsaf')
# b.pop()
# g=set("abcde")
# h=set('anbfr')
# print(a.intersection(c)) #求交集
# print(a.union(c))   #求并集
# print(a.difference(c))  #求差集
# print(a.symmetric_difference(c))#求对称差集

s=(x*2 for x in range(100000000000))
#print(s)    #generator object
# print(next(s))   #等价于s.__next__() 在py2里面
s.__next__()
print(next(s))