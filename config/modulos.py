# -*- coding: utf-8 -*-
from config.banner import cores
import os

def cadastrar(lista):    # Este def realiza o cadastro do usuário
    # os.system('cls' if os== 'nt' else 'clear')
    addUser = 'S'
    validacao = [] # Armazena os dados de cadastro

    while addUser == 'S':
        validador = False 
        while validador != True:
            
            apelido = input('\nDigite um apelido ou nome abreviado: ').upper()
            if apelido not in validacao:
                usuario=[
                input('Informe o nome completo: ').upper(),
                apelido,
                input('Informe o cargo do usuário: ').upper(),
                input('Nível de acesso, exemplo: Visitante, usuario, administrativo, tecnico, super-usuario:\n').upper(),
                input('Informe a data do último acesso, por exemplo: 06/05/2019\n').upper()
                ]

                print('{verde}\nCadastro realizado com sucesso.{finale}'.format(**cores))

                validacao.append(apelido)
                lista.append(usuario)

                validador = True # Caso esteja tudo ok, será validado as informações e o programa dará prosseguimento no seu fluxo
            else:
                print('{amarelo}\nO usuário já se encontra registrado, tente novamente.{finale}'.format(**cores)) # Caso o validador seja diferente de verdadeiro, será exibido essa mensagem

        addUser = input('\nDeseja continuar com outro cadastro (S)im? Para prosseguir aperte qualquer tecla: ').upper() 

def buscar(lista): # Sistema de busca
    # os.system('cls' if os== 'nt' else 'clear')
    procurar = input('Digite o apelido escolhido pelo usuário: ').upper()

    for registro in lista:
        if procurar == registro[1]:
            print('{amarelo}\nNome...: {finale}{}'.format(registro[0], **cores))
            print('{amarelo}Apelido: {finale}{}'.format(registro[1], **cores))
            print('{amarelo}Cargo..: {finale}{}'.format(registro[2], **cores))
        else:
            print('{amarelo}\n§ Usuário não encontrado §{finale}'.format(**cores))

def sudos(lista): # Exibi a quantidade de usuários no sistema
    # os.system('cls' if os== 'nt' else 'clear')
    inicio = 0

    for registro in lista:
        if registro[3] == registro[3]:
            print('\nO nível de acesso do usuário {} é {}.'.format(registro[0], registro[2]))
        inicio  = inicio + 1
    print('\nTotal de usuários: '+ str(inicio))


def excluir(lista): # Exclui um usuário do registro 
    # os.system('cls' if os== 'nt' else 'clear')
    procurar = input('\nInforme o apelido do usuário que deseja realizar a exclusão: ').upper()

    for registro in lista:
        if registro[1] == procurar:
            lista.remove(registro)
            print('{verde}Exclusão bem sucedida.{finale}'.format(**cores))
        else:
            print('{amarelo}\nUsuário não consta mais no sistema.{finale}'.format(**cores))
    #return "{verde}Exclusão bem sucedida.{finale}"

def acesso(lista): # Exibir os usuários a partir do nível cadastrado
    # os.system('cls' if os== 'nt' else 'clear')
    procurar = input('\nInforme o nível de acesso para encontrar usuários setados com o mesmo nível, exemplo: Visitante, usuario, administrativo, tecnico, super-usuario:\n').upper()
    
    for registro in lista:
        if procurar == registro[3]:
            print('{amarelo}\nNome.:{finale} {}'.format(registro[0], **cores))
            print('{amarelo}Cargo:{finale} {}'.format(registro[2], **cores))

def horaData(lista): # Exibi as informações de ultimo acesso 
    # os.system('cls' if os== 'nt' else 'clear')
    dta = []

    for registro in lista:
        if registro[4] not in dta:
            dta.append(registro[4])
    print('Datas disponiveis: {}'.format(str(dta)))

    procurar = input('\nInforma a data de registro: ')

    for registro in lista:
        if registro[4] == procurar:
            print('O usuário {} acessou o sistema nesta data'.format(registro[1]))

        else:
            print('{amarelo}Não foi encontrado nenhum outro registro{finale}'.format(**cores))
