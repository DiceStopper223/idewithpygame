import pygame

#Initialize pygame
pygame.init()

#Set the screen size
screen = pygame.display.set_mode((800, 600))

#Set the title of the screen
pygame.display.set_caption("Text Editor")

#Set the font and font size
font = pygame.font.Font(None, 36)
number_font = pygame.font.Font(None, 36)

#Text to be displayed in the editor
text = ""

#Run the main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode == '\x08':
                text = text[:-1]
            elif event.unicode == '\r':
                text += '\n'
            else:
                text += event.unicode
    
    #Clear the screen
    screen.fill((255, 255, 255))
    
    #Get the lines of text
    lines = text.split("\n")
    
    #Render the line numbers
    line_number = 1
    for line in lines:
        text_surface = number_font.render(str(line_number), True, (192, 192, 192))
        screen.blit(text_surface, (0, (line_number - 1) * 40))
        line_number += 1
    
    #Render the text
    line_number = 1
    for line in lines:
        if "function" in line:
            text_surface = font.render(line, True, (0, 0, 255))
        else:
            text_surface = font.render(line, True, (0, 0, 0))
        screen.blit(text_surface, (50, (line_number - 1) * 40))
        line_number += 1
    
    #Update the screen
    pygame.display.update()

#Quit pygame
pygame.quit()
