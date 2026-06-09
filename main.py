lista_movimentacoes = []
rodando = True
mensagem = ''' 
Seja bem vindo ao App de Orçamento Pessoal

Escolha uma das opções do menu:

1 - Registrar entrada;
2 - Registrar saída;
3 - Exibir extrato;
4 - Calcular saldo;
5 - Sair

'''

def exibir_menu():
    print(mensagem)

def registrar_movimentacoes(tipo, descricao, valor):
    movimentacao = f'{tipo} | {descricao} | {valor} '
    lista_movimentacoes.append(movimentacao)

while rodando:
    exibir_menu()
    
    opcao_usuario = input('Qual opção do menu vai escolher? ')
    
    if opcao_usuario == '1':
        tipo_movimentacao = 'entrada'
        descricao_movimentacao = input('Que tipo de entrada quer registrar? ')
        valor_movimentacao = float(input('Qual o valor que vai registrar? '))
        registrar_movimentacoes(tipo_movimentacao, descricao_movimentacao, valor_movimentacao)
    
    if opcao_usuario == '5':
        print('Volte sempre!')
        rodando = False
    
    else:
        print('Opção inválida. Por favor, escolha uma das opções do menu.')