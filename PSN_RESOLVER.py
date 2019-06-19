
import requests
logo="""

                    ________  ________  ________                                       
                   |\   __  \|\   ____\|\   ___  \                                     
                   \ \  \|\  \ \  \___|\ \  \\ \  \                                    
                    \ \   ____\ \_____  \ \  \\ \  \                                   
                     \ \  \___|\|____|\  \ \  \\ \  \                                  
                      \ \__\     ____\_\  \ \__\\ \__\                                 
                       \|__|    |\_________\|__| \|__|                                 
                                \|_________|                                           
                                                                                       
                                                                                       
 ________  _______   ________  ________  ___       ___      ___ _______   ________     
|\   __  \|\  ___ \ |\   ____\|\   __  \|\  \     |\  \    /  /|\  ___ \ |\   __  \    
\ \  \|\  \ \   __/|\ \  \___|\ \  \|\  \ \  \    \ \  \  /  / | \   __/|\ \  \|\  \   
 \ \   _  _\ \  \_|/_\ \_____  \ \  \\\  \ \  \    \ \  \/  / / \ \  \_|/_\ \   _  _\  
  \ \  \\  \\ \  \_|\ \|____|\  \ \  \\\  \ \  \____\ \    / /   \ \  \_|\ \ \  \\  \| 
   \ \__\\ _\\ \_______\____\_\  \ \_______\ \_______\ \__/ /     \ \_______\ \__\\ _\ 
    \|__|\|__|\|_______|\_________\|_______|\|_______|\|__|/       \|_______|\|__|\|__|
                       \|_________|                                                    
                                                                                       
                                                                                       

""" 
start = "<td>"#div.class for our "hostname"
end = "</td>"#^                                       
class Color:
    Red = '\u001b[31;1m'
    Green = '\u001b[32;1m'
    Yellow = '\u001b[33;1m'
    Blue = '\u001b[34;1m'
    Magenta = '\u001b[35;1m'
    Cyan = '\u001b[36;1m'
    Bright_White = '\u001b[37;1m'
    
colored_logo = str(Color.Red + logo)    
def do():
    print('   Api To psnresolver.org By Chad Groom\n')
    print(colored_logo)
    name=input(Color.Green+"Enter Gamertag: ")
    try:
        s = requests.get("https://psnresolver.org/resolve/"+name)
    except Exception as Error:
        print( "\n\nCheck Your Connection!! ")
        oops=open("psn_res_error_log.txt", "+w")
        oops.write(str(Error))
        oops.close()
        lookup()
    html_str = s.text
    ip=str((html_str.split(start))[1].split(end)[0])
    re=requests.get('https://json.geoiplookup.io/' + ip)
    if re.status_code > 299:
        print(Color.Red + "[ERROR] - " + Color.Yellow+"Failed To Connect To geoiplookup.org\n\n"+Color.Green+"We Got Host Address: ["+ ip+"] ")
    data=re.json()
    re_ip = data['ip']
    re_isp = data['isp']
    re_org = data['org']
    re_hostname = data['hostname']
    re_city = data['city']
    re_country = data['country_name']
    re_asn = data['asn']
    re_integ = data['success']
    re_is_cached = data['cached']
    re_curr = data['currency_code']
    if re_integ == True:
        integ_char = 'Success'
    elif re_is_cached == False:
        integ_char = 'Failed/ Errors :( '
    if re_integ == True:
        cache_char = 'True'
    elif re_is_cached == False:
        cache_char = 'False'
        
    print("""
RESULTS:

_______________________________________________________________________________________________________

IP: """ + Color.Green + re_ip + """

ISP: """ + Color.Cyan + re_isp + """

ORG: """ + Color.Red + re_org + """

HOSTNAME: """ + Color.Magenta + re_hostname + """

CITY: """ + Color.Blue + re_city + """

COUNTRY: """ + Color.Green + re_country + """

ASN: """ + Color.Cyan + re_asn + """

INTEGRITY: """ + Color.Blue + integ_char + """

IS CACHED: """ + Color.Red + cache_char + """

CURRENCY: """ + Color.Green + re_curr + """
_______________________________________________________________________________________________________

""")
    ex=input(Color.Bright_White + '\nHit [ENTER] To Restart Or CTRL + C To Exit\n')
    do()

do()    
