import env
import sensors
import pygame
import time

from streetGenerator import VEHICLES, StreetGenerator

# Example usage
streetWidth = 600
streetHeight = 800

street_generator = StreetGenerator(streetWidth, streetHeight, 0.5, VEHICLES)
street_generator.createStreet()

environment = env.buildEnvironment((800, 600))
environment.originalMap = environment.map.copy()
laser = sensors.LaserSensor(500, environment.originalMap, uncertainity=(0.5, 0.01))
environment.map.fill((0, 0, 0))
environment.infomap = environment.map.copy()

# Create a camera to highlight where the sensor is currently
camera = pygame.Rect(0, 0, 50, 50)
camera.center = (streetWidth // 2, streetHeight)

running = True
start_time = time.perf_counter()

y = streetHeight

# Do all the computations first without rendering each frame
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    position = (streetWidth // 2, y)
    laser.position = position
    sensor_data = laser.sense()
    environment.dataStorage(sensor_data)

    y -= 5
    if y < 0:
        break

    camera.center = position

end_time = time.perf_counter()

# After all computations are done, render once
environment.render()
environment.map.blit(environment.infomap, (0, 0))
pygame.display.update()

# Save the resulting map as an image
pygame.image.save(environment.map, "map.png")

pygame.quit()

print(f"Time taken: {(end_time - start_time) * 1000:.2f} milliseconds")
