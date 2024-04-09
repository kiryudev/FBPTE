import requests, sys, os

vio = "\033[95m"
red = "\033[91m"
grn = "\033[92m"
ylw = "\033[93m"
gry = "\033[90m"
non = "\033[0m"

def clear():
    if 'linux' in sys.platform.lower():
        os.system('clear')
    elif 'win' in platform:
        os.system('cls')
    else:
        pass
        
def retrieve(token):
    try:
        dat = requests.get('https://graph.facebook.com/v18.0/me/accounts', headers={'Authorization': f'Bearer {token}'}).json()
        page_data = dat.get('data', [])        
        for page in page_data:
            print(f"{vio} ID: {non}{page['id']}\n{vio} Name: {non}{page['name']}\n{vio} Access Token: {non}{page['access_token']}\n")
    except Exception as e:
        print(f"{red} [!] Error occurred : {e} {non}")

def main():
    print(f"{gry} You can use my tool to obtain your account token \n{ylw} ·› https://github.com/kiryudev/FBT {non}\n")       
    token = input(f"{vio} [›] Account Token :{non} ")
    print("")
    retrieve(token)

clear()
main()
