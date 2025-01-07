import os
import requests

# URL of the proxy list
url = "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt"

# Create the temp directory if it doesn't exist
temp_dir = "Socks/temp"
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

# Get the content of the proxy list
response = requests.get(url)
proxy_list = response.text.strip().split("\n")

# Create raw.txt with the original proxy list
with open(os.path.join(temp_dir, "raw1.txt"), "w") as raw_file:
    raw_file.write("\n".join(proxy_list))

# Convert and save proxies in the specified format
socks_proxies = []
for proxy in proxy_list:
    ip, port = proxy.split(":")
    socks_proxy = f"tg://socks?server={ip}&port={port}"
    socks_proxies.append(socks_proxy)

# Save the socks proxies to socks.txt
with open(os.path.join(temp_dir, "socks1.txt"), "w") as socks_file:
    socks_file.write("\n".join(socks_proxies))