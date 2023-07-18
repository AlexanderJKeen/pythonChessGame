# This is our driver file. It will be responcible for handling user input and displaying the current GameState object.

import pygame as p

import chessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

#to load images I will initialize a global dictionary of images. 
#this will be called exactly once in the main

def loadImages():
    pieces =["wP", "bP", "wR","bR", "wB", "bB", "wN", "bN", "wQ", "bQ", "wK", "bK"]
    # Usin this for loop and the dictionary I can access an image by typing IMAGE[dictionary]
    for piece in pieces:
        IMAGES[piece] =p.image.load("assets/" +piece+ ".png")