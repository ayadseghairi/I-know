@echo off
setlocal enabledelayedexpansion
set "file=c:\zoui\s.txt"
set /p value=<"%file%"
if !value! equ 0 (
  set "new_value=1"
  python3 c:/zoui/main.pyw
) else (
  set "new_value=0"
)
echo !new_value!>"%file%"

