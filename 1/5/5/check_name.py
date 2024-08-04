#检查用户名
curent_users=['Queen','Weierstrass','Cauthy,','Liouville','Poincare']
new_users=['king','Weierstrass','Cauthy','Euler','Newton','Kontsevich',"QUeen"]
#创造小写副本curren_user2
current_user2=[]
for user2 in curent_users:
    user3=user2.lower()
    current_user2.append(user3)
#检测
for user1 in new_users:
    user=user1.lower()
    if user in current_user2:
        print(f"The name '{user1}' is already in use")
    else:
        print(f"The name '{user1}' can be used")
#观察我的小写副本
print(current_user2)
#非常乱，但是第一次想到这样用