import sys
from cx_Freeze import setup, Executable
import tkinter

base = None
icon = "icon.ico"

if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("Calculadora_CEDERJ.py", base=base, icon=icon)]
buildOptions = dict (
    packages = [],
    includes = ["tkinter"],
    include_files = [],
    excludes = []
)

setup(name ="Calculadora CEDERJ",
      version = "1.0",
      description = "My GUI Application!",
      options = dict(build_exe = buildOptions),
      executables = executables
      )
