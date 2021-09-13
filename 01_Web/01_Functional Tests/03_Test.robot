*** Settings ***
Resource          WebRes.robot

*** Test Cases ***
01_Cenas
    Click    ex1
    Click    ex2
    Click    ex3
    Click    ex4
    Click    ex5
    Click    ex6

02_Cenas
    Click    painticon
    Click    paint

03_Cenas
    Comment    Check    chrome
    Click    chrome
    Click    search
    Press key    Backspace
    Write    banana
    Press key    Enter
