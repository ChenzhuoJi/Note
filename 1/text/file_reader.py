from pathlib import Path

path=Path('pi_digits.txt')
contents=path.read_text()
print(contents)
#不能存放到同一个模块
