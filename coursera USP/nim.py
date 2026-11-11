def computador_escolhe_jogada(n, m):
    # Se tirar peças de forma que o resto seja múltiplo de (m + 1)
    if n % (m + 1) != 0:
        # Tenta deixar um múltiplo de (m + 1) para o usuário
        # O computador tira o resto da divisão por (m + 1) se for menor ou igual a m
        jogada = n % (m + 1)
        if jogada > 0:
            return jogada
    
    # Se já for múltiplo ou se a estratégia exigir, o computador tira o máximo possível (m)
    if m <= n:
        return m
    return n


def usuario_escolhe_jogada(n, m):
    valido = False
    while not valido:
        try:
            jogada = int(input("Quantas peças você vai tirar? "))
            if 1 <= jogada <= m and jogada <= n:
                valido = True
            else:
                print("\nOops! Jogada inválida! Tente de novo.\n")
        except ValueError:
            print("\nOops! Jogada inválida! Tente de novo.\n")
    return jogada


def partida():
    print()
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print()

    # Define quem começa
    if n % (m + 1) == 0:
        print("Você começa!")
        vez_computador = False
    else:
        print("Computador começa!")
        vez_computador = True

    while n > 0:
        if vez_computador:
            jogada = computador_escolhe_jogada(n, m)
            n -= jogada
            if jogada == 1:
                print("\nO computador tirou uma peça.")
            else:
                print(f"\nO computador tirou {jogada} peças.")
            
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            elif n > 1:
                print(f"Agora restam {n} peças no tabuleiro.")
            
            vez_computador = False
        else:
            jogada = usuario_escolhe_jogada(n, m)
            n -= jogada
            if jogada == 1:
                print("\nVocê tirou uma peça.")
            else:
                print(f"\nVocê tirou {jogada} peças.")
            
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            elif n > 1:
                print(f"Agora restam {n} peças no tabuleiro.")
            
            vez_computador = True

    print("\nFim do jogo! ", end="")
    if vez_computador:
        print("Você ganhou!")
        return 1  # Usuário venceu
    else:
        print("O computador ganhou!")
        return 2  # Computador venceu


def campeonato():
    vitorias_usuario = 0
    vitorias_computador = 0

    for i in range(1, 4):
        print(f"\n**** Rodada {i} ****")
        vencedor = partida()
        if vencedor == 1:
            vitorias_usuario += 1
        else:
            vitorias_computador += 1

    print("\n**** Final do campeonato! ****")
    print(f"\nPlacar: Você {vitorias_usuario} X {vitorias_computador} Computador")


def principal():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    
    opcao = int(input())
    
    if opcao == 1:
        print("\nVoce escolheu uma partida isolada!")
        partida()
    elif opcao == 2:
        print("\nVoce escolheu um campeonato!")
        campeonato()


if __name__ == "__main__":
    principal()