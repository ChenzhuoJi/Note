university=['tsinghua','peking','fudan','shanghaijiaotong','nankai']
#打印特定元素
university[0],university[4]='nankai','tsinghua'
print(university)
#增添
university.append('zhongguokeji')
print(university)
#del语句删除
del university[-1]
print(university)
#插入
university.insert(2,'wuhandaxue')
print(university)
#pop（）语句删除
poped_university=university.pop()
print(university)
print(poped_university)
#remove删除法
university.remove('wuhandaxue')
print(university)
                                #在这些语句中，变量是最新的，print出来的是其上面最新的变量
                                
                                


