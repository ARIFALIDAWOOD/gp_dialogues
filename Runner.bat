@REM python path of .Rnv environment is current_dir\.Rnv\Scripts\python.exe
set python_path=%~dp0\.Rnv\Scripts\python.exe
@REM run python script main.py
call "%python_path%" "%~dp0main_prompt_copier.py" %*
