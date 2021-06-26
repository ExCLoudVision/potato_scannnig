import dns.resolver
from colorama import Fore, Back, Style
import requests, socket, sys
dnsTypes = ["A","AAAA","PTR","NS","MX","SOA", "CNAME","TXT"]
url = sys.argv[1]
portNeededToBeScan = [21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
headersHeaderList = ["X-XSS-Protection","X-Frame-Options","X-Content-Type-Options","Strict-Transport-Security","Referrer-Policy","Feature-Policy","Content-Security-Policy"]
for x in range(100):
    print("\n")
def ligne():
    print("_:-:_"*20)
def Information(text):
    buf = Fore.WHITE + " ["
    buf += Fore.CYAN + " ! "
    buf += Fore.WHITE + "]"
    buf +=  " - "
    buf += Fore.WHITE + text
    print(buf)
    print(Fore.RESET)

banner = """
                                           ▓▓            
                                      ████            
                                    ██  ██      ██    
                                    ██    ████████      
                                  ██            ██      
                              ██          ██      
                   ██████      ██        ████████
                 ████████▒▒██████    ██          ██  
              ████▒▒▒▒▒▒▒▒▒▒▒▒▒▒████  ██      ██    
           ████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  ██  ██      
           ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒██  ██        
           ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒██            
         ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒██          
    ██████████▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██          
  ██▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒████        
██▒▒▒▒▒▒████▒▒▒▒▒▒▒▒██▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒██      
██▒▒████  ██▒▒▒▒▒▒▒▒████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒██    
████    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  ██▒▒██    
    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██    ██▒▒██    
    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████      ██▒▒██    
         ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████          ████      
         ██████▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██                      
       ██▒▒▒▒▒▒████████████▒▒▒▒▒▒▒▒██                    
       ██▒▒▒▒▒▒██          ██▒▒▒▒▒▒██                    
       ████████            ██▒▒▒▒▒▒██                    
                             ██████                      

"""
print(banner)
ligne()
print("Web Directory Scanner | port scannner | dns scanner |")
ligne()
try:
    with open("potato.wordlist","r") as f:
        wordlist = f.read().split("\n")
    f.close()
    wordListPlace = {}
    x = 0
    for d in wordlist:
        wordListPlace[d] = x
        x += 1
    Information("wordlist loaded")
except:
    print("worlist missing")
    exit()
openPort = []
def portScanner(ip):
    Information("port scanning")
    for x in portNeededToBeScan:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip,x))
        if result == 0:
            openPort.append(x)
ActiveDir = []
def DnsScanner(ip):
    print("*------------------*")
    for _type in dnsTypes:
        x = 0
        try:
            result = dns.resolver.query(ip, _type)
            for val in result:
                print(f"{_type} - {val.to_text()}")
                x += 1
        except:
            pass
        if(x > 0):
            print("\n")
    print("*------------------*")
def WebDirScan(url):
    stop = False
    try:
        urlopen = 0
        for ext in wordlist:
            if(stop != True):
                r = requests.get(f"{url}/{ext}")
                if r.status_code != 404:
                    urlopen += 1
                    ActiveDir.append(f"{url}/{ext}")
                    print(f"{url}/{ext} : {wordListPlace[ext]} / {len(wordlist)}")
    except:
        stop = True
def VerifySecurityOfSite(url):
    try:
        server = ""
        r = requests.get(url)
        for header in headersHeaderList:
            server = r.headers["Server"]
            try:
                res = req.headers[header]
            except:
                Information(f"{header} is missing")
        Information(f"{server}")
    except:
        pass
ip = url.replace("https://", "")
ip = ip.replace("http://","")
ip = ip.split("/")
ip = ip[0]
DnsScanner(ip)
portScanner(ip)
print("*------------------*")
lenn = len("*------------------*")
for port in openPort:
    print(f"\t- {port}")
print("*------------------*")
VerifySecurityOfSite(url)
print("*------------------*")
WebDirScan(url)

print('''
        

    good buy :)
   see you sooon


''')
