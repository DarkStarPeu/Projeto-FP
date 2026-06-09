import os
from datetime import datetime

# Arquivos onde os dados serão salvos
ARQUIVO_TREINOS = "treinos.txt"
ARQUIVO_EXERCICIOS = "exercicios.txt"
ARQUIVO_METAS = "metas.txt"
ARQUIVO_EVOLUCAO = "evolucao.txt"


# -------------------------------
# Funções gerais
# -------------------------------

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPressione ENTER para continuar...")


def ler_opcao():
    try:
        return int(input("Escolha uma opção: "))
    except ValueError:
        return -1


def gerar_id(lista):
    if len(lista) == 0:
        return 1

    maior_id = 0

    for item in lista:
        if item["id"] > maior_id:
            maior_id = item["id"]

    return maior_id + 1


# -------------------------------
# Carregar dados dos arquivos
# -------------------------------

def carregar_treinos():
    treinos = []

    try:
        arquivo = open(ARQUIVO_TREINOS, "r", encoding="utf-8")

        for linha in arquivo:
            dados = linha.strip().split("|")

            if len(dados) == 6:
                treino = {
                    "id": int(dados[0]),
                    "nome": dados[1],
                    "tipo": dados[2],
                    "data": dados[3],
                    "duracao": dados[4],
                    "objetivo": dados[5]
                }

                treinos.append(treino)

        arquivo.close()

    except FileNotFoundError:
        pass

    return treinos


def carregar_exercicios():
    exercicios = []

    try:
        arquivo = open(ARQUIVO_EXERCICIOS, "r", encoding="utf-8")

        for linha in arquivo:
            dados = linha.strip().split("|")

            if len(dados) == 6:
                exercicio = {
                    "id": int(dados[0]),
                    "id_treino": int(dados[1]),
                    "nome": dados[2],
                    "series": dados[3],
                    "repeticoes": dados[4],
                    "observacao": dados[5]
                }

                exercicios.append(exercicio)

        arquivo.close()

    except FileNotFoundError:
        pass

    return exercicios


def carregar_metas():
    metas = []

    try:
        arquivo = open(ARQUIVO_METAS, "r", encoding="utf-8")

        for linha in arquivo:
            dados = linha.strip().split("|")

            if len(dados) == 5:
                meta = {
                    "id": int(dados[0]),
                    "descricao": dados[1],
                    "tipo": dados[2],
                    "prazo": dados[3],
                    "status": dados[4]
                }

                metas.append(meta)

        arquivo.close()

    except FileNotFoundError:
        pass

    return metas

def carregar_metas_concluidas():
    try:
        arquivo = open(ARQUIVO_EVOLUCAO, "r", encoding="utf-8")
        conteudo = arquivo.read().strip()
        arquivo.close()
        
        if conteudo == "":
            return 0
        return int(conteudo)
    except (FileNotFoundError, ValueError):

        return 0

def somar_metas_concluida():
    metas_concluidas = carregar_metas_concluidas()
    metas_concluidas += 1

    arquivo = open(ARQUIVO_EVOLUCAO, "w", encoding="utf-8")
    arquivo.write(str(metas_concluidas))
    arquivo.close()

# -------------------------------
# Salvar dados nos arquivos
# -------------------------------

def salvar_treinos(treinos):
    arquivo = open(ARQUIVO_TREINOS, "w", encoding="utf-8")

    for treino in treinos:
        linha = f'{treino["id"]}|{treino["nome"]}|{treino["tipo"]}|{treino["data"]}|{treino["duracao"]}|{treino["objetivo"]}\n'
        arquivo.write(linha)

    arquivo.close()


def salvar_exercicios(exercicios):
    arquivo = open(ARQUIVO_EXERCICIOS, "w", encoding="utf-8")

    for exercicio in exercicios:
        linha = f'{exercicio["id"]}|{exercicio["id_treino"]}|{exercicio["nome"]}|{exercicio["series"]}|{exercicio["repeticoes"]}|{exercicio["observacao"]}\n'
        arquivo.write(linha)

    arquivo.close()


def salvar_metas(metas):
    arquivo = open(ARQUIVO_METAS, "w", encoding="utf-8")

    for meta in metas:
        linha = f'{meta["id"]}|{meta["descricao"]}|{meta["tipo"]}|{meta["prazo"]}|{meta["status"]}\n'
        arquivo.write(linha)

    arquivo.close()


# -------------------------------
# Funções dos treinos
# -------------------------------

def cadastrar_treino(treinos):
    limpar_tela()
    print("=== CADASTRAR PLANO DE TREINO ===")

    nome = input("Nome do treino: ")
    tipo = input("Tipo do treino (musculação, cardio, funcional, corrida): ")
    data = input("Data do treino (dd/mm/aaaa): ")
    duracao = input("Duração do treino: ")
    objetivo = input("Objetivo do treino: ")

    treino = {
        "id": gerar_id(treinos),
        "nome": nome,
        "tipo": tipo,
        "data": data,
        "duracao": duracao,
        "objetivo": objetivo
    }

    treinos.append(treino)
    salvar_treinos(treinos)

    print("\nTreino cadastrado com sucesso!")


