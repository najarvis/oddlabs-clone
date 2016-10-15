import random

class MidpointDisplacement(object):

    def NewMidDis(self, N):
        WIDTH = HEIGHT = (2 ** N) - 1
        to_return = [[0 for x in xrange(WIDTH)] for y in xrange(HEIGHT)]

        to_return[0][0] = random.random()
        to_return[WIDTH][0] = random.random()
        to_return[WIDTH][HEIGHT] = random.random()
        to_return[0][HEIGHT] = random.random()

        for r in xrange(N):
            for i in range(2 ** N):
                diamond(to_return, r, i, N)
                square(to_return, r, i, N)

    def diamond(self, array, recursion_depth, iteration, N):
        size = ((2 ** N) / (2 ** recursion_depth)) - 1
        tl = array[size * iteration][size * iteration]
        tr = array[size * iteration + size][size * iteration]
        br = array[size * iteration + size][size * iteration + size]
        bl = array[size * iteration][size * iteration + size]

        array[(size * iteration) / 2

    def square(self, array, recursion_depth, iteration, N):
        pass

