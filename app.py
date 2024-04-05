import os

def clear():
    '''
        Essa função é responsável por apagar tudo que está sendo mostrado no console.
    '''
    os.system('cls')

def titulo_app():
    '''
        Essa função é responsável por exibir o título do aplicativo no terminal.
    '''
    print('''

    ╭━━━╮╱╱╭╮╱╱╱╱╱╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╭━━━╮╱╱╱╭╮╭╮
    ┃╭━╮┃╱╱┃┃╱╱╱╱╱╱┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱┃╭━╮┃╱╱╭╯╰┫┃
    ┃┃╱╰╋━━┫┃╭━━┳╮╭┫┃╭━━┳━╯┣━━┳━┳━━╮┃╰━╯┣╮╱┣╮╭┫╰━┳━━┳━╮
    ┃┃╱╭┫╭╮┃┃┃╭━┫┃┃┃┃┃╭╮┃╭╮┃╭╮┃╭┫╭╮┃┃╭━━┫┃╱┃┃┃┃╭╮┃╭╮┃╭╮╮
    ┃╰━╯┃╭╮┃╰┫╰━┫╰╯┃╰┫╭╮┃╰╯┃╰╯┃┃┃╭╮┃┃┃╱╱┃╰━╯┃╰┫┃┃┃╰╯┃┃┃┃
    ╰━━━┻╯╰┻━┻━━┻━━┻━┻╯╰┻━━┻━━┻╯╰╯╰╯╰╯╱╱╰━╮╭┻━┻╯╰┻━━┻╯╰╯
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
    ''')

def menu_opcoes():
    '''
        Essa função é responsável por exibir o menu de opções no terminal.
    '''
    print('[ 1 ] - Somar \n[ 2 ] - Subtrair \n[ 3 ] - Multiplicar \n[ 4 ] - Dividir \n[ 9 ] - Sair do aplicativo \n')

def somar():
    '''
        Essa funçaõ é responsável por receber dois números, somá-los e exibí-los no terminal.

        -Inputs:
            n1;
            n2;
            soma.

        -Outputs:
            n1 + n2 = soma
    '''
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    soma = n1 + n2
    print(f'{n1} + {n2} = {soma}')

def subtrair():
    '''
        Essa funçaõ é responsável por receber dois números, subtraí-los e exibí-los no terminal.

        -Inputs:
            n1;
            n2;
            subtrair.

        -Outputs:
            n1 - n2 = subtrair
    '''
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    subtrair = n1 - n2
    print(f'{n1} - {n2} = {subtrair}')

def multiplicar():
    '''
        Essa funçaõ é responsável por receber dois números, multiplicá-los e exibí-los no terminal.

        -Inputs:
            n1;
            n2;
            multiplicar.

        -Outputs:
            n1 * n2 = multiplicar
    '''
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    multiplicar = n1 * n2
    print(f'{n1} x {n2} = {multiplicar}')

def dividir():
    '''
        Essa funçaõ é responsável por receber dois números, dividí-los e exibí-los no terminal.

        -Inputs:
            n1;
            n2;
            dividir.

        -Outputs:
            n1 / n2 = dividir
    '''
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    dividir = n1 / n2
    print(f'{n1} ÷ {n2} = {dividir}')

def opcao_invalida():
    '''
        Essa função é responsável por exibir uma mensagem de opção inválida caso o usuário digite algo que não esteja no menu de opções.
    '''
    print('Opção inválida, digite uma opção válida para continuar\n')

def finalizar_app():
    '''
        Essa função é responsável por encerrar o aplicativo
    '''
    print('App finalizado...')

def selecionar_opcao_do_menu():
    '''
        Essa função é responsável por manusear o menu de opções, considerando o que o usuário digita.

        -Inputs:
            opcao_escolhida;

        -Outputs:
            funções - somar, subtrair, multiplicar, dividir, finalizar_app e opcao_invalida;
    '''
    opcao_escolhida = 0
    while opcao_escolhida !=9:
        try:
            opcao_escolhida = int(input('Selecione uma opção: '))
            if opcao_escolhida == 1:
                somar()
            elif opcao_escolhida == 2:
                subtrair()
            elif opcao_escolhida == 3:
                multiplicar()
            elif opcao_escolhida == 4:
                dividir()
            elif opcao_escolhida == 9:
                finalizar_app()
            else:
                opcao_invalida()
        except:
            opcao_invalida()

def main():
    '''
        Essa é a função principal do aplicativo.
    '''
    titulo_app()
    menu_opcoes()
    selecionar_opcao_do_menu()

if __name__ == '__main__':
    '''
        Aqui será executado o App.
    '''
    main()
