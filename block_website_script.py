import os

# Run this script as admin!
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect_ip = "127.0.0.1"
block_list = [
    "x.com",
    "www.x.com",
    "twitter.com",
    "www.twitter.com",
    "mobile.twitter.com",
    "deviantart.com",
    "www.deviantart.com",
    "kemono.su",
    "www.kemono.su",
    "newgrounds.com",
    "www.newgrounds.com",
    "rule34.xxx"
]



def block_websites():
    with open(hosts_path, 'r+') as file:
        content = file.read()
        for site in block_list:
            entry = f"{redirect_ip} {site}"
            if entry not in content:
                file.write(f"\n{entry}")
    print("Websites blocked successfully.")


# Run block function 
block_websites()
