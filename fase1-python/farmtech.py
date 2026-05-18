import os # Importa o módulo os para manipulação de arquivos e diretórios

# Cadastro de culturas, áreas e insumos

culturas = []
areas = []
insumos = []

# Entrada de dados para culturas

while True:

    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n=== FARMTECH SOLUTIONS ===")
    print("1. Cadastrar Cultura")
    print("2. Mostrar dados cadastrados")
    print("3. Atualizar")
    print("4. Deletar")
    print("5. Sair")

    escolha = input("Escolha uma opção: ") 

    if escolha == '1':
        cultura = input("Digite o nome da cultura [Café] ou [Cana-de-açucar]: ")
        if cultura == "Café":
            base = int(input("Digite o valor da base(em metros) da área de plantio: "))                    # Para a área de café, foi escolhido a forma geométrica do retângulo area = base * altura
            altura = int(input("Digite o valor da altura(em metros) da área de plantio: "))
            area_ret = base * altura
            areas.append(area_ret)

            ruas = int(input("Digite a quantidade de ruas da lavoura: "))
            litros = (ruas * 500) / 1000
            insumos.append(litros)
            print(f"Quantidade necessária de fosfato: {litros} L") 

            print(f"\nO valor da área de plantio é: {area_ret} m²")
            print(f"\nInsumos necessários: {litros} L")

        elif cultura == "Cana-de-açucar":
            raio = int(input("Digite o valor do raio da área de plantio: "))                  # Para a área de plantio da Cana-de-açucar, foi escolhido a forma geométrica do Circulo area = 3.14 * (raio ** 2) 
            area_cir = 3.14 * (raio ** 2) 
            areas.append(area_cir) 

            ruas = int(input("Digite a quantidade de ruas da lavoura: "))
            litros = (ruas * 800) / 1000
            insumos.append(litros)
            print(f"Quantidade necessária de herbicida: {litros} L")

            print(f"\nO valor da área de plantio é: {area_cir} m²")
            print(f"\nInsumos necessários: {litros} L")

        

        else:
            print("Digite um valor válido!")
            continue    

        culturas.append(cultura)
        print(f"\nCultura '{cultura}' cadastrada com sucesso!")

        input("\nPressione ENTER para continuar...")
        
    
    elif escolha == '2':

        if len(culturas) == 0:
            print("Nenhum dado cadastrado.")

        else:
            for i in range(len(culturas)):
                print(f"\nÍndice: {i}")
                print(f"Cultura: {culturas[i]}")
                print(f"Área: {areas[i]}")
                print(f"Insumos necessários: {insumos[i]} L")

        input("\nPressione ENTER para continuar...")

    elif escolha == '3':

        indice = int(input("Digite o índice que deseja atualizar: "))

        if indice >= 0 and indice < len(culturas):

            nova_cultura = input("Digite a nova cultura: ")
            culturas[indice] = nova_cultura

            print("Cultura atualizada com sucesso!")

        else:
            print("Índice inválido!")

        input("\nPressione ENTER para continuar...")

    elif escolha == '4':

        indice = int(input("Digite o índice que deseja deletar: "))

        if indice >= 0 and indice < len(culturas):

            del culturas[indice]
            del areas[indice]
            del insumos[indice]

            print("Cadastro deletado com sucesso!")

        else:
            print("Índice inválido!")

        input("\nPressione ENTER para continuar...")

    elif escolha == '5':
        print("Obrigado por acessar a FarmTech Solutions! \nSaindo...")
        break

    else:
        print("Opção inválida!")
