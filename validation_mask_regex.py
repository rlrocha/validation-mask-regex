# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 13:00:07 2021

@author: Rafael Rocha
"""

import re


def name_check(string):
    
    pattern = "^[A-Z][a-z]+\s[A-Z][a-z]+$"
    if bool(re.match(pattern, string)):
        print('Nome válido.')
    else:
        print('Nome inválido!')
    
    return None

def email_check(string):
    
    pattern = "^[a-z]+@[a-z]+.br$"
    
    if bool(re.match(pattern, string)):
        print('E-mail válido.')
    else:
        print('E-mail inválido!')
    
    return None

def password_check(string):
    
    pattern = "^(?=.*\d)(?=.*[A-Z])[a-zA-Z0-9]{8}$"
    
    if bool(re.match(pattern, string)):
        print('Senha válida.')
    else:
        print('Senha inválida!')
    
    return None

def cpf_check(string):
    
    pattern = "^(\d{3}.){2}\d{3}-\d{2}$"
    
    if bool(re.match(pattern, string)):
        print('CPF válido.')
    else:
        print('CPF inválido!')
    
    return None

def phone_check(string):
    
    pattern = "^((\(\d{2}\)\s)(9\d{4}?\-?\d{4}$))|((\d{2}\s)(9\d{8}$))"
    
    if bool(re.match(pattern, string)):
        print('Telefone válido.')
    else:
        print('Telefone inválido!')
    
    return None

def menu():
    print('[1] Validar nome.')
    print('[2] Validar e-mail.')
    print('[3] Validar senha.')
    print('[4] Validar cpf.')
    print('[5] Validar telefone.')
    print('[0] Sair da validação.')

menu()
option = int(input('Insira a opção: '))

while option !=0:
    if option == 1:
        string = input('Insira o nome e sobrenome: ')
        name_check(string)
    elif option == 2:
        string = input('Insira o e-mail: ')
        email_check(string)
    elif option == 3:
        string = input('Insira a senha: ')
        password_check(string)
    elif option == 4:
        string = input('Insira o CPF: ')
        cpf_check(string)
    elif option == 5:
        string = input('Insira o telefone: ')
        phone_check(string)
    else:
        print('Opção inválida.')
        
    print()
    menu()
    option = int(input('Insira a opção: '))