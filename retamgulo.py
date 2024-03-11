import turtle

# Função para desenhar a planta baseada na largura e altura
def desenha_planta(largura, altura):
    # Configurações iniciais da tartaruga
    turtle.speed("fastest")  # Velocidade máxima
    turtle.penup()  # Levanta a caneta para mover sem desenhar
    turtle.goto(-largura * 10, -altura * 10)  # Posiciona a tartaruga no canto esquerdo inferior
    turtle.pendown()  # Abaixa a caneta para começar a desenhar

    # Desenha um retângulo com base nas dimensões informadas
    turtle.color("green")  # Define a cor para verde
    for _ in range(2):
        turtle.forward(largura * 120)
        turtle.left(90)
        turtle.forward(altura * 120)
        turtle.left(90)

    # Mantém a janela aberta até que o usuário a feche
    turtle.done()

# Solicita a largura e altura ao usuário
largura_informada = int(input("Digite a largura do terreno (em metros): "))
altura_informada = int(input("Digite a altura do terreno (em metros): "))
desenha_planta(largura_informada, altura_informada)
