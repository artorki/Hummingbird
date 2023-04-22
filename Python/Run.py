import platform, os, sys, json

System = platform.uname()[0]
Clear = lambda : os.system ("cls" if System == "Windows" else "clear")
Clear()


libraries = ["Config", "colorama", "time", "requests", "socket"]

def Check(x) :
    try:
        exec (f"import {x}")
    except:
        sys.exit (f" [-] Error (Import-L14) - Install {x}")
x = [Check(i) for i in libraries]

import Config, socket, requests

from colorama import Fore, init
init()
white, cyan = "\033[0;37m", "\033[96m"


try:
    Connection = requests.get ("http://google.com")
except:
    sys.exit ("\n [-] Error (Connection-L27) - Check Internet")

def Banner() :
    print (f"""{white}
  _                               _             _     _         _ 
 | |__  _   _ _ __ ___  _ __ ___ (_)_ __   __ _| |__ (_)_ __ __| |
 | '_ \| | | | '_ ` _ \| '_ ` _ \| | '_ \ / _` | '_ \| | '__/ _` |
 | | | | |_| | | | | | | | | | | | | | | | (_| | |_) | | | | (_| |
 |_| |_|\__,_|_| |_| |_|_| |_| |_|_|_| |_|\__, |_.__/|_|_|  \__,_|
                                          |___/
 =================================================================
""")                           


def Modules () :
    SubList = Config.SubList
    Admin = Config.Admin
    Port = Config.Port
    Iran = ""

    try:
        URL = input (f"{cyan} [{white}~{cyan}] {white}Enter URL: {cyan}") .lower()
        URL.replace("https://","").replace("http://","").replace("www.","") if "https://" == URL or "http://" == URL or "www." == URL else ...
    except:
        print (f"{cyan} [{white}-{cyan}] {white}Error")


    print (f"{white} =================================================================\n")
    print (f"{cyan} [{white}~{cyan}] {white}Location, URL, IP")

    for i in SubList :
        if i != "" :
            URL2 = i + "." + URL
        else:
            pass
        try:
            IP = socket.gethostbyname (URL2)
            Location = requests.post ("https://iplocation.com/", data={"ip": f"{IP}"}) .text
            Location = str(json.loads (Location) ["country_name"]) .replace(" ","")
            print (f"{cyan} [{white}+{cyan}] {cyan}{Location}, {URL2}, {IP}")
            if Iran == "" and Location == "Iran" :
                Iran = IP
            URL2 = URL
        except:
            pass


    print (f"{white} =================================================================\n")
    print (f"{cyan} [{white}~{cyan}] {white}Admin Page URL")
    
    for i in Admin :
        URL2 = "http://" + URL + "/" + i
        try:
            r = requests.get (URL2)
            print (f"{cyan} [{white}+{cyan}] {cyan}{URL2}") if r.status_code == 200 else ...
            URL2 = URL
        except:
            pass


    print (f"{white} =================================================================\n")
    print (f"{cyan} [{white}~{cyan}] {white}Port, service")

    for i in Port :
        try:
            scan = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
            scan = scan.connect_ex ((Iran, i))
            if scan == 0 :
                service = socket.getservbyport (i)
                print (f"{cyan} [{white}+{cyan}] {cyan}{service}, {i}")
        except:
            pass


    print (f"{white} =================================================================\n")
    print (f"{cyan} [{white}~{cyan}] {white}Extract Links")

    try:
        r = requests.get ("https://api.hackertarget.com/pagelinks/?q=shakerin.ir")
        Links = (r.text).split("\n")

        [print (f"{cyan} [{white}+{cyan}] {cyan}" + i) for i in Links]
    except:
        pass


Banner()
Modules()
