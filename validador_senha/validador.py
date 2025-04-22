import math
import re
import requests
import hashlib

def calcular_entropia(senha):
    charset = 0
    if re.search(r"[a-z]", senha):
        charset += 26
    if re.search(r"[A-Z]", senha):
        charset += 26
    if re.search(r"[0-9]", senha):
        charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        charset += 32
    return round(len(senha) * math.log2(charset), 2)

def senha_forte(senha):
    return (
        len(senha) >= 12 and
        re.search(r"[a-z]", senha) and
        re.search(r"[A-Z]", senha) and
        re.search(r"[0-9]", senha) and
        re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha)
    )

def verificar_pwned(senha):
    sha1 = hashlib.sha1(senha.encode("utf-8")).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    res = requests.get(url)
    hashes = (line.split(":") for line in res.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0
