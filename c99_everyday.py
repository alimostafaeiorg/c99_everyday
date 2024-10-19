import requests
from bs4 import BeautifulSoup


url = 'https://subdomainfinder.c99.nl/scans/2024-10-12/dell.com'
filename = 'subdomains.txt'


GREEN = '\033[92m'  
RESET = '\033[0m'   

def fetch_subdomains():
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        subdomain_elements = soup.select('.sd')   
        return {element.text.strip() for element in subdomain_elements}  
    else:
        print(f"Error on Receive Data: {response.status_code}")
        return set()

def load_previous_subdomains():
    try:
        with open(filename, 'r') as file:
            return set(file.read().splitlines())  
    except FileNotFoundError:
        return set() 
      
def save_subdomains(subdomains):
    with open(filename, 'a') as file:  
        for subdomain in subdomains:
            file.write(f"{subdomain}\n")


previous_subdomains = load_previous_subdomains()  
current_subdomains = fetch_subdomains()  


new_subdomains = current_subdomains - previous_subdomains

if new_subdomains:
    print(GREEN + "New Subdomains:" + RESET)   
    for subdomain in new_subdomains:
        print(subdomain)

  save_subdomains(new_subdomains)
else:
    print(GREEN + " new subdomains Not found." + RESET)  


print(GREEN + "Create By Alimostafaeiorg" + RESET)  

