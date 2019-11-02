s1 = set([1,2,3])
print(s1)
#{1,2,3}

s2 = set("Hello")
print(s2)
#{'o', 'l', 'e', 'H'}


s3 = set([1, 2, 3, 4, 5, 6])
s4 = set([4, 5, 6, 7, 8, 9])

print("교집합 : ", s3 & s4)

print("교집합2 : ", s3.intersection(s4))

print("합집합 : " , s3 | s4)

print("합집합2 : ", s3.union(s4))

print("차집합 : " , s3 - s4)

print("차집합2 : ", s3.difference(s4))


s1 = set([1,2,3])
s1.add(4)
print(s1)

s1.remove(2)
print(s1)

s1.update([6,7,8])
print(s1)

