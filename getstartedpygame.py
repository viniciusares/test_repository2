# This code is to test and get started with Pygame
# In future, the objective is to make an Othello game
# Vinicius Ares - 08/09/2018

import pygame as pg
pg.init()
(win_width, win_height) = (300, 300)
win = pg.display.set_mode((win_width, win_height))

pg.display.flip()
pg.display.set_caption("Reversi")


x_pos = 35
xy_step = 95
y_pos = 35
obj_dx = 40 # delta x of the object, width
obj_dy = 40 # delta y of the object, height
velocity = 5

running = True
while running: # Main loop
	pg.time.delay(100)
	for event in pg.event.get(): # event are user's input
		if event.type == pg.QUIT:
			running = False

	red = (255, 0, 0)
	for J in range(3): # counter of y positions
		for I in range(3): # counter of x positions
			pg.draw.rect(win, red, (x_pos+I*xy_step, y_pos+J*xy_step, obj_dx, obj_dy))
			pg.display.update()

	keys = pg.key.get_pressed()
	if keys[pg.K_RIGHT]:
		pg.draw.rect(win, (0,0,0), (130, y_pos, obj_dx, obj_dy))
		pg.display.update()
	
pg.quit()