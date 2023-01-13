import turtle #Parecido com a biblioteca pygames. Funciona muito bem para jogos simples
import winsound # para reproduzir o som quando a bola bate na parede

wn = turtle.Screen() #criando uma janela
wn.title("Pong")
wn.bgcolor("black") #mudando a cor de background da janela
wn.setup(width=800, height=600) #mudando o tamanho da janela
wn.tracer(0) #para a janela de atualizar, portanto tempo que atualizar manualmente -> Assim podemos aumentar a velocidade do jogo.

#Score
score_a = 0
score_b = 0

# Paddle A
paddle_a  = turtle.Turtle() #objeto
paddle_a.speed(0) # velocidade da animação - estamos setando para velocidade maxima.
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #mudando o tamanho do paddle A
paddle_a.penup()
paddle_a.goto(-350, 0) # local onde ele vai começar

# Paddle B
paddle_b  = turtle.Turtle() #objeto - (obs: poo)
paddle_b.speed(0) # velocidade da animação - estamos setando para velocidade maxima.
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #mudando o tamanho do paddle A
paddle_b.penup()
paddle_b.goto(350, 0) # local onde ele vai começar

# Ball
ball  = turtle.Turtle() #objeto - (obs: poo)
ball.speed(0) # velocidade da animação - estamos setando para velocidade maxima.
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0) # local onde ele vai começar
ball.dx = 0.15 #eixo x - toda vez que a bola se mover, ela se deslocara em 0.15
ball.dy = 0.15 #eixo y - toda vez que a bola se mover, ela se deslocara em 0.15

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("PlayerA: 0  PlayerB: 0", align="center", font=("Courier", 24, "normal"))

# Funções
# O paddle A e B poderá se mover para cima ou para baixo
def paddle_a_up():
    y = paddle_a.ycor() #retorna as coordenadas de y 
    y += 20 
    paddle_a.sety(y) # setando o paddle para o novo local

def paddle_a_down():
    y = paddle_a.ycor() #retorna as coordenadas de y 
    y -= 20 
    paddle_a.sety(y) # setando o paddle para o novo local

def paddle_b_up():
    y = paddle_b.ycor() #retorna as coordenadas de y 
    y += 20 
    paddle_b.sety(y) # setando o paddle para o novo local

def paddle_b_down():
    y = paddle_b.ycor() #retorna as coordenadas de y 
    y -= 20 
    paddle_b.sety(y) # setando o paddle para o novo local

#keyboard binding
wn.listen() #fala para "escutar" pela tecla digitada
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#main game loop
while True:
    wn.update() #faz o update da tela

    #movimento da bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking 
    if ball.ycor() > 290: # bola bateu na parede
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    if ball.ycor() < -290: # bola bateu na parede
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390: # fez gol
        ball.goto(0, 0) # bola volta para o ponto inicial
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("PlayerA: {}  PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390: # gol
        ball.goto(0, 0) # bola volta para o ponto inicial
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("PlayerA: {}  PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # colisão entre o paddle e a bola 
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
        ball.setx(-340)
        ball.dx *= -1
