@echo off
#C:\Python27\Scripts\pyi-grab_version.exe Starter version.rc   
python -O -m PyInstaller -F Starter.py --icon=ico.ico
REM C:\Python27\Scripts\pyinstaller.exe -F Starter.py  
REM --add-data="ico.ico;ico" --icon=ico.ico
set /p DUMMY=Hit ENTER to continue...