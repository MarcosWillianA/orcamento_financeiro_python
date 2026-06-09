lista_movimentacoes = []
rodando = True
mensagem = ''' 
Seja bem vindo ao App de Orçamento Pessoal

Escolha uma das opções do menu:

1 - Registrar entrada;
2 - Registrar saída;
3 - Exibir extrato;
4 - Exibir saldo;
5 - Sair

'''

def exibir_menu():
    print(mensagem)

def registrar_movimentacoes(tipo, descricao, valor):
    movimentacao = [tipo, descricao, valor]
    lista_movimentacoes.append(movimentacao)

def calcular_saldo(lista):
    receita = 0
    despesa = 0
    for item in lista:
        if item[0] == 'Entrada':
            receita += item[2]
        else:
            despesa += item[2]
    saldo = receita - despesa
    return saldo
    
def exibir_extrato(lista):
    if len(lista) < 1:
        print('Não há registro de movimentações no momento.')
    else:
        for item in lista:
            print(f'{item[0]} -- {item[1]}: R${item[2]:.2f}')
    
    saldo_atual = calcular_saldo(lista_movimentacoes)
    print(f'Saldo: R${saldo_atual:.2f}\n')


while rodando:
    exibir_menu()
    
    opcao_usuario = input('Qual opção do menu vai escolher? ')
    
    if opcao_usuario == '1':
        tipo_movimentacao = 'Entrada'
        cancelou = False # Variável para controlar se o usuário desistiu no meio do caminho
        
        while True:
            entrada_movimentacao = input('Que tipo de entrada quer registrar? (ou digite 0 para voltar): ').strip()
            
            if entrada_movimentacao == '0':
                cancelou = True
                break # Sai da validação da descrição
                
            descricao_movimentacao = entrada_movimentacao.capitalize()
            if descricao_movimentacao != '':
                break
            else:
                print('A descrição não pode ficar em branco, por favor, digite uma descrição adequada ')
        
        # Se ele cancelou na descrição, o 'continue' faz o código ignorar o resto e voltar pro menu principal
        if cancelou:
            print("Operação cancelada. Voltando ao menu...\n")
            continue 
            
        while True:
            entrada_usuario = input('Qual o valor que quer registrar? (ou digite 0 para voltar): ').strip()
            
            if entrada_usuario == '0':
                cancelou = True
                break # Sai da validação do valor
                
            entrada_formatada = entrada_usuario.replace(',','.')
            if entrada_formatada.replace('.', '', 1).isdigit():
                valor_movimentacao = round(float(entrada_formatada), 2)
                if valor_movimentacao > 0:
                    break
                else:
                    print('Erro: o valor de entrada deve ser maior que zero')
            else:
                print('Erro: digite um valor válido (Ex.: 1650,00 ou 1650.00 ou 1650).')
        
        if cancelou:
            print("Operação cancelada. Voltando ao menu...\n")
            continue
            
        # Só executa o registro se o usuário não tiver cancelado nada
        registrar_movimentacoes(tipo_movimentacao, descricao_movimentacao, valor_movimentacao)
        print(f'Entrada de {descricao_movimentacao} de R${valor_movimentacao:.2f} registrada com sucesso \n')
        
    elif opcao_usuario == '2':
        tipo_movimentacao = 'Saída'
        cancelou = False
        
        while True:
            saida_movimentacao = input('Que tipo de saída quer registrar? (ou digite 0 para voltar): ').strip()
            
            if saida_movimentacao == '0':
                cancelou = True
                break
                
            descricao_movimentacao = saida_movimentacao.capitalize()
            if descricao_movimentacao != '':
                break
            else:
                print('A descrição não pode ficar em branco, por favor digite uma descrição adequada')
                
        if cancelou:
            print("Operação cancelada. Voltando ao menu...\n")
            continue
            
        while True:
            saida_usuario = input('Qual o valor da saída? (ou digite 0 para voltar): ').strip()
            
            if saida_usuario == '0':
                cancelou = True
                break
                
            saida_formatada = saida_usuario.replace(',','.')
            if saida_formatada.replace('.', '', 1).isdigit():
                valor_movimentacao = round(float(saida_formatada), 2)
                if valor_movimentacao > 0:
                    break
                else:
                    print('Erro: o valor de saída deve ser maior que zero')
            else:
                print('Erro: digite um valor válido (Ex.: 165,00 ou 165.00 ou 165).')
                
        if cancelou:
            print("Operação cancelada. Voltando ao menu...\n")
            continue
        
        registrar_movimentacoes(tipo_movimentacao, descricao_movimentacao, valor_movimentacao)
        print(f'Saída de {descricao_movimentacao} de R${valor_movimentacao:.2f} registrada com sucesso \n')
        
    elif opcao_usuario == '3':
        exibir_extrato(lista_movimentacoes)
        
    elif opcao_usuario == '4':
        saldo_atual = calcular_saldo(lista_movimentacoes)
        print(f'O saldo atual é de R${saldo_atual:.2f}\n')
            
    elif opcao_usuario == '5':
        print('Volte sempre!')
        rodando = False
    
    else:
        print('Opção inválida. Por favor, escolha uma das opções do menu.\n')