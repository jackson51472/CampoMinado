import random

import numpy as np


def randomizarTabuleiroQuadro():
    # Função feita para randomizar os valores da Matriz
    tesouro = 0
    bomba = 0
    colunas = 5
    linha = 5

    listaObjetos = ['🌐', '💣', '⛏']

    tabuleiro = np.zeros((linha, colunas), str)

    # Fazer um tabuleiro do ZERO
    for i in range(linha):
        y = random.choices(['🌐', '💣', '⛏'], [8, 3, 1], k=colunas)
        tabuleiro[i] = y

    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if tabuleiro[i][j] == '⛏':
                tesouro += 1
            else:
                if tabuleiro[i][j] == '💣':
                    bomba += 1

    # !!! Verificar o número de BOMBAS e MINA, caso seja inferior ao desejado ele ira refazer o Vetor até que apareça um desejado.
    while bomba > 5 or tesouro > 2 or bomba < 3 or tesouro == 0:

        # !!! FAZ A MESMA COISA QUE O DA LINHA 5 ATÉ A LINHA 17 COM DIFERENÇA QUE AQUI NÃO TEM O TAMANHO.
        tesouro = 0
        bomba = 0

        for i in range(linha):
            y = random.choices(['🌐', '💣', '⛏'], [8, 3, 1], k=colunas)
            tabuleiro[i] = y

        for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro)):
                if tabuleiro[i][j] == '⛏':
                    tesouro += 1
                else:
                    if tabuleiro[i][j] == '💣':
                        bomba += 1

    return tabuleiro

def randomizarTabuleiroLinha():
    # Função feita para randomizar os valores do Vetor
    tesouro = 0
    bomba = 0
    tamanho = 10

    # Fazer um tabuleiro do ZERO
    tabuleiro = random.choices(['🌐', '💣', '⛏'], [8, 3, 1], k=tamanho)

    for i in range(len(tabuleiro)):
        if tabuleiro[i] == '⛏':
            tesouro += 1
        else:
            if tabuleiro[i] == '💣':
                bomba += 1

    # !!! Verificar o número de BOMBAS e MINA, caso seja inferior ao desejado ele ira refazer o Vetor até que apareça um desejado.
    while bomba > 5 or tesouro > 2 or bomba < 3 or tesouro == 0:

        # !!! FAZ A MESMA COISA QUE O DA LINHA 5 ATÉ A LINHA 17 COM DIFERENÇA QUE AQUI NÃO TEM O TAMANHO.
        tesouro = 0
        bomba = 0

        tabuleiro = random.choices(['🌐', '💣', '⛏'], [8, 3, 1], k=tamanho)

        for i in range(len(tabuleiro)):
            if tabuleiro[i] == '⛏':
                tesouro += 1
            else:
                if tabuleiro[i] == '💣':
                    bomba += 1


    return tabuleiro

def tabelaMostrada(tipoJogo):
    # Criar um vetor do mesmo tamanho do Vetor ou Matriz que sera retornado no randomizarTabuleiro, só que com os simbolos trocados por ⭕
    if tipoJogo == 1:

        provTab = randomizarTabuleiroLinha()
        for i in range(len(provTab)):
            provTab[i] = (f"{1 + i} ⭕ ")

        return provTab
    else:
        if tipoJogo == 2:
            provTab = randomizarTabuleiroQuadro()
            for i in range(len(provTab)):
                for j in range(len(provTab)):
                    provTab[i][j] = ("⭕")
        return provTab

def startGame(continuação):
    # Start no game
    tipo = 0
    while tipo < 1 or tipo > 2:

        tipo = int(input("TIPO DE JOGO\n[1] EM LINHA\n[2] EM QUADRO !!! AINDA NÃO FUNCIONAL: \n-"))

    if tipo == 1:
        modoUm()

    else:
        modoDois()
    print("=========================================================")

    while continuação == 1:
        continuação = int(input("Deseja continuar: [1 SIM]   [2 NÃO] "))

        if continuação != 1:
            print("=========================================================")
            print("FECHANDO O JOGO:")

        else:
            if tipo == 1:
                modoUm()
            else:
                modoDois()

