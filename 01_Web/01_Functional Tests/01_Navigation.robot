*** Settings ***
Test Setup        Start Application
Test Teardown     Close All Browsers
Resource          WebRes.robot

*** Test Cases ***
01_User can navigate between top bar menu
    [Documentation]    *01_User can navigate between top bar menu*
    ...
    ...    - _description:_ Verify that User can browse between top bar menu items: _Python | PSF | Docs | PyPI | Jobs | Community_
    Comment    Python Screen Navigation
    Go    to PSFScreen
    Go    to PythonScreen
    Go    to DocsScreen
    Go    to PythonScreen
    Go    to PyPIScreen
    Go    to PythonScreen
    Go    to JobsScreen
    Go    to PythonScreen
    Go    to CommunityScreen
    Go    to PythonScreen
    Comment    PSF Screen Navigation
    Go    to PSFScreen
    Go    to PythonScreen
    Go    to PSFScreen
    Go    to DocsScreen
    Go    to PSFScreen
    Go    to PyPIScreen
    Go    to PSFScreen
    Go    to JobsScreen
    Go    to PSFScreen
    Go    to CommunityScreen
    Go    to PSFScreen
    Comment    Docs Screen Navigation
    Go    to DocsScreen
    Go    to PythonScreen
    Go    to DocsScreen
    Go    to PSFScreen
    Go    to DocsScreen
    Go    to PyPIScreen
    Go    to DocsScreen
    Go    to JobsScreen
    Go    to DocsScreen
    Go    to CommunityScreen
    Go    to DocsScreen
    Comment    PyPI Screen Navigation
    Go    to PyPIScreen
    Go    to PythonScreen
    Go    to PyPIScreen
    Go    to PSFScreen
    Go    to PyPIScreen
    Go    to DocsScreen
    Go    to PyPIScreen
    Go    to JobsScreen
    Go    to PyPIScreen
    Go    to CommunityScreen
    Go    to PyPIScreen
    Comment    Jobs Screen Navigation
    Go    to JobsScreen
    Go    to PythonScreen
    Go    to JobsScreen
    Go    to PSFScreen
    Go    to JobsScreen
    Go    to DocsScreen
    Go    to JobsScreen
    Go    to PyPIScreen
    Go    to JobsScreen
    Go    to CommunityScreen
    Go    to JobsScreen
    Comment    Community Screen Navigation
    Go    to CommunityScreen
    Go    to PythonScreen
    Go    to CommunityScreen
    Go    to PSFScreen
    Go    to CommunityScreen
    Go    to DocsScreen
    Go    to CommunityScreen
    Go    to PyPIScreen
    Go    to CommunityScreen
    Go    to JobsScreen
    Go    to CommunityScreen
    Comment    Back To Original Screen
    Go    to PythonScreen
