 # Install the pygame library

import pygame
import sys
import requests

#api_url = "https://newcastle.urbanobservatory.ac.uk/data/"
#response = requests.get(api_url)
#
#if response.status_code == 200:
 #   data = response.json()
  #  # Process the data as needed
#else:

 #   print(f"Error: Unable to fetch data. Status code: {response.status_code}")


# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Laser/Sensor Simulation")

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up the laser/sensor
laser_color = (255, 0, 0)
laser_rect = pygame.Rect(width // 2 - 10, height // 2 - 50, 20, 100)

# Load the sound
pygame.mixer.init()
sound = pygame.mixer.Sound("C:\\Users\\satti\\PycharmProjects\\Smart Sound Env\\.venv\\music\\londonderry.wav")


def main():
    global laser_rect

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Check for collision with laser/sensor
        mouse_pos = pygame.mouse.get_pos()
        if laser_rect.collidepoint(mouse_pos):
            # Play the sound when laser/sensor is tripped
            sound.play()

        # Draw the screen
        screen.fill(white)
        pygame.draw.rect(screen, laser_color, laser_rect)

        pygame.display.flip()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()
