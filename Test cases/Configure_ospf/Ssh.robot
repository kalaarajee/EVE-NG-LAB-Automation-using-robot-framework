*** Settings ***
Library  enable_ip.py

Metadata  Version  1.0
...       Author  Kadhim Alaarajee
...       Date    Mar  30 2020
...       Topology:-
...            ________________________________
...           |               R1     OSPF     |
...           |              /|\     AREA 0   |
...           |             / | \             |
...           |            /  |  \            |
...           |           /   |   \           |
...           |          /    |    \          |
...           |_____ R2_/____ |___  \R3_______|
...                          Sw2
...                          |
...                          |
...                          |
...          ___Internet___ Sw1  ___Management___
...
Documentation  A test suit for configuring ospf

*** Test Case ***
show commands

  [Documentation]  show information
  display ssh connection hosts
  display show ip
  display show run
configuration
    [Documentation]  ip and ospf configuration
    configure ip and ospf

*** Variables ***
${hostname1}=  10.1.1.51
${hostname2}=  10.1.1.52
${hostname3}=  10.1.1.53
${username}=  admin
${password}=  cisco
${show_ip}=  show ip int bri
${show_run}=  show run
*** Keywords ***
display ssh connection hosts
    [Documentation]  ssh connection
    ${ssh1}=  enable_ssh  ${hostname1}
    ${ssh2}=  enable_ssh  ${hostname2}
    ${ssh3}=  enable_ssh  ${hostname3}
    Log To Console  ${ssh1}
    Log To Console  ${ssh2}
    Log To Console  ${ssh3}
display show ip
    [Documentation]  display ip information
    ${show_ip_R1}=  cli  ${hostname1}  ${show_ip}
    ${show_ip_R2}=  cli  ${hostname2}  ${show_ip}
    ${show_ip_R3}=  cli  ${hostname3}  ${show_ip}
    Log To Console  ${show_ip_R1}
    Log To Console  ${show_ip_R2}
    Log To Console  ${show_ip_R3}

display show run
    [Documentation]  show running config
    ${show_run_R1}=  cli  ${hostname1}  ${show_run}
    ${show_run_R2}=  cli  ${hostname1}  ${show_run}
    ${show_run_R3}=  cli  ${hostname1}  ${show_run}
    Log To Console  ${show_run_R1}
    Log To Console  ${show_run_R2}
    Log To Console  ${show_run_R3}

configure ip and ospf
    [Documentation]  ip address and ospf configuration
    ${enable_ip_R1}=  enable_ip  R1
    ${enable_ip_R2}=  enable_ip  R2
    ${enable_ip_R3}=  enable_ip  R3
    log to Console  ${enable_ip_R1}
    log to Console  ${enable_ip_R2}
    log to Console  ${enable_ip_R3}
    ${enable_ospf_R1}=  enable_ospf  R1
    ${enable_ospf_R2}=  enable_ospf  R2
    ${enable_ospf_R3}=  enable_ospf  R3
    log to console  ${enable_ospf_R1}
    log to console  ${enable_ospf_R2}
    log to console  ${enable_ospf_R3}