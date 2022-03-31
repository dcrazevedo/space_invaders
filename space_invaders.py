import turtle
import os
import math
import random

# Cria a tela

window = turtle.Screen()
window.bgcolor('black')
window.title('Space Invaders')
#window.bgpic('space_invaders_background.gif')

# Registrar as formas

turtle.register_shape('invader.gif')
#turtle.register_shape('player.gif')

# Desenhar a borda
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('white')
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Placar
score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290, 280)
score_string = 'Score: {}'.format(score)
score_pen.write(score_string, False, align='left', font=('Arial', 14, 'normal'))
score_pen.hideturtle()

# Cira jogador
player = turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

player_speed = 15

# Numero de inimigos

number_of_enemies = 5
enemies = []

# Criar inimigo
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color('red')
    enemy.shape('circle')
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x,y)

enemy_speed = 2

# Criando a bala

bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bullet_speed = 20

# Define o estado da bala
## ready - pronta pra atirar
## fire - atirou
bullet_state = 'ready'

# Mover para esqueda

def move_left():

    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)

# Mover para esqueda

def move_right():

    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    # Declarar bullet_state como variável global

    global bullet_state

    if bullet_state == 'ready':
    
        bullet_state = 'fire'   
        
        # Mover a bala
        x = player.xcor()
        y = player.ycor() + 10

        bullet.setposition(x, y)
        bullet.showturtle()

def is_collision(t1, t2):

    delta_x = t1.xcor() - t2.xcor()
    delta_y = t1.ycor() - t2.ycor()

    distance = math.sqrt(math.pow(delta_x,2) + math.pow(delta_y, 2))

    if distance < 15:
        return True
    else:
        return False

# Conexão com teclado

turtle.listen()
turtle.onkey(move_left, 'Left')
turtle.onkey(move_right, 'Right')
turtle.onkey(fire_bullet, 'space')

# Main game loop

while True:

    # Mover o inimigo
    for enemy in enemies:
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        # Mover inimigo de volta e para baixo
        if enemy.xcor() > 280:
            for e in enemies:
            
                y = e.ycor()
                y -= 40
                e.sety(y)

            enemy_speed *= -1
        
        if enemy.xcor() < -280:
            for e in enemies:
            
                y = e.ycor()
                y -= 40
                e.sety(y)

            enemy_speed *= -1
        # Checa colisao da bala e do inimigo
        if is_collision(bullet, enemy):
            
            # Reseta a bala
            
            bullet.hideturtle()
            bullet_state = 'ready'
            bullet.setposition(0, -400)
            
            # Reseta o inimigo            
            
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x,y)
            score += 10
            score_string = 'Score: {}'.format(score)
            score_pen.clear()
            score_pen.write(score_string, False, align='Left', font=('Arial', 14, 'normal'))

        if is_collision(enemy, player):

            player.hideturtle()
            enemy.hideturtle()

            print('Game Over')
            break
        
    # Mover a bala
    if bullet_state == 'fire':
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # Checar se a bala já atingiu a borda
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = 'ready'


sair = input('Aperte Enter para sair')