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


def adicionar(tarefa, lista_tarefas):
    print()
    if not tarefa.strip():
        print('Nada para adiconar.')
        print()
        return
    
    lista_tarefas.append(tarefa)
    print(f'{tarefa=} adicionada ã lista.')
    print()    
    

tarefas = []
tarefas_refazer = []
while True:
    print('Comandos: listar, desfazer, refazer, ejetar')
    tarefa = input('Qual tarefa você deseja fazer?')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    
    elif tarefa == 'clear':
        os.system('cls')#comando para limpar o terminal!
        continue
    
    elif tarefa == 'ejetar':
        break
    
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue


with open('Lista_de_tarefas', 'w', encoding='utf8') as arquivo:
    json.dumps(arquivo, tarefas, ensure_ascii=False, indent=2)

print('vapo ^3^')
 