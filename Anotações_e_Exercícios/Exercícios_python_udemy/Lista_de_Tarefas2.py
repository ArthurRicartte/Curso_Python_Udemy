import os
import json 

def listar(tarefas):
    print()
    if not tarefas:
        print('Nada para listar.')
        print()
        return #serve para caso não tenha nada em tarefas, parar a execução da função
    
    print('TAREFAS')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, lista_refazer):
    print()
    if not tarefas:
        print('Nada para desfazer')
        print()
        return
    
    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)#Esse listar ficava nas condcionais do while True agora fica aqui

def refazer(tarefas, lista_refazer):
    print()
    if not tarefas:
        print('Nada para refazer.')
        print()
        return
    tarefa = lista_refazer.pop()
    print(f'{tarefa=} adiconada novamente na lista.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)

def adicionar(tarefa, lista_tarefas):
    print()
    if not tarefa.strip():
        print('Nada para adiconar.')
        print()
        return
    
    lista_tarefas.append(tarefa)
    print(f'{tarefa=} adicionada ã lista.')
    print()    
    listar(tarefas)

def ler(tarefas, caminho_arquivo):
    dados = []
    
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    
    except FileNotFoundError:
        print('arquivo não encontrado.')
        salvar(tarefas, caminho_arquivo)
    
    return dados# serve para usar os dados lidos em outro momento no caso para salvar no arquivo json

def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, ensure_ascii=False, indent=2)
    return dados# serve para usar os dados lidos em outro momento no caso para salvar no arquivo json



CAMINHO_ARQUIVO = 'lista_de_tarefas2.json'
tarefas = ler([], CAMINHO_ARQUIVO)#exemplo do pq usar return dados
tarefas_refazer = []
while True:
    print('Comandos: listar, desfazer, refazer, ejetar')
    tarefa = input('Qual tarefa você deseja fazer?')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('cls'),
        'adicionar': lambda: adicionar(tarefa, tarefas)
         
        }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    #Caso não encontre nehuma tarefa digitada correspondente nos comandos a tarefa serã adicionar

    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)#exemplo do pq usar return dados


print('vapo ^3^')

#pra conferir
'''import json
import os


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados


CAMINHO_ARQUIVO = 'aula119.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)'''