
import os


lista_de_restaurantes = [{'Nome':'Arvo', 'Categoria':'Comida Caseira', 'Status':'Ativo'},
                         {'Nome':'Oficina do Sabor', 'Categoria':'Regional', 'Status':'Inativo' },
                         {'Nome':'Pizzaria Atlântico', 'Categoria':'Massas', 'Status':'Ativo'}
                         ]


def exibir_nome_programa():
    ''' Exibe o nome estilizado do programa na tela '''
    print("""   
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)



def exibir_opcoes():
    ''' Exibe as opções disponíveis no menu principal '''
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurante")
    print("3. Alternar Status do Restaurante")
    print("4. Sair\n")



def voltar_menu_principal():
    ''' Função responsável por
    retornar para o menu principal'''
    input('Digite uma tecla para voltar para o "menu principal".\n')
    main()
    

    
def exibir_subtitulo(titulo):
    '''Esta função é responsável por cadastrar
    um novo restaurante '''
    os.system('cls')
    linha = '*' * (len(titulo) + 4)
    print(linha)
    print(titulo)
    print(linha)
    print()



def funcao_finalizar_app():
    os.system('cls')
    exibir_subtitulo('O app está sendo finalizado...')


def valor_nao_cadastrado():
    
    print('Essa opcão não é válida para esse programa!')
    print('='*50)
    voltar_menu_principal()



def cadastrar_restaurante():
    
    # docString
    '''
    Inputs:
    - Nome do Restaurante
    - Categoria do Restaurante
    
    Outputs:
    - Adicionando novos Restaurantes à lista de Restaurantes
    
    '''
    
    os.system('cls')
    exibir_subtitulo('Cadastro de restaurantes')
    nome_do_restaurantes = input('Digite o nome do restaurante que deseja cadastrar: ')
    nome_da_categoria = input(f'Digite o nome da categoria do restaurante, "{nome_do_restaurantes}", que deseja cadastrar: ')
    dado_do_restaurante = {'Nome': nome_do_restaurantes, 'Categoria':nome_da_categoria, 'Status':False}
    lista_de_restaurantes.append(dado_do_restaurante)
    print(f'\nO restaurande "{nome_do_restaurantes}" foi cadastrado com sucesso.\n')
    voltar_menu_principal()
    
    
     
def listar_restaurante():
    os.system('cls')
    exibir_subtitulo('Listando Restaurantes')
    cont =0;
    print(f'{'Restaurantes cadastrados'.ljust(25)} | {'Categoria'.ljust(20)} | Status\n')
    for restuarante_cadastrado in lista_de_restaurantes:
        so_nome = restuarante_cadastrado['Nome']
        so_categoria = restuarante_cadastrado['Categoria']
        so_status = 'Ativo' if restuarante_cadastrado['Status'] else 'Inativo'
        cont+=1
        print(f'{cont}º - {so_nome.ljust(20)} | {so_categoria.ljust(20)} | {so_status}\n')
    voltar_menu_principal()



def mudanca_status_restaurante():
    exibir_subtitulo('Alternando Status do Restaurante')
    nome_restaurante_alteracao = input('Digite o nome do restaurante para a mudança do Status: ')
    
    value_atual_Status = False
    
    for rest_status in lista_de_restaurantes:
        if nome_restaurante_alteracao == rest_status['Nome']:
            value_atual_Status = True
            rest_status['Status'] = not rest_status['Status']
            mensagem = f'O Restaurante {nome_restaurante_alteracao} foi "Ativado" com sucesso.' if rest_status['Status'] else f'O Restaurante {nome_restaurante_alteracao} foi "Desativado" com sucesso.'
            print(mensagem)
    
    
    if not nome_restaurante_alteracao:
        print('O Restaurante não foi encontrado')
    
        
    voltar_menu_principal()




def escolher_opcao():
    try:
        valor_opcao = int(input("Escolha uma opcão: "))
        #print(f'Opção solicitado: {valor_opcao}')
        if valor_opcao == 1:
            cadastrar_restaurante()
        elif valor_opcao == 2:
            listar_restaurante()
        elif valor_opcao == 3:    
            mudanca_status_restaurante()
        elif valor_opcao == 4:
            funcao_finalizar_app()
        else :
            valor_nao_cadastrado()
    except:
        valor_nao_cadastrado()
      


    
    
def main():    
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()
        


if __name__ == '__main__':
    main()    
    
    