def listar_treinos(treinos):
    limpar_tela()
    print("=== PLANOS DE TREINO ===")

    if len(treinos) == 0:
        print("Nenhum treino cadastrado.")
        return

    for treino in treinos:
        print(f'\nID: {treino["id"]}')
        print(f'Nome: {treino["nome"]}')
        print(f'Tipo: {treino["tipo"]}')
        print(f'Data: {treino["data"]}')
        print(f'Duração: {treino["duracao"]}')
        print(f'Objetivo: {treino["objetivo"]}')


def buscar_treino_por_id(treinos, id_treino):
    for treino in treinos:
        if treino["id"] == id_treino:
            return treino

    return None


def editar_treino(treinos):
    limpar_tela()
    print("=== EDITAR TREINO ===")

    listar_treinos(treinos)

    try:
        id_treino = int(input("\nDigite o ID do treino que deseja editar: "))
        treino = buscar_treino_por_id(treinos, id_treino)

        if treino is None:
            print("\nTreino não encontrado.")
            return

        print("\nDeixe em branco caso não queira alterar o campo.")

        novo_nome = input("Novo nome: ")
        novo_tipo = input("Novo tipo: ")
        nova_data = input("Nova data: ")
        nova_duracao = input("Nova duração: ")
        novo_objetivo = input("Novo objetivo: ")

        if novo_nome != "":
            treino["nome"] = novo_nome

        if novo_tipo != "":
            treino["tipo"] = novo_tipo

        if nova_data != "":
            treino["data"] = nova_data

        if nova_duracao != "":
            treino["duracao"] = nova_duracao

        if novo_objetivo != "":
            treino["objetivo"] = novo_objetivo

        salvar_treinos(treinos)

        print("\nTreino editado com sucesso!")

    except ValueError:
        print("\nID inválido.")


def excluir_treino(treinos, exercicios):
    limpar_tela()
    print("=== EXCLUIR TREINO ===")

    listar_treinos(treinos)

    try:
        id_treino = int(input("\nDigite o ID do treino que deseja excluir: "))
        treino = buscar_treino_por_id(treinos, id_treino)

        if treino is None:
            print("\nTreino não encontrado.")
            return

        confirmacao = input("Tem certeza que deseja excluir esse treino? (s/n): ")

        if confirmacao.lower() == "s":
            treinos.remove(treino)

            # Também remove os exercícios ligados a esse treino
            exercicios[:] = [ex for ex in exercicios if ex["id_treino"] != id_treino]

            salvar_treinos(treinos)
            salvar_exercicios(exercicios)

            print("\nTreino excluído com sucesso!")
        else:
            print("\nExclusão cancelada.")

    except ValueError:
        print("\nID inválido.")


# -------------------------------
# Funções dos exercícios
# -------------------------------

def cadastrar_exercicio(treinos, exercicios):
    limpar_tela()
    print("=== CADASTRAR EXERCÍCIO ===")

    if len(treinos) == 0:
        print("Cadastre um treino antes de adicionar exercícios.")
        return

    listar_treinos(treinos)

    try:
        id_treino = int(input("\nDigite o ID do treino para adicionar o exercício: "))
        treino = buscar_treino_por_id(treinos, id_treino)

        if treino is None:
            print("\nTreino não encontrado.")
            return

        nome = input("Nome do exercício(ex: agachamento, supino, corida, abdominal, flexão): ")
        series = input("Quantidade de séries: ")
        repeticoes = input("Repetições: ")
        observacao = input("Tempo, distância ou observação: ")

        exercicio = {
            "id": gerar_id(exercicios),
            "id_treino": id_treino,
            "nome": nome,
            "series": series,
            "repeticoes": repeticoes,
            "observacao": observacao
        }

        exercicios.append(exercicio)
        salvar_exercicios(exercicios)

        print("\nExercício cadastrado com sucesso!")

    except ValueError:
        print("\nID inválido.")


def listar_exercicios_por_treino(treinos, exercicios):
    limpar_tela()
    print("=== EXERCÍCIOS POR TREINO ===")

    if len(treinos) == 0:
        print("Nenhum treino cadastrado.")
        return

    listar_treinos(treinos)

    try:
        id_treino = int(input("\nDigite o ID do treino: "))
        treino = buscar_treino_por_id(treinos, id_treino)

        if treino is None:
            print("\nTreino não encontrado.")
            return

        print(f'\nExercícios do treino: {treino["nome"]}')

        encontrou = False

        for exercicio in exercicios:
            if exercicio["id_treino"] == id_treino:
                encontrou = True
                print(f'\nID: {exercicio["id"]}')
                print(f'Nome: {exercicio["nome"]}')
                print(f'Séries: {exercicio["series"]}')
                print(f'Repetições: {exercicio["repeticoes"]}')
                print(f'Observação: {exercicio["observacao"]}')

        if not encontrou:
            print("Nenhum exercício cadastrado para esse treino.")

    except ValueError:
        print("\nID inválido.")


