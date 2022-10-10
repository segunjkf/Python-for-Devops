# from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

import pandas as pd


file_path = "Sample-Spreadsheet-1000-rows.csv"

#with open(file_path, newline='') as csv_file:
 #   new_reader = csv.reader(csv_file, delimiter=',')
  #  for _ in range(5):

       # print(next(new_reader))

#with open('Sample-Spreadsheet-1000-rows.csv') as f:
 #   print(f)
#df = pd.read_csv("Sample-Spreadsheet-1000-rows.csv", encoding='cp1252')

#print(df.describe())


#line = '127.0.0.1 - rj [13/AUG/2022:14:43:30] "GET HTTP/1.0" 200'

#segun = re.search(r'(?P<WP>\w+\.\w+\.\w+\.\w+\W+\)', line)
#print(segun)

#print(segun.group('WP'))

#r = r'\[(?P<Time>\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})\]'
'''
with open('text.txt', 'r') as new_file:
    with open('big-data.txt', 'w') as target_file:
        for line in new_file:
            target_file.write(line)


def line_reader(file_path):
    with open(file_path, 'r')as anotherone:
        for line in anotherone:
            yield line


print(line_reader("Sample-Spreadsheet-1000-rows.csv"))
'''
'''
secret = "This is the password or document text"

bsecret = secret.encode()

print(bsecret)

m = hashlib.md5()
m.update(bsecret)

print(m.digest())
'''
'''
key = Fernet.generate_key()

#print(key)

f = Fernet(b'8u0tewYtUt28dROq87gMcqzUXc8xij4FbS_FgHxlguc=')

message = b"secrets go here"

encrypt = f.encrypt(message)

print(f.decrypt(encrypt))
'''

private_key = rsa.generate_private_key(public_exponent=65537, key_size=4096, backend=default_backend())

print(private_key)

public_key = private_key.public_key()
print(public_key)

message = b'more thing that are going to be ecrypted'
