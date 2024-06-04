# Lista de registros de resíduos
residuos = []

def adicionar_residuo():
    tipo = input("Digite o tipo de resíduo: ").strip()
    quantidade = int(input("Digite a quantidade coletada: ").strip())
    localizacao = input("Digite a localização onde foi encontrado: ").strip()
    registro = {'tipo': tipo, 'quantidade': quantidade, 'localizacao': localizacao}
    residuos.append(registro)
    print("Resíduo adicionado com sucesso!")

def exibir_residuos():
    if not residuos:
        print("Nenhum resíduo registrado.")
        return
    for idx, residuo in enumerate(residuos, start=1):
        print(f"{idx}. Tipo: {residuo['tipo']}, Quantidade: {residuo['quantidade']}, Localização: {residuo['localizacao']}")

def buscar_residuo_por_tipo():
    tipo_busca = input("Digite o tipo de resíduo que deseja buscar: ").strip()
    encontrados = [residuo for residuo in residuos if residuo['tipo'].lower() == tipo_busca.lower()]
    if not encontrados:
        print("Nenhum resíduo encontrado desse tipo.")
        return
    for idx, residuo in enumerate(encontrados, start=1):
        print(f"{idx}. Tipo: {residuo['tipo']}, Quantidade: {residuo['quantidade']}, Localização: {residuo['localizacao']}")

def calcular_estatisticas():
    total_residuos = len(residuos)
    if total_residuos == 0:
        print("Nenhum resíduo registrado para calcular estatísticas.")
        return
    
    total_quantidade = sum(residuo['quantidade'] for residuo in residuos)
    tipos_residuos = set(residuo['tipo'] for residuo in residuos)
    
    print(f"Total de registros de resíduos: {total_residuos}")
    print(f"Quantidade total de resíduos coletados: {total_quantidade}")
    print(f"Tipos de resíduos coletados: {', '.join(tipos_residuos)}")

def menu():
    while True:
        print("\nMenu de Opções:")
        print("1. Adicionar resíduo")
        print("2. Exibir todos os resíduos")
        print("3. Buscar resíduo por tipo")
        print("4. Calcular estatísticas")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == '1':
            adicionar_residuo()
        elif escolha == '2':
            exibir_residuos()
        elif escolha == '3':
            buscar_residuo_por_tipo()
        elif escolha == '4':
            calcular_estatisticas()
        elif escolha == '5':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
menu()



#Esse programa cria um sistema básico de gerenciamento de resíduos coletados do oceano, onde a empresa pode:

#Adicionar novos registros de resíduos.
#Exibir todos os registros.
#Buscar resíduos por tipo.
#Calcular estatísticas básicas dos resíduos registrados.