def verificarCampos(tabuleiroVerdadeiro, tabuleiroFalso):
    # Feita para vericar cada unidade do vetor ou matriz e retornar True se todas as unidades contendo Terra foram adivinhadas,
    # ou  retornar falso se ainda falta unidade a ser adivinhada e também verificar se ele jogou emcima de uma bomba ou tesouro
    mina = 0
    bomba = 0
    terra = 0
    correto = 0

    # Faz a contagem de BOMBA, MINA e Terra
    for i in range(len(tabuleiroVerdadeiro)):
        if tabuleiroVerdadeiro[i] == '⛏':
            mina += 1
        else:
            if tabuleiroVerdadeiro[i] == '💣':
                bomba += 1
            else:
                terra += 1
    # Faz contagem de quantas unidades foram acertadas.
    for i in range(len(tabuleiroFalso)):

        if "❌" in tabuleiroFalso[i]:
            correto += 1

    # Verifica se a quantidade de Terra e a quantidade de unidades acertadas são iguas, se forem iguais o jogo acaba
    if correto == terra:
        return True

    # Caso ainda não seja iguais o jogo continua.
    else:
        return False

def verificarCampos(tabuleiroVerdadeiro, tabuleiroFalso, i):
    # Feita para vericar cada unidade do vetor ou matriz e retornar True se todas as unidades contendo Terra foram adivinhadas,
    # ou  retornar falso se ainda falta unidade a ser adivinhada e também verificar se ele jogou emcima de uma bomba ou tesouro
    mina = 0
    bomba = 0
    terra = 0
    correto = 0

    # Faz a contagem de BOMBA, MINA e Terra
    for i in range(len(tabuleiroVerdadeiro)):
        for j in range(len(tabuleiroVerdadeiro)):
            if tabuleiroVerdadeiro[i][j] == '⛏':
                mina += 1
            else:
                if tabuleiroVerdadeiro[i][j] == '💣':
                    bomba += 1
                else:
                    terra += 1
    # Faz contagem de quantas unidades foram acertadas.
    for i in range(len(tabuleiroFalso)):
        for j in range(len(tabuleiroFalso)):
            if "❌" in tabuleiroFalso[i][j]:
                correto += 1

    # Verifica se a quantidade de Terra e a quantidade de unidades acertadas são iguas, se forem iguais o jogo acaba
    if correto == terra:
        return True

    # Caso ainda não seja iguais o jogo continua.
    else:
        return False

def modoUm():
    #Modo de jogo em linha == Vetor

    # Aqui cria os vetores ou matrizes para começar o jogo
    tabuleiro = randomizarTabuleiroLinha()
    provTab = tabelaMostrada(1)
    tentantiva = True
    while tentantiva == True:
        menorPosicao = 1
        maiorPosicao = len(tabuleiro) + 1

        # Printa o estado atual do Tabuleiro
        print(tabuleiro)
        print(provTab)
        jogada = int(input("Onde você jogará nessa tentativa: "))

        # Verifica se o número jogado e inválido
        while jogada < menorPosicao or jogada >= maiorPosicao:
            jogada = int(input("VOCÊ DIGITOU ERRRADO. DIGITE NOVAMENTE: "))

        # CASO A UNIDADE QUE O JOGADOR JOGUE SEJA == BOMBA
        if tabuleiro[jogada - 1] == "💣":
            print("=========================================================\nVOCÊ PERDEU!!!!!!!!!!!!!!!!!!!!!")
            print(tabuleiro)
            tentantiva = False

        else:
            bombas = 0
            #VERIFICARA QUANTAS BOMBAS TEM POR PERTO
            # EX:'💣',    '🌐',  '💣' VOCE JOGA NA SEGUNDA CASA IRA APARECER QUANTAS BOMBAS EXISTEM EMVOLTA DA CASA 2
            #    '1 ⭕ ', "2❌", '3 ⭕ '
            for i in range(len(tabuleiro)):

                if i == (jogada - 1):
                    if (i - 1) > 0:
                        if tabuleiro[i - 1] == "💣":
                            bombas += 1

                    if i + 1 < len(tabuleiro):
                        if tabuleiro[i + 1] == "💣":
                            bombas += 1

            # CASO A UNIDADE QUE O JOGADOR JOGUE SEJA == TESOURO
            if tabuleiro[jogada - 1] == "⛏":
                print("=========================================================\nPARABÉNS VOCÊ ACHOU O TESOURO")
                print(tabuleiro)
                tentantiva = False

            else:
                # CASO A UNIDADE QUE O JOGADOR JOGUE SEJA == TERRA
                provTab[jogada - 1] = f"{bombas}❌"


                # Verifica se o jogador acertou todas as terras ou se ainda falta
                if verificarCampos(tabuleiro, provTab) == True:
                    print(tabuleiro)
                    print("=========================================================\nParabén você ganhou!!!!!!!!!!!!!!!!!!!")
                    tentantiva = False

