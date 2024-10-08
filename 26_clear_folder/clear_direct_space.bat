@echo off
setlocal enabledelayedexpansion

set "current_dir=%cd%"

mkdir "Officebaz" 2>nul
for %%F in (*) do (
	set "filename=%%~nF"
	set "ext=%%~xF"

	if not "!ext!" == "" (
		if not "!ext!" == ".bat" (
			if not "!ext!" == ".zip" (
if not "!ext!" == ".rar" (
			set "ext =! ext :~ 1!"
			mkdir "Officebaz\!ext!" 2>nul
			move "%%F" "Officebaz\!ext!"
		)
	)
)
)
)
for /d %%D in (*) do (
	if exist "%%D.zip" (
		mkdir "zip" 2>nul
		move "%%D" "zip\%%D"
		move "%%D.zip" "zip\%%D.zip"
	)
)
for /d %%D in (*) do (
	if exist "%%D.rar" (
		mkdir "rar" 2>nul
		move "%%D" "rar\%%D"
		move "%%D.rar" "rar\%%D.rar"
	)
)

rem برگرداندن
cd "%current_dir%"

echo "Done."
pause