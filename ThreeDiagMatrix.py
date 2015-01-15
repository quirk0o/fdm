__author__ = 'beatka'


class ThreeDiagMatrix:
    MDI = 1     # Main Diagonal Index
    LSI = 2     # Left Side Index
    RSI = 3     # Right Side Index

    def __init__(self, rows):
        self.rows = rows

    def reduce(self):
        for i in range(len(self.rows) - 1):
            row = self.rows[i]
            nextRow = self.rows[i+1]
            self.divide(row, row[self.MDI])
            self.substract(self.multiply(row, nextRow[0]), nextRow)
        self.divide(self.rows[-1], self.rows[-1][self.MDI])

    def substitute(self):
        for i in reversed(range(len(self.rows) - 1)):
            self.rows[i][self.RSI] -= self.rows[i+1][self.RSI] * self.rows[i][self.LSI]
            self.rows[i][self.LSI] = 0

    def solve(self):
        self.reduce()
        self.substitute()
        return [ row[ self.RSI ] for row in self.rows ]

    def substract(self, row, fromRow):
        for k in range(2):
            fromRow[k] -= row[k+1]
        fromRow[self.RSI] -= row[self.RSI]

    def divide(self, row, num):
        for i in range(len(row)):
            row[i] /= float(num)

    def multiply(self, row, num):
        temp = []
        for x in row:
            temp.append(x*num)
        return temp