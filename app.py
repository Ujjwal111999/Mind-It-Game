import pygame
import game_config as gc

from pygame import display,event,image
from animal import Animal
from time import sleep
def find_index(x,y):
    row = y // gc.image_size
    col = x // gc.image_size
    index = row * gc.num_tiles_side + col
    return index


pygame.init()

display.set_caption('Mind It ')
screen = display.set_mode((512,512))
matched = image.load('other_assets/matched.png')

running=True
tiles = [Animal(i) for i in range(0,gc.num_tiles_total)]
current_images=[]


while running:
    current_events=event.get()
    for e in current_events:
        if e.type == pygame.QUIT:
            running=False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            index = find_index(mouse_x,mouse_y)
            if index not in current_images:
                current_images.append(index)
            if len(current_images) > 2:
                current_images = current_images[1:]
               

    
    screen.fill((255,255,255))

    total_skipped = 0

    for _,tile in enumerate(tiles):
        image_i= tile.image if tile.index in current_images else tile.box
        if not tile.skip:
            screen.blit(image_i, (tile.col * gc.image_size + gc.margin,tile.row * gc.image_size + gc.margin))
        else:
            total_skipped +=1
    if len(current_images) == 2:
        idx1, idx2 = current_images
        if tiles[idx1].name == tiles[idx2].name:
            tiles[idx1].skip = True 
            tiles[idx2].skip = True 
            sleep(0.6)
            screen.blit(matched,(0,0))
            display.flip()
            sleep(0.6)
            current_images = []

    if total_skipped ==len(tiles):
        running = False    

    display.flip()     
print("Game End!")