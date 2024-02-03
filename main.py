import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

'''
Steps:
Create player with method move().'''

screen = Screen()
screen.tracer(0)
player = Player()
car = CarManager()


screen.listen()
screen.onkeypress(player.move_forward, 'Up')





screen.setup(width=600, height=600)

game_is_on= True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    player.back_to_beginning()
    car.move()


screen.exitonclick()