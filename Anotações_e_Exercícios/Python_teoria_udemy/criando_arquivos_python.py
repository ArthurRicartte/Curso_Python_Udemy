import os

# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho_arquivo = 'C:\\Users\\Starss\\Curso_Python\\'
caminho_arquivo += 'teste_arquivo.txt'
#arquivo = open(caminho_arquivo,'w')
#arquivo.close()
#print(caminho_arquivo)

with open(caminho_arquivo, '+w', encoding= 'utf-8') as arquivo:
   arquivo.write('Atenção \n')
   arquivo.write('Linha 1 \n')
   arquivo.write('Linha 2 \n')
   arquivo.writelines(('Linha 3 \n', 'Linha 4 \n'))
   print()

   arquivo.seek(0,0)
   print('Read')
   print(arquivo.read())
   print()

   arquivo.seek(0,0)
   print('Readline')
   print(arquivo.readline(), end='')   
   print(arquivo.readline(), end='')   
   print(arquivo.readline(), end='')   
   print(arquivo.readline().strip())   
   print(arquivo.readline().strip())   
   print()

   arquivo.seek(0,0)
   print('Readlines')

   for linha in arquivo.readlines():
      print(linha.strip())

#os.remove(caminho_arquivo) or os.unlink(caminho_arquivo)
#os.rename(caminho_arquivo, 'novo_nome_arquivo')
