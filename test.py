import redis
import re

# pool = redis.ConnectionPool(host='192.168.1.41', port=6409, db=0)
#
# r = redis.Redis(connection_pool=pool)
# # print(r.mget("863288446120_LastCustomer"))
# keys = r.keys()
# # print(keys)
# for key in keys:
#
#   print(key.decode(), r.mget(key),r.ttl(key))


# pipe = r.pipeline()  
# pipe_size = 100000  
""""
len = 0
key_list = []
print(r.pipeline())



for key in keys:  
    key_list.append(key)  
    msg = pipe.get(key)
    if len < pipe_size:  
        len += 1
    else:
        for (k, v) in zip(key_list, pipe.execute()):  
            print(k, v)
        len = 0
        key_list = []


for (k, v) in zip(key_list, pipe.execute()):  
    print(k, v)
"""
#keys = r.keys()
#print(type(keys))
#print(keys)

# l = ['Python', 'C++', 'Java']
# #追加元素
# l.append('PHP')
# print(l)
# print(l.append('asdf'))
# print(l)
# b_group = 'all'
# if b_group == 'zs' or 'all':
#     print('ok')

# imgCorrespondenceJK = {'a':2,'b':3}
# f = imgCorrespondenceJK[None]
# print(f)
a = ' aaa  '
print(a.strip())