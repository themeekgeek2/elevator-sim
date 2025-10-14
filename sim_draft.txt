cls
@echo off
setlocal

setx prompt Choice:$G

echo ELEVATOR SIM LOADING...
echo .
pause

rem Since there's no splashscreen yet, the first scene will be the lobby
rem CUSTOM VARIABLE LIST:
rem   usr_ is the user's input on the cmd

:START
type outsidev2.txt
type floor_1_message.txt
rem .
set /p "usr_= "
rem .
if %usr_%=="1" goto:FLOOR_2
if %usr_%=="2" goto: FLOOR_3
if %usr_%=="exit" goto: EXIT_PROG
pause
goto:START

:FLOOR_2
type go_up.txt
pause
type insidev2.txt
pause
type floor_2_message.txt
pause
type 

:FLOOR_3
type go_up.txt
pause
type insidev2.txt
pause
type floor_3_m.txt

:EXIT_PROG
type exit_prompt.txt





