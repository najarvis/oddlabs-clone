import pygame
import MidpointDisplacement

def run():
    pygame.init()

    N = 8
    img_size = (2 ** N, 2 ** N)

    to_save = pygame.PixelArray(pygame.Surface(img_size))
    height_array = MidpointDisplacement.MidpointDisplacement().NewMidDis(N)

    for y in range(2 ** N):
        for x in range(2 ** N):
            col = max(min(height_array[x][y] * 255, 255), 0)
            to_save[x, y] = (col, col, col)

    pygame.image.save(to_save.make_surface(), "DisplacementTest.png")

if __name__ == "__main__":
    run()
