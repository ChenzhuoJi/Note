from pathlib import Path

path=Path('pi_digits.txt')
contents=path.read_text()

lines=contents.splitlines()
pi_strings=''
for line in lines:
    pi_strings+=line
    
print(pi_strings)
print(len(pi_strings))

