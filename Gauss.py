__author__ = 'beatka'

from ThreeDiagMatrix import ThreeDiagMatrix
import numpy


def loadEquation(fileName):
    with open(fileName, "r") as file:
        n = fileLen(file)
        rows = numpy.zeros((n, 4))
        for i, line in enumerate(file):
            for k in range(4):
                rows[i][k] = float(line.split()[k])
    return (rows, n)


def fileLen(file):
    for i, line in enumerate(file):
        pass
    file.seek(0)
    return i+1

if __name__ == '__main__':
    (rows, n) = loadEquation("matrix")
    a = numpy.zeros((n, n))
    b = numpy.zeros((n, 1))
    for i, row in enumerate(rows):
        a[i][i-1] = row[0]
        a[i][i] = row[1]
        if(i < n-1): a[i][i+1] = row[2]
        b[i] = row[3]
    M = ThreeDiagMatrix(rows)
    X = M.solve()
    print X
    print M.rows

    x = numpy.linalg.solve(a, b)
    print x
