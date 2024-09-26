from PIL import Image, ImageDraw
import random

VEHICLES = {"car": (80, 200), "jeep": (90, 220), "truck": (100, 280)}
class StreetGenerator:

    PROTRUDE = 5
    CAR_LENGTH = 100
    CURB_SEGMENT_HEIGHT = 20
    

    def __init__(self, streetWidth, streetHeight, traffic, vehicles):
        self.streetWidth = streetWidth
        self.streetHeight = streetHeight
        self.traffic = traffic
        self.vehicles = vehicles
    def createCurbs(self, draw, curbWidth, segmentHeight, colors=("yellow", "black")):
        current_y = 0
        color_index = 0

        # Draw alternating segments on the left curb
        while current_y < self.streetHeight:
            draw.rectangle(
                (0, current_y, curbWidth, min(current_y + segmentHeight, self.streetHeight)),
                fill=colors[color_index]
            )
            color_index = (color_index + 1) % 2  # Alternate between colors
            current_y += segmentHeight

        # Reset variables for the right curb
        current_y = 0
        color_index = 0

        # Draw alternating segments on the right curb
        while current_y < self.streetHeight:
            draw.rectangle(
                (self.streetWidth - curbWidth, current_y, self.streetWidth, min(current_y + segmentHeight, self.streetHeight)),
                fill=colors[color_index]
            )
            color_index = (color_index + 1) % 2  # Alternate between colors
            current_y += segmentHeight

    def fillLane(self, image, draw, lane):
        current_y = 30
        while current_y < image.height:
            psNoise = random.randint(0, 40)
            if self.traffic > random.random():
                vehicle = random.choice(list(self.vehicles.keys()))
                vw, vh = self.vehicles[vehicle][0], self.vehicles[vehicle][1]
                paNoise = random.randint(0, 5)
                if lane == "left":

                    draw.polygon(
                        [
                            (self.PROTRUDE + 5 + paNoise, current_y),
                            (self.PROTRUDE + 5 + paNoise + vw, current_y),
                            (self.PROTRUDE + 5 - paNoise + vw, current_y + vh),
                            (self.PROTRUDE + 5 - paNoise, current_y + vh),
                        ],
                        fill="black",
                    )
                else:
                    draw.polygon(
                        [
                            (self.streetWidth- (self.PROTRUDE + 5 + vw + paNoise), current_y),
                            (self.streetWidth - (self.PROTRUDE + 5 + paNoise), current_y),
                            (self.streetWidth - (self.PROTRUDE + 5 - paNoise), current_y + vh),
                            (self.streetWidth - (self.PROTRUDE + 5 + vw - paNoise), current_y + vh),
                        ],
                        fill="black",
                    )
                   

                current_y += vh + 5 + psNoise
            else:
                current_y += self.CAR_LENGTH + psNoise

    def createStreet(self, savePath="maps/street.png"):
        image = Image.new("RGB", (self.streetWidth, self.streetHeight), color="white")
        draw = ImageDraw.Draw(image)

        # Draw the curbs with alternating yellow and black
        self.createCurbs(draw, self.PROTRUDE, self.CURB_SEGMENT_HEIGHT)

        # Draw the middle lane marking
        # draw.line((self.streetWidth // 2, 0, self.streetWidth // 2, self.streetHeight), fill="black")

        # Fill left lane
        self.fillLane(image, draw, "left")
        # Fill right lane
        self.fillLane(image, draw, "right")

        image.save(savePath)

