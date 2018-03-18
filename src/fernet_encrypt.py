from cryptography.fernet import Fernet

key = Fernet.generate_key();
f = Fernet(key);
token= f.encrypt(b"hello")
print(token +"  token")
print(f.decrypt(token))
