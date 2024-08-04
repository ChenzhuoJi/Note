name_of_members=['admin','swindler','richman','queen','princess']
for members in name_of_members:
    if members=='admin':
        print(f'Hello {members.title()},would you like to see a staus report.')
    else:
        print(f'Hello {members.title()},thank you for logging again.')