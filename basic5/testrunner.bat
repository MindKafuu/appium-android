@echo off

set /P name="Enter your feature name: "

set cmd = behave .\features\tests\%name%.feature

if %name% == - %cmd% = behave

@REM set count = 1
@REM :loop
@REM set /a count = %count% + 1
@REM echo %count% > config.txt
@REM behave .\features\tests\%name%.feature

@REM if %count% == 3 goto exitloop
@REM goto loop
@REM :exitloop


%cmd%

