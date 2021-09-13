*** Settings ***

*** Variables ***

*** Keywords ***
Start Application
    [Tags]    General
    Start Browser    https://www.python.org/
    Set Current Screen    PythonScreen

Close Applications
    [Tags]    General
    Close All Browsers

Search
    [Arguments]    ${for}
    [Tags]    PythonScreen
    ${searchString}    Set Variable Up    ${for}    for${SPACE}    '
    Click    PythonScreen_SearchTextField_Input
    Input Text Into    PythonScreen_SearchTextField_Input    ${searchString}    clearfirst=True
    Click    PythonScreen_GoSearch_Button
    Wait Until Visible    PythonScreen_SearchPython_Text
    Check Attribute    PythonScreen_SearchInput_Input    value    ${searchString}

Check Results
    [Arguments]    ${for}    ${expect}
    [Tags]    PythonScreen
    ${searchString}    Set Variable Up    ${for}    for${SPACE}    '
    ${expect}    Set Variable Up    ${expect}    and expect    '
    Log    ${searchString}
    Check Attribute    PythonScreen_ResultsElements_Container    innerText    ${searchString}    contains=${True}    respectCapitalLetters=${False}
    Run Keyword If    ${rc} == 0
    ...    ELSE IF
    ...    ELSE IF
    ...    ELSE IF
