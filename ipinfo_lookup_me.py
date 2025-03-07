import subprocess
import re
import requests

keepdoing = True

while keepdoing:
    lines = subprocess.check_output(args=['netstat','-an'],text=True)
    pattern = r"^\d{1,3}(?:\.\d{1,3}){3}(?=:\d+)?"
    x = lines.split('\n')
    ip_list = set()

    for i in x:
        tokens = i.split(" ")
        filtered_tokens  = []
        for token in tokens:
            if token != '':
                filtered_tokens.append(token)
        if len(filtered_tokens) == 4:
            match = re.match(pattern,filtered_tokens[2])
            if match:
                if(match.group(0) != '0.0.0.0' and match.group(0) != '127.0.0.1'):
                    ip_list.add(match.group(0))


    for ip in ip_list:
        url = f"https://ipinfo.io/{ip}/json"
        try:
            response = requests.get(url)
            data = response.json()
            print(f"{ip}"+" "*(20-len(ip))+"->   "+data.get('org', 'Unknown')+ " "*4 + data.get('country', 'Unknown'))
        except:
            print(f"{ip}"+" "*(20-len(ip))+"->   " + 'Unknown'+ " "*4 + 'Unknown')
    
    input_var = input("Do you want to continue? (y/n): ")
    if input_var.lower() == 'n':
        keepdoing = False
    elif input_var.lower() == 'y':
        keepdoing = True
    else:
        print("Invalid input. Exiting...")
        keepdoing = False
        break
