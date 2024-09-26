import pygame
import math
import numpy as np


def uncertainity(distance, angle, sigma):
    mean = np.array([distance, angle])
    covariance = np.diag(sigma ** 2)
    distance, angle = np.random.multivariate_normal(mean, covariance)
    distance = distance if distance > 0 else 0
    angle = angle if angle > 0 else 0
    return [distance, angle]

class LaserSensor:
    def __init__(self, Range, map, uncertainity):
        self.range = Range
        self.speed = 4
        self.sigma = np.array([uncertainity[0], uncertainity[1]])
        self.position = np.array([0, 0])
        self.map = map
        self.w, self.h = pygame.display.get_surface().get_size()
        self.sensedObstacles = []
    
    def distance(self, obstacle):
        px = (obstacle[0] - self.position[0]) ** 2
        py = (obstacle[1] - self.position[1]) ** 2
        return math.sqrt(px + py)
    
    def sense(self, position = None):
        if position is not None:
            self.position = position
        data = []
        x1, y1 = self.position[0], self.position[1]
        for angle in np.linspace(0, 2 * math.pi, 60, False):
            x2 = x1 + self.range * math.cos(angle)
            y2 = y1 - self.range * math.sin(angle)
            for i in range(0, 100):
                u = i / 100
                x = int(x2 * u + x1 * (1 - u))
                y = int(y2 * u + y1 * (1 - u))
                if 0 < x < self.w and 0 < y < self.h:
                    color = self.map.get_at((x, y))
                    if (color[0], color[1], color[2]) == (0, 0, 0):
                        distance = self.distance((x,y))
                        output = uncertainity(distance, angle, self.sigma)
                        output.append(self.position)

                        data.append(output)
                        break
        if len(data) > 0:
            return data
        else:
            return False

