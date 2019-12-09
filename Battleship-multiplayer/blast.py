import pygame
def blast(ship1,ship2,blasted):#ship1 is the imported grid
    for x in range(5):
        for y in range(5):
            if ship1[y][x] == 'S' and ship2[y+6][x] == 'Bo':#executes to True if the ship is present and opponent has dropped a bomb at the position 
                ship2[y+6][x] = 'Bl' 
                blasted += 1
    return blasted
