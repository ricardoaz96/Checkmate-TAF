*** Settings ***

*** Variables ***

*** Keywords ***

PythonScreen to PSFScreen
    Log    Going from PythonScreen to PSFScreen
    Click    PythonScreen_PSF_TopMenuBarItem
    Wait Until Visible    PSFScreen_PSFLogo_Image

PythonScreen to DocsScreen
    Log    Going from PythonScreen to DocsScreen
    Click    PythonScreen_Docs_TopMenuBarItem
    Wait Until Visible    DocsScreen_PythonDoc_TitleText

PythonScreen to PyPIScreen
    Log    Going from PythonScreen to PyPIScreen
    Click    PythonScreen_PyPI_TopMenuBarItem
    Wait Until Visible    PyPIScreen_PythonHeaderLogo_Image

PythonScreen to JobsScreen
    Log    Going from PythonScreen to JobsScreen
    Click    PythonScreen_Jobs_TopMenuBarItem
    Wait Until Visible    JobsScreen_PythonJobBoardNumber_TitleText

PythonScreen to CommunityScreen
    Log    Going from PythonScreen to CommunityScreen
    Click    PythonScreen_Community_TopMenuBarItem
    Wait Until Visible    CommunityScreen_ThePythonCommunity_SubTitleText

PSFScreen to PythonScreen
    Log    Going from PSFScreen to PythonScreen
    Click    PythonScreen_Python_TopMenuBarItem
    Wait Until Visible    PythonScreen_PythonLogo_Image

DocsScreen to PythonScreen
    Log    Going from DocsScreen to PythonScreen
    Click    DocsScreen_PythonTopLinkTree_Link
    Wait Until Visible    PythonScreen_PythonLogo_Image

PyPIScreen to PythonScreen
    Log    Going from PyPIScreen to PythonScreen
    Go to URL    https://www.python.org/
    Wait Until Visible    PythonScreen_PythonLogo_Image

JobsScreen to PythonScreen
    Log    Going from JobsScreen to PythonScreen
    Click    PythonScreen_Python_TopMenuBarItem
    Wait Until Visible    PythonScreen_PythonLogo_Image

CommunityScreen to PythonScreen
    Log    Going from CommunityScreen to PythonScreen
    Click    PythonScreen_Python_TopMenuBarItem
    Wait Until Visible    PythonScreen_PythonLogo_Image

PSFScreen to DocsScreen
    Log    Going from PSFScreen to DocsScreen
    Click    PythonScreen_Docs_TopMenuBarItem
    Wait Until Visible    DocsScreen_PythonDoc_TitleText

PSFScreen to PyPIScreen
    Log    Going from PSFScreen to PyPIScreen
    Click    PythonScreen_PyPI_TopMenuBarItem
    Wait Until Visible    PyPIScreen_PythonHeaderLogo_Image

PSFScreen to JobsScreen
    Log    Going from PSFScreen to JobsScreen
    Click    PythonScreen_Jobs_TopMenuBarItem
    Wait Until Visible    JobsScreen_PythonJobBoardNumber_TitleText

PSFScreen to CommunityScreen
    Log    Going from PSFScreen to CommunityScreen
    Click    PythonScreen_Community_TopMenuBarItem
    Wait Until Visible    CommunityScreen_ThePythonCommunity_SubTitleText

DocsScreen to PSFScreen
    Log    Going from DocsScreen to PSFScreen
    Click    DocsScreen_PythonTopLinkTree_Link
    Wait Until Visible    PythonScreen_PythonLogo_Image
    PythonScreen to PSFScreen

PyPIScreen to PSFScreen
    Log    Going from PyPIScreen to PSFScreen
    Go to URL    https://www.python.org/
    Wait Until Visible    PythonScreen_PythonLogo_Image
    PythonScreen to PSFScreen

JobsScreen to PSFScreen
    Log    Going from JobsScreen to PSFScreen
    Click    PythonScreen_PSF_TopMenuBarItem
    Wait Until Visible    PSFScreen_PSFLogo_Image

CommunityScreen to PSFScreen
    Log    Going from CommunityScreen to PSFScreen
    Click    PythonScreen_PSF_TopMenuBarItem
    Wait Until Visible    PSFScreen_PSFLogo_Image

DocsScreen to PyPIScreen
    Log    Going from DocsScreen to PyPIScreen
    Click    DocsScreen_PythonTopLinkTree_Link
    Wait Until Visible    PythonScreen_PythonLogo_Image
    PythonScreen to PyPIScreen

DocsScreen to JobsScreen
    Log    Going from DocsScreen to JobsScreen
    Click    DocsScreen_PythonTopLinkTree_Link
    Wait Until Visible    PythonScreen_PythonLogo_Image
    PythonScreen to JobsScreen

DocsScreen to CommunityScreen
    Log    Going from DocsScreen to CommunityScreen
    Click    DocsScreen_PythonTopLinkTree_Link
    Wait Until Visible    PythonScreen_PythonLogo_Image
    PythonScreen to CommunityScreen

PyPIScreen to DocsScreen
    Log    Going from PyPIScreen to DocsScreen
    Go to URL    https://www.python.org/
    Wait Until Visible    PythonScreen_PythonLogo_Image
    PythonScreen to DocsScreen

JobsScreen to DocsScreen
    Log    Going from JobsScreen to DocsScreen
    Click    PythonScreen_Docs_TopMenuBarItem
    Wait Until Visible    DocsScreen_PythonDoc_TitleText

CommunityScreen to DocsScreen
    Log    Going from CommunityScreen to DocsScreen
    Click    PythonScreen_Docs_TopMenuBarItem
    Wait Until Visible    DocsScreen_PythonDoc_TitleText

PyPIScreen to JobsScreen
    Log    Going from PyPIScreen to JobsScreen
    Go to URL    https://www.python.org/
    Wait Until Visible    PythonScreen_PythonLogo_Image
    PythonScreen to JobsScreen

PyPIScreen to CommunityScreen
    Log    Going from PyPIScreen to CommunityScreen
    Go to URL    https://www.python.org/
    Wait Until Visible    PythonScreen_PythonLogo_Image
    PythonScreen to CommunityScreen

JobsScreen to PyPIScreen
    Log    Going from JobsScreen to PyPIScreen
    Click    PythonScreen_PyPI_TopMenuBarItem
    Wait Until Visible    PyPIScreen_PythonHeaderLogo_Image

CommunityScreen to PyPIScreen
    Log    Going from CommunityScreen to PyPIScreen
    Click    PythonScreen_PyPI_TopMenuBarItem
    Wait Until Visible    PyPIScreen_PythonHeaderLogo_Image

JobsScreen to CommunityScreen
    Log    Going from JobsScreen to CommunityScreen
    Click    PythonScreen_Community_TopMenuBarItem
    Wait Until Visible    CommunityScreen_ThePythonCommunity_SubTitleText

CommunityScreen to JobsScreen
    Log    Going from CommunityScreen to JobsScreen
    Click    PythonScreen_Jobs_TopMenuBarItem
    Wait Until Visible    JobsScreen_PythonJobBoardNumber_TitleText
