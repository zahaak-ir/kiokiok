import requests

with open("V2/fromsite/sites.txt") as f:
    sites = f.read().splitlines()

line_count = 0
file_count = 1
output_file = f"V2/temp/fromsite_{file_count}.txt"

with open(output_file, "w") as f:
    for site in sites:
        try:
            html = requests.get(site).content.decode("utf-8")
            lines = html.split("\n")
            servers = [line for line in lines if line.startswith("ss://") or line.startswith("ssr://") or line.startswith("vmess://") or line.startswith("vless://") or line.startswith("trojan://") or line.startswith("hy2://") or line.startswith("tuic://") or line.startswith("hysteria://")]

            for server in servers:
                f.write(server + "\n")
                line_count += 1

                # Check if we have reached 2000 lines
                if line_count >= 2000:
                    f.close()  # Close the current file
                    file_count += 1  # Increment the file count
                    output_file = f"V2/temp/fromsite_{file_count}.txt"  # Create a new file name
                    f = open(output_file, "w")  # Open a new file for writing
                    line_count = 0  # Reset line count for the new file

        except Exception as e:
            print(f"An error occurred while fetching content from {site}: {e}")
            continue  # Skip to the next site if there's an error

# Close the last file if it's still open
if line_count > 0:
    f.close()
