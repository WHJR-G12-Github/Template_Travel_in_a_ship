import pygame, sys,random

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()
width=500
height=400
screen = pygame.display.set_mode((width,height))

# Loading images
# Create an empty dictionary 'images'

# Loading the background image 'sea.png' into the 'images' dictionary under the name 'bg'. Now, 'images["bg"]' refers to th background image
images["bg"] = pygame.image.load("sea.png").convert_alpha()

# Load the 'ship.png' image under the name 'ship' so that 'images["ship"] refers to the ship image


# Create a variable 'bgx' to hold x-axis value of background image and initialize it to zero (Eg. a=0 . Here, variable 'a' is created & initialized to zero)


while True:    
    screen.fill((50,150,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Decrement the value of 'bgx' by 5 to move the background (Eg. a=a-1 . Here, variable 'a' is decremented by 1)
    
		
    # Add code to reset 'bgx' to 0 if 'bgx' becomes less then -1000 is true . 
    # Check using 'if' if 'bgx' is less than -1000 (Eg. if a < 5: It checks whether value of 'a' is less than 5)
    
				# Reset the value of 'bgx' to zero
   
	  # Displaying the ship image at the coordinates '[100,150]'
    screen.blit(images["ship"],[100,150]) 
		
    # Display the background image at the coordinates '[bgx,0]'
   
    pygame.display.update()
    clock.tick(30)
