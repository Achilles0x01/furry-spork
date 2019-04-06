#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Henrique Galdino RM 82723
# Iohan Pereira    RM 81869

import os
from config import banner as arte
from config.banner import cores 
from config.modulos import *

os.system('cls' if os== 'nt' else 'clear')  # Limpa a tela considerando o sistema operacional

registros = [] # Realiza o armazenamento das informações 
opcoes = 0 # op do menu

try: 

    while(opcoes <= 6):
        
        descricao = arte.banner()
        print(descricao)

        print('{amarelo}[1]{finale} - Modo de cadastro para adicionar um novo usuário.'.format(**cores))
        print('{amarelo}[2]{finale} - Modo de busca, procura um usuário a partir do apelido inserido.'.format(**cores))
        print('{amarelo}[3]{finale} - Exibir quantidade de usuários cadastrados.'.format(**cores))
        print('{amarelo}[4]{finale} - Modo de exclusão, capaz de excluir um usuário.'.format(**cores))
        print('{amarelo}[5]{finale} - Nível acesso no sistema'.format(**cores))
        print('{amarelo}[6]{finale} - Exibe apenas usuários com classificação administrativa.'.format(**cores))

        opcoes = (int(input('\nDigite uma das opções, de 1-6: ')))

        if( opcoes == 1 ):
            cadastrar(registros)
        
        elif (opcoes == 2 ):
            buscar(registros)

        elif (opcoes == 3):
            sudos(registros)

        elif (opcoes == 4):
            excluir(registros)

        elif (opcoes == 5):
            acesso(registros)

        elif (opcoes == 6):
            horaData(registros)

        else:
            print('Op invalida padawan')

except KeyboardInterrupt:
    print('\n{verde}{italic}Saindo do sistema{finale}'.format(**cores))
exit()
