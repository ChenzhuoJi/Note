#检查用户名
curent_users=['queen','Weierstrass','Cauthy,','Liouville','Poincare']
new_users=['king','Weierstrass','Cauthy','Euler','Newton','Kontsevich',"QUeen"]
current_user2=curent_users[:]
current_user2
for user1 in new_users:
    user=user1.lower()
    if user in current_user2:
        print(f"The name '{user1}' is already in use")
    else:
        print(f"The name '{user1}' can be used")
print(current_user2)