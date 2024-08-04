from  pathlib import Path
import json

def get_stored_username(path):
    """if name is stored,get it"""
    if path.exists():
        contents=path.read_text()
        username=json.loads(contents)
        return username
    else:
        return None
    
def greet_user():
    """greet user,and point name"""
    path=Path('username.json')
    username=get_stored_username(path) 
    if username:
        print(f"Welcome back,{username}")
    else:
        username=input("What's your name?")
        contents=json.dumps(username) 
        path.write_text(contents)
        print(f"We'll remember you wwhen you come back,{username}")
get_stored_username('jaidjaid')
greet_user()         
                
            