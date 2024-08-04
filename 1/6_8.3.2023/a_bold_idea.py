#提取键值对分别到一个列表中
namelist=[]
lanlist=[]
favorite_language={'jen':'python',
                   'alice':'c',
                   'newton':'c++',
                   'quenn':'python'}
for name in favorite_language.keys():
     namelist.append(name)
print(namelist)


for language in favorite_language.values():
    lanlist.append(language)
print(lanlist)


#去除重复元素
namelist.append('jen')
namelist_2=[]
for name in set(namelist):
    namelist_2.append(name)
print(namelist_2)