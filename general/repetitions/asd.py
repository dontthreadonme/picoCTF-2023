from base64 import b64decode

f = open("enc_flag", "r").read().replace("\n", "")
print(f)

while True:
    try:
        f = b64decode(f)
        print(f)
    except Exception:
        break