def modoDois():
    #Modo de jogo em Quadro == Matriz

    # Aqui cria os vetores ou matrizes para começar o jogo
    tabuleiro = randomizarTabuleiroQuadro()
    provTab = tabelaMostrada(2)
    tentantiva = True

    while tentantiva == True:
        print(tabuleiro)
        print(provTab)
        linha = int(input("Linha jogada: "))
        while linha > 5:
            linha = int(input("Não existe essa linha, digite novamente: "))

        coluna = int(input("Coluna jogada: "))
        while coluna > 5:
            coluna = int(input("Não existe essa coluna, digite novamente: "))


        for i in range(len(provTab)):
            if (linha - 1) == i:
                for j in range(len(provTab)):
                    if (coluna - 1) == j:
                        if tabuleiro[i][j] == "💣":
                            print(
                                "=========================================================\nVOCÊ PERDEU!!!!!!!!!!!!!!!!!!!!!")
                            print(tabuleiro)

                            tentantiva = False
                            print("=========================================================")
                            break

                        else:
                            # CASO A UNIDADE QUE O JOGADOR JOGUE SEJA == TESOURO
                            if tabuleiro[i][j] == "⛏":
                                print("=========================================================\nPARABÉNS VOCÊ ACHOU O TESOURO")
                                print(tabuleiro)

                                tentantiva = False
                                print("=========================================================")
                                break


                            else:
                                bombas = 0
                                for i in range(len(provTab)):
                                    if i == (linha - 1):
                                        for j in range(len(provTab)):
                                            if i == linha - 1 and j == coluna - 1:

                                                #Verificar linha debaixo
                                                if (i + 1) < 5:
                                                    if (j + 1) < 5:
                                                        if tabuleiro[i + 1][j + 1] == "💣":
                                                            bombas += 1

                                                    if (j - 1) >= 0:
                                                        if tabuleiro[i + 1][j - 1] == "💣":
                                                            bombas += 1

                                                    if tabuleiro[i + 1][j] == "💣":
                                                        bombas += 1


                                                #Verificar linha de cima
                                                if (i - 1) >= 0:
                                                    if (j + 1) < 5:
                                                        if tabuleiro[i - 1][j + 1] == "💣":
                                                            bombas += 1

                                                    if (j - 1) >= 0:
                                                        if tabuleiro[i - 1][j - 1] == "💣":
                                                            bombas += 1

                                                    if tabuleiro[i - 1][j] == "💣":
                                                        bombas += 1
                                                #Verificar linha jogada
                                                if (j + 1) < 5:
                                                    if tabuleiro[i][j + 1] == "💣":
                                                        bombas += 1

                                                if (j - 1) >= 0:
                                                    if tabuleiro[i][j - 1] == "💣":
                                                        bombas += 1

                                for i in range(len(provTab)):
                                    if i == (linha - 1):
                                        for j in range(len(provTab)):
                                            if i == linha - 1 and j == coluna - 1:
                                                provTab[i][j] =  f"{bombas}❌"
                            if verificarCampos(tabuleiro,provTab, i) == True:
                                print(tabuleiro)
                                print("=========================================================\nParabén você ganhou!!!!!!!!!!!!!!!!!!!")
                                tentantiva = False

startGame(1)

