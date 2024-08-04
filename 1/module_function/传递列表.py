def greet_users(names):
    for name in names:
        msg=f'Hello,{name.title()}'
        print(msg)

usersname=['hannzh','ty','margot']
greet_users(usersname)