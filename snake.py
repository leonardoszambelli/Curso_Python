import turtle
import random
import time

tela = turtle.Screen()
tela.title("Jogo da Cobrinha - Nokia 3310")

pontos=0

tela.bgcolor("black")
tela.setup(width=600, height=600)

tela.tracer(0)

cobra = turtle.Turtle() #jogador
cobra.speed(0)
cobra.shape("square")
cobra.color("violet")
cobra.penup() #impede que a cobra desenhe enquanto se movimenta 
cobra.goto(0,0)
cobra.direction = 'stop'

fruta=turtle.Turtle()
fruta.speed(0)
fruta.shape("circle")
fruta.color("green")
fruta.penup()
fruta.goto(0,100)

corpo= []

def cima():
    cobra.direction="up"

def baixo():
    cobra.direction="down"
    
def direita():
    cobra.direction="right"
    
def esquerda():
    cobra.direction="left"
    
#fazer a cobra obedecer aos comandos do teclado
tela.listen()
tela.onkeypress(cima,"Up")
tela.onkeypress(baixo,"Down")
tela.onkeypress(direita,"Right")
tela.onkeypress(esquerda,"Left")


while True:
    tela.update()
    
    if cobra.distance(fruta) < 20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        fruta.goto(x,y)
        pontos +=10 #Soma os pontos 
        
        novo_pedaco = turtle.Turtle() #criar um novo pedaco do corpo
        novo_pedaco.speed(0)
        novo_pedaco.shape("square")
        novo_pedaco.color("purple")
        novo_pedaco.penup()
        corpo.append(novo_pedaco)
        
        tela.title(f"Pontos: {str(pontos)}") 
    time.sleep(0.1)
    
    if cobra.direction=="left":
        x=cobra.xcor()
        cobra.setx(x-20)

    elif cobra.direction=="right":
        x=cobra.xcor()
        cobra.setx(x+20)
        
    elif cobra.direction=="down":
        y=cobra.ycor()
        cobra.sety(y-20)
    
    elif cobra.direction=="up":
        y=cobra.ycor()
        cobra.sety(y+20)
    
    for i in range(len(corpo)-1,0,-1):
    #iniciamos um laco para percorrer os pedacoes do corpo 
    #len retorna a quantidade de pedacos do corpo ##### len é length
    #esse -1 comeca pelo ultimo pedaco do corpo
    #esse 0 define que o laco FOR vai até o primeiro pedaco sem incluir ele
    #esse -1 faz o contrador diminuir de 1 em 1 andando de tras para a frente    
        
        x = corpo[i-1].xcor()
        y = corpo[i-1].ycor()
        corpo[i].goto(x,y)
        
        if len(corpo)>0:
            x=cobra.xcor()
            y=cobra.ycor()
            corpo[0].goto(x,y)
    
    if cobra.xcor()>290 or cobra.xcor() < -290 or cobra.ycor()>290 or cobra.ycor() < -290:
        tela.title(f"Game Over! Pontuação Final : {str(pontos)}")
        cobra.goto(0,0) 
        cobra.direction= "stop"   
        break

tela.mainloop()