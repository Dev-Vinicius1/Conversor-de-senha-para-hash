from getpass import getpass
import hashlib

def hashmd5():
    senha = getpass("Insira sua senha: ")
    print("_"*60)
    print("Senha criptografada: "+hashlib.md5(senha.encode("utf-8")).hexdigest())
    print("_"*60)
    
def hashsha1():
    senha = getpass("Insira sua senha: ")
    print("_"*60)
    print("Senha criptografada: "+hashlib.sha1(senha.encode("utf-8")).hexdigest())
    print("_"*60)
    
def hashsha256():
    senha = getpass("Insira sua senha: ")
    print("_"*60)
    print("Senha criptografada: "+hashlib.sha256(senha.encode("utf-8")).hexdigest())
    print("_"*60)
    
def hash512():
    senha = getpass("Insira sua senha: ")
    print("_"*60)   
    print("Senha criptografada: "+hashlib.sha512(senha.encode("utf-8")).hexdigest())
    print("_"*60)
