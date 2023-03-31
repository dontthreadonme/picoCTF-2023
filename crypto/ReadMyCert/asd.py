from base64 import b64decode

with open("readmycert.csr", "r") as f:
    cert = "".join(f.readlines()).split("-----")[2].strip()
    print(b64decode(cert).decode("unicode_escape"))
