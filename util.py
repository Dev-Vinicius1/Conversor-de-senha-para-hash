import os, hashlib

def menuPrincipal():
    print("_"*60)
    print("\n\t                 CONVERSOR HASH")
    print("_"*60)
    print("1 - Verificar hash de arquivo.\n2 - Converter texto para hash.")
    print("_"*60)

def menuGerarSenha():
    print("_"*60)
    print("\n\t        CONVERSOR DE TEXTO EM HASH")
    print("_"*60)
    print("\n1-> MD5.\n2-> SHA-1.\n3-> SHA-256.\n4-> SHA-512.\n5-> Sair")
    print("_"*60)

def limparTela(): 
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# criar um interface que permita buscar um arquivo no sistema;
# após isso tirar a hash desse arquivo;
    

def arquivoHash(file_path):
    hashMD5 = hashlib.md5()
    hashSHA1 = hashlib.sha1()

    with open(file_path, 'rb') as file:
        buffer = file.read(65536)
        while len(buffer) > 0:
            hash.update(buffer)
            buffer = file.read(65536)
    
    return hash.hexdigest()

def hashFromFile():
    arquivo = input("Informe o caminho do arquivo que deseja gerar a hash: ")

    if os.path.exists(arquivo):
        arquivo_hash = arquivo_hash(arquivo)
        print(f"Hash do arquivo em MD5: {arquivo_hash}")
        print(f"Hash do arquivo em SHA1: {arquivo_hash}")
    
    else:
        print("Arquivo não encontrado.\nCertifique-se que o caminho está correto!")
