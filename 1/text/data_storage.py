from pathlib import Path
import json

username=input('what is your name?')

path=Path('username.json')

contents=json.dumps(username)
path.write_text(contents)

print(f"We will remember you when you come back,{username}")