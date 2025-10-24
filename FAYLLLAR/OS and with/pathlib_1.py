from pathlib import Path

file=Path("../intro.txt")
Path.write_text(file,"hello")