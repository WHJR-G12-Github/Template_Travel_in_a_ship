import pygame, sys,random

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()
width=500
height=400
screen = pygame.display.set_mode((width,height))

# Loading images
# Create an empty dictionary 'images'
images = 

# Loading the background image 'sea.png' into the 'images' dictionary under the name 'bg'. Now, 'images["bg"]' refers to the background image
images["bg"] = pygame.image.load("sea.png").convert_alpha()

# Load the 'ship.png' image on the key "ship" of 'images' dictionary
images["ship"] = pygame.image.load(         ).convert_alpha()

# Create a variable 'bgx' to hold x-axis value of background image and initialize it to zero (Eg. a=0 . Here, variable 'a' is created & initialized to zero)
bgx = 0

while True:    
    screen.fill((50,150,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Decrement the value of 'bgx' by 5 to move the background 
    bgx = 
		
    # Add code to reset 'bgx' to 0 if 'bgx' becomes less then -1000 is True
    # Check if 'bgx' is less than -1000 
    if    
	# Reset the value of 'bgx' to zero
   	bgx = 0
    # Displaying the ship image at the coordinates '[100,150]'
    screen.blit(images["ship"],[100,150]) 
		
    # Display the background image at the coordinates '[bgx,0]'
    screen.blit(         ,[bgx,0])
	
    pygame.display.update()
    clock.tick(30)
