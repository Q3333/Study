import collections
 
myList = ['a', 'b', 'c', 'c', 'a', 'a']
myCounter = collections.Counter(myList)
print('myCounter:', myCounter)
# myCounter: Counter({'a': 3, 'c': 2, 'b': 1})