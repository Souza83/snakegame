import pygame  # Importa a biblioteca pygame
from pygame.locals import *  # Importa de pygame tudo do submódulo locals
from sys import exit  # Importa a função exit do módulo sys que fecha a janela
from random import randint  # Sorteia valores de um determinado intervalo

# Inicializa todas as funções e variáveis da biblioteca pygame
pygame.init()

pygame.mixer.music.set_volume(0.1)  # Configura volume da música de fundo (valores entre 0 e 1)

musica_de_fundo = pygame.mixer.music.load('SomdeFundo - CPU Talk.mp3') # Recebe a música de fundo (somente fundo em MP3)

pygame.mixer.music.play()  # Toca a música de fundo (-1 faz um loop após término da música)

som_colisao = pygame.mixer.Sound('SomdePonto - Coin.wav')  # Recebe som quando colisão (recebe extenção wav)

# Cria o objeto tela
largura = 640  # Medida da tela em pixel
altura = 480  # Medida da tela em pixel

x_cobra = int(largura/2)  # Representa a posição horizontal (eixo x = largura da tela / 2 = inicia no meio da tela)
y_cobra = int(altura/2)  # Representa a posição vertical (eixo y = altura da tela / 2 = inicia no meio da tela)
x_maca = randint(40, 600)  # Variável recebe valor aleatório entre 40 a 600 para o eixo x
y_maca = randint(50, 430)  # Variável recebe valor aleatório entre 50 a 430 para o eixo y
pontos = 0

fonte = pygame.font.SysFont('gabriola', 40, True, True)  # Define fonte, tamanho, negrito e itálico ()

tela = pygame.display.set_mode((largura, altura))  # Objeto que configura display

relogio = pygame.time.Clock()  # Variável que controla o tempo

# Configura nome da tela
pygame.display.set_caption('Jogo')

lista_cobra = []  # Recebe lista da posição para comprimento da cobra


# Função que aumenta a cobra
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))


# loop principal do jogo
while True:
    relogio.tick(30)  # Controla a taxa de frame por segundo (numero> = rápido e n< = devagar  )
    tela.fill((255, 255, 255))  # ("Limpa tela") A cada iteração do loop infinito a tela é preenchida com a cor preta
    mensagem = f'Pontos: {pontos}'  # Formata a mensagem que exibirá na tela com a variável pontos
    texto_formatado = fonte.render(mensagem, False, (0, 0, 0))  # Variável que formata (mensagem, pixelização e cor)
    for event in pygame.event.get():  # Detecta se algum evento ocorreu
        if event.type == QUIT:  # Para a janela fechar ao clicar em fechar
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_a]:  # Se pressionar a tecla "a"
        x_cobra = x_cobra - 20  # mova para esquerda
    if pygame.key.get_pressed()[K_d]:  # Se pressionar a tecla "d"
        x_cobra = x_cobra + 20  # mova para direita
    if pygame.key.get_pressed()[K_w]:  # Se pressionar a tecla "w"
        y_cobra = y_cobra - 20  # mova para cima
    if pygame.key.get_pressed()[K_s]:  # Se pressionar a tecla "s"
        y_cobra = y_cobra + 20  # mova para baixo

    # Representa Cobra ((local),(cor),(posição XY e PX))
    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    # Representa maça ((local),(cor),(posição XY e PX))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))

    if cobra.colliderect(maca):  # Verifica se colidiu ou sobrepôs
        x_maca = randint(40, 600)  # Variável que recebe valor aleatório entre 40 a 600 para o eixo x
        y_maca = randint(50, 430)  # Variável que recebe valor aleatório entre 50 a 430 para o eixo y
        pontos += 1  # Recebe valor de pontos + 1 ao colidirem
        som_colisao.play()  # Toca o som quando há colisão entre os objetos

    # Cria lista da posição da cabeça da cobra e lista do tamanho da cobra
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado, (400, 40))  # Exibe o texto na tela na posição XY.

    pygame.display.update()  # Atualiza tela do jogo a cada interação do loop principal
