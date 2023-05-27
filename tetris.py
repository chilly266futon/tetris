import pygame as pg
import random, time, sys
from pygame.locals import *

fps = 25
window_w, window_h = 600, 500  # ширина и высота окна
block = 20
cup_h, cup_w = 20, 10  # высота и ширина игрового поля
side_freq, down_freq = 0.15, 0.1  # время на перемещение фигуры в сторону и вниз, когда клавиша нажата
side_margin = int((window_w - cup_w * block) / 2)  # Расстояние между боковыми сторонами окна и игровым полем
top_margin = window_h - (cup_h * block) - 5  # Расстояние между верхней границей окна и игровым полем    clock.tick(FPS)