*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${Browser}  Chrome
${URL}  https://10.1.1.150/#/login  { USE your information }


*** Test Cases ***
Robot First Test Case
   open Browser  ${URL}  ${Browser}
   Maximize Browser Window
   Click Button  xpath://button[@id='details-button']
   Click link  xpath://a[@id='proceed-link']
   Sleep  5 seconds
   #Select From List By Value  //select[@name="html5"]  -1  to switch to  legacy console current is HTML5 console
   Input Text  xpath://input[@ng-model='username']  username
   Sleep  5 seconds
   Input Text  xpath://input[@ng-model='password']  password
   Sleep  5 seconds
   Click Button  xpath://button[@id='btnlogin']
   Sleep  15 seconds
   Click link  xpath=(//a[@class="pointer ng-binding"])[16]
   Sleep  20 seconds
   Click Element  //button[@class="btn btn-primary btn-flat ng-scope"]
   Sleep  15 seconds
   Click link  //a[@title="More actions"]
   Click link  xpath=(//a[@href="javascript:void(0)"])[19]
   Sleep  30 seconds
   Click Element  xpath=(//img)[12]
   Click Element  //div[@id="framewrap30"]
   Click Element  xpath=(//img)[3]
   Click Element  //div[@id="framewrap1"]
   Click Element  xpath=(//img)[5]
   Click Element  //div[@id="framewrap3"]
   Sleep  300 seconds  #  I choose 300 second it could be more or less based on your environment













