prompt='\nTell me something,and I will repeat it back to you:'
prompt+="\nEnter 'quit' to end the program."
msg=""
while msg!='quit':
    msg=input(prompt)
    if msg!='quit':
        print(msg)