# 字典

user = {
    'name': 'Green',
    'age': 12,
    'gender': 'male'
}
# user = {'name': 'Green', 'age': 12, 'gender': 'male'}
print(user['name'])

# get
address = user.get('address')  # 返回None，因为没有address这个key
name = user.get('name')  # 返回Green

# 修改
user['address'] = 'china'  # 添加一个address键值对
user['age'] = 18           # age被修改为18
# 删除
del user['gender']  # 删除了gender这个键值对
# 清空
# user.clear()        # 清空了所有键值对

# 判断存在key
if 'age' in user:           # 判断age是否在user里面
    print(user['age'])

# keys，values, items
print(user.keys())      # 获得所有key值
print(user.values())    # 获得所有value值
print(user.items())     # 获得所有键值对


# 复杂结构
users = [
    {'name': 'Green', 'age': 12, 'like': ['apple']},
    {'name': 'Lucy', 'age': 13, 'like': ['apple', 'pear']},
    {'name': 'Lily', 'age': 11, 'like': ['orange', 'melon']}
]

print(users[1]['like'][0])
