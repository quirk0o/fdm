__author__ = 'beatka'


class FDM:
    range = (0, 1)

    def __init__(self, n):
        self.n = n
        self.h = 1/n

    def createEquation(self):
        with open("matrix", "w") as file:
            i, N = self.range
            while i <= N:
                file.write()