# -------------------------------
# Funções das metas
# -------------------------------

def cadastrar_meta(metas):
    limpar_tela()
    print("=== CADASTRAR META ===")

    descricao = input("Descrição da meta: ")
    tipo = input("Tipo da meta (perder peso, ganhar massa, condicionamento, treinar mais vezes): ")
    prazo = input("Prazo da meta (dd/mm/aaaa): ")

    meta = {
        "id": gerar_id(metas),
        "descricao": descricao,
        "tipo": tipo,
        "prazo": prazo,
        "status": "Em andamento"
    }

    metas.append(meta)
    salvar_metas(metas)

    print("\nMeta cadastrada com sucesso!")


def listar_metas(metas):
    limpar_tela()
    print("=== METAS CADASTRADAS ===")

    if len(metas) == 0:
        print("Nenhuma meta cadastrada.")
        return

    for meta in metas:
        print(f'\nID: {meta["id"]}')
        print(f'Descrição: {meta["descricao"]}')
        print(f'Tipo: {meta["tipo"]}')
        print(f'Prazo: {meta["prazo"]}')
        print(f'Status: {meta["status"]}')


def concluir_meta(metas):
    limpar_tela()
    print("=== CONCLUIR META ===")

    listar_metas(metas)

    try:
        id_meta = int(input("\nDigite o ID da meta que deseja concluir: "))

        for meta in metas:
            if meta["id"] == id_meta:
                if meta["status"] == "Concluída":
                    print("\nEsta meta já foi concluída anteriormente!")
                    return
                meta["status"] = "Concluída"
                salvar_metas(metas)
                somar_metas_concluida()
                print("\nMeta marcada como concluída!")
                return

        print("\nMeta não encontrada.")

    except ValueError:
        print("\nID inválido.")


# -------------------------------
# Menus
# -------------------------------

def menu_treinos(treinos, exercicios):
    while True:
        limpar_tela()
        print("=== MENU DE TREINOS ===")
        print("1 - Cadastrar treino")
        print("2 - Listar treinos")
        print("3 - Editar treino")
        print("4 - Excluir treino")
        print("0 - Voltar")

        opcao = ler_opcao()

        if opcao == 1:
            cadastrar_treino(treinos)
            pausar()
        elif opcao == 2:
            listar_treinos(treinos)
            pausar()
        elif opcao == 3:
            editar_treino(treinos)
            pausar()
        elif opcao == 4:
            excluir_treino(treinos, exercicios)
            pausar()
        elif opcao == 0:
            break
        else:
            print("\nOpção inválida.")
            pausar()


def menu_exercicios(treinos, exercicios):
    while True:
        limpar_tela()
        print("=== MENU DE EXERCÍCIOS ===")
        print("1 - Cadastrar exercício em um treino")
        print("2 - Listar exercícios de um treino")
        print("0 - Voltar")

        opcao = ler_opcao()

        if opcao == 1:
            cadastrar_exercicio(treinos, exercicios)
            pausar()
        elif opcao == 2:
            listar_exercicios_por_treino(treinos, exercicios)
            pausar()
        elif opcao == 0:
            break
        else:
            print("\nOpção inválida.")
            pausar()


def menu_metas(metas):
    while True:
        limpar_tela()
        print("=== MENU DE METAS ===")
        print("1 - Cadastrar meta")
        print("2 - Listar metas")
        print("3 - Marcar meta como concluída")
        print("0 - Voltar")

        opcao = ler_opcao()

        if opcao == 1:
            cadastrar_meta(metas)
            pausar()
        elif opcao == 2:
            listar_metas(metas)
            pausar()
        elif opcao == 3:
            concluir_meta(metas)
            pausar()
        elif opcao == 0:
            break
        else:
            print("\nOpção inválida.")
            pausar()

def menu_evolucao(treinos, metas):
    limpar_tela()
    print("=== MENU DE EVOLUÇÃO ===")


    print(f"Treinos cadastrados: {len(treinos)}")
    print(f"Metas cadastradas: {len(metas)}")
    print(f"Metas concluídas: {carregar_metas_concluidas()}")


    pausar()


# -------------------------------
# Programa principal
# -------------------------------

def main():
    treinos = carregar_treinos()
    exercicios = carregar_exercicios()
    metas = carregar_metas()

    while True:
        limpar_tela()
        print("=================================")
        print("        FITPLANNER")
        print(" Sistema de Planejamento Fitness")
        print("=================================")
        print("1 - Planos de treino")
        print("2 - Exercícios")
        print("3 - Metas")
        print("4 - Evolução")
        print("0 - Sair")

        opcao = ler_opcao()

        if opcao == 1:
            menu_treinos(treinos, exercicios)
        elif opcao == 2:
            menu_exercicios(treinos, exercicios)
        elif opcao == 3:
            menu_metas(metas)
        elif opcao == 4:
            menu_evolucao(treinos, metas)
        elif opcao == 0:
            print("\nSaindo do FitPlanner...")
            break
        else:
            print("\nOpção inválida.")
            pausar()


main()