from collections import defaultdict

dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}

print(dic)

list_dict = defaultdict(list)

print(list_dict)

# defaultdict(list,{})                              
# 디폴트값이 list인 딕셔너리

list_dict['key1']                                       
# 값을 지정하지 않으면 빈 리스트로 초기화
print("key1 :",list_dict)
#key1 : defaultdict(<class 'list'>, {'key1': []})


list_dict['key2'] = 'test'                             
# 값을 지정하면 해당값으로 초기화

print("key2 :",list_dict)
#key2 : defaultdict(<class 'list'>, {'key1': [], 'key2': 'test'})

