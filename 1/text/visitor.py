from pathlib import Path
path=Path('guest.txt')
contents=''
while True:
    content_adding=input('Enter your name:')
    contents+=f'{content_adding}\n'
    print(contents)
    path.write_text(contents)