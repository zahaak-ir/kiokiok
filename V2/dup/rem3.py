import os

files_to_remove = ['VmessL.txt', 'VlessL.txt', 'TuicL.txt', 'TrojanL.txt', 'SsrL.txt', 'SsL.txt', 'socksF.txt', 'mtprotoF.txt', 'juicityL.txt', 'HysteriaL.txt', 'Hy2L.txt']

for file in files_to_remove:
    if os.path.exists(file):
        os.remove(file)
    else:
        print(f"File '{file}' does not exist, skipping removal.")
