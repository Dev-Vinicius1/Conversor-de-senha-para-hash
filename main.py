import util
import hash

util.limparTela()
util.menuPrincipal()

try:
    opcao = int(input("Escolha uma opção: "))
    print("_"*60)

    if opcao == 1:
        pass

    elif opcao == 2:
        util.limparTela()
        util.menuGerarSenha()
        opcao = int(input("Escolha uma opção: "))
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
        
