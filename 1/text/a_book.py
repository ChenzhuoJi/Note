from pathlib import Path
path=Path("ghost.txt")
contents=path.read_text()
contents=contents.lstrip()
