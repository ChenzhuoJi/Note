def get_formatted_name(first_name,last_name):
    """返回规范格式的姓名"""
    full_name=f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nPlease tell me your name :")
    print("(enter 'q' at any time to quit)")
 
    f_name=input("First_name:")
    if f_name=="q":
        break
    
    l_name=input("Last_name:")
    if l_name=="q":
        break
    
    #实参要参照input的变量
    
    formatted_name=get_formatted_name(f_name,l_name)
    print(f"\nHello,{formatted_name}")
    