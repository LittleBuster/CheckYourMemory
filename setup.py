import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(name = 'CheckYourMemory',
      version = '0.0.1',
      executables = [Executable('checkmem.py', icon='images/app.ico', base=base)],
      options = {'build_exe': {'includes': ['sip']}})
