####################### Task 1


# import pygame
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# pygame.init()
# screen = pygame.display.set_mode([800, 600])
# pygame.display.set_caption('Fly')
# clock = pygame.time.Clock()
# pygame.display.update()
# background_position = [0, 0]
# player_image = pygame.image.load("/Users/dante/Documents/pic1.png").convert()
# player_image.set_colorkey(BLACK)
 
# done = False
 
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True            
 
 
#     player_position = pygame.mouse.get_pos()
#     x = player_position[0]
#     y = player_position[1]
#     screen.fill((0, 0, 0))
#     screen.blit(player_image, [x, y])
#     pygame.display.flip()
#     clock.tick(60)


# pygame.quit()

########################## Task 2


# from tkinter import *
# from random import choice
# root = Tk()
# root.geometry('800x600')
# root.title('Relax')
# c = Canvas(root,bg='DeepSkyBlue2')
# c.pack(fill=BOTH,expand=1)
# colors = ['red','orange','yellow','green','pink']
# ball = c.create_oval(375,275,425,325, fill = choice(colors), width=0)
# ball_x_move = int(choice(['1', '-1']))
# ball_y_move = int(choice(['1', '-1']))



# def move_ball():
#     c.move(ball, ball_x_move, ball_y_move)
   
   
# def coords_check():
#     global ball_x_move, ball_y_move
#     x = int(c.coords(ball)[0]) + 25
#     y = int(c.coords(ball)[3]) - 25
        
#     if x > 775 and ball_x_move == 1 and ball_y_move == 1:
#         ball_x_move = -1
#         ball_y_move = 1     
#     if x > 775 and ball_x_move == 1 and ball_y_move == -1:
#         ball_x_move = -1
#         ball_y_move = -1
#     if x < 25 and ball_x_move == -1 and ball_y_move == 1:
#         ball_x_move = 1
#         ball_y_move = 1
#     if x < 25 and ball_x_move == -1 and ball_y_move == -1:
#         ball_x_move = 1
#         ball_y_move = -1
#     if y > 575 and ball_x_move == 1 and ball_y_move == 1:
#         ball_x_move = 1
#         ball_y_move = -1
#     if y > 575 and ball_x_move == -1 and ball_y_move == 1:
#         ball_x_move = -1
#         ball_y_move = -1
#     if y < 25 and ball_x_move == 1 and ball_y_move == -1:
#         ball_x_move = 1
#         ball_y_move = 1  
#     if y < 25 and ball_x_move == -1 and ball_y_move == -1:
#         ball_y_move = -1
#         ball_y_move = 1
        

# def main():
#     move_ball()
#     coords_check()
#     root.after(10, main)
    
        
# main()     
# mainloop()