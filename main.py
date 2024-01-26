import util as limparTela
import hash

limparTela
print("_"*60)
print("\n\t         CONVERSOR DE SENHA EM HASH")
print("_"*60)
print("\n1-> MD5.\n2-> SHA-1.\n3-> SHA-256.\n4-> SHA-512.\n5-> Sair")
print("_"*60)

try:
    opcao = int(input("Escolha uma opção: "))
    print("_"*60)

    if opcao == 1:
        hash.hashmd5()
        input("Presiona qualquer tecla para sair do programa.")
    
    elif opcao == 2:
        hash.hashsha1()
        input("Presiona qualquer tecla para sair do programa.")   
    elif opcao == 3:
        hash.hashsha256()
        input("Presiona qualquer tecla para sair do programa.")    
    elif opcao == 4:
        hash.hash512()
        input("Presiona qualquer tecla para sair do programa.")    
    elif opcao == 5:
        print("saindo do programa.")
    
    else:
        print("Opção incorreta, tente novamente!")

except ValueError:
    print("Essa opção não existe, tente novamente!")

except KeyboardInterrupt:
    print("\n\nEscolheu sair do programa.")
        
