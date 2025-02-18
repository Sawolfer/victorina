import sys
from cx_Freeze import setup, Executable

build_options = {
    "packages": ["tkinter", "PIL"],
    "excludes": ["tkinter.ttk"],
    "include_files": ["sapsan-facts.jpg", "article.txt"]
}

base = "Win32GUI" if sys.platform == "win32" else None

executables = [
    Executable("Victorina.py", base=base)
]

setup(
    name="Quiz Application",
    version="1.0",
    description="Supply Chain Quiz Application",
    options={"build_exe": build_options},
    executables=executables
)