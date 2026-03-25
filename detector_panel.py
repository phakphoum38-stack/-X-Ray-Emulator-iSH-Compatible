import random

class DetectorPanel:

    def __init__(self):
        self.width = 128
        self.height = 128

    def capture(self, photons):

        image = []

        for y in range(self.height):

            row = []

            for x in range(self.width):

                value = random.randint(0, photons//100)

                row.append(value)

            image.append(row)

        return image
