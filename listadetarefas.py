tarefas = []

def mostrar_menu():
    print("\n--- Lista de Tarefas ---")
    print("A. Adicionar tarefa")
    print("B. Listar tarefas")
    print("C. Atualizar tarefa")
    print("D. Remover tarefa")
    print("E. Sair")
    opcao = input("Escolha uma opção: ").upper() #Aumenta o tamanho da letra
    return opcao #Retorna a opção para o "while" abaixo.

def adicionar_tarefa():
    descricao = input("Digite a descrição da tarefa: ") #Descrição da tarefa
    tarefa = {'descricao': descricao, 'concluida': False} #"Tarefa Pendente"
    tarefas.append(tarefa) #"Adiciona a nova tarefa à lista tarefas"
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    else:
        tarefas.sort(key=lambda x: x['descricao'].lower()) #Tarefas ordenadas pelo "Sort" e Diminui o tamanho da letra com "Lower"
        for i, tarefa in enumerate(tarefas, 1): #Percorre a lista, começando por 1
            letra = chr(64 + i)  # Converte o número para a letra correspondente
            status = "Concluída" if tarefa['concluida'] else "Pendente" #Define a tarefa como Concluida (Comunica com "Def atualizar tarefas")
            print(f"{letra}. {tarefa['descricao']} - {status}") #Mostra status da tarefa

def atualizar_tarefa():
    listar_tarefas()
    if len(tarefas) > 0:
        letra = input("Digite a letra da tarefa a atualizar: ").upper()
        indice = ord(letra) - 65
        if 0 <= indice < len(tarefas):
            descricao = input("Nova descrição (deixe em branco para não alterar): ")
            if descricao:
                tarefas[indice]['descricao'] = descricao
            concluida = input("Marcar como concluída? (s/n): ").lower()
            if concluida == 's':
                tarefas[indice]['concluida'] = True
            print("Tarefa atualizada com sucesso!")
        else:
            print("Letra inválida.")

def remover_tarefa():
    listar_tarefas()
    if len(tarefas) > 0:
        letra = input("Digite a letra da tarefa a remover: ").upper()
        indice = ord(letra) - 65
        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)
            print("Tarefa removida com sucesso!")
        else:
            print("Letra inválida.")

while True:
    opcao = mostrar_menu()
    if opcao == 'A':
        adicionar_tarefa()
    elif opcao == 'B':
        listar_tarefas()
    elif opcao == 'C':
        atualizar_tarefa()
    elif opcao == 'D':
        remover_tarefa()
    elif opcao == 'E':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")