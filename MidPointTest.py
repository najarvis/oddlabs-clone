import pygame
import MidpointDisplacement

def run():
    pygame.init()

    N = 8
    img_size = (2 ** N, 2 ** N)

    to_save = pygame.Surface(img_size)
    MidGen = MidpointDisplacement.MidpointDisplacement()
    height_array = MidGen.normalize(MidGen.NewMidDis(N))

    to_save.lock()
    for y in range(2 ** N):
        for x in range(2 ** N):
            col = max(min(height_array[x][y] * 255, 255), 0)

            to_save.set_at((x, y), (col, col, col))
    to_save.unlock()

    pygame.image.save(to_save, "DisplacementTest.png")

if __name__ == "__main__":
    run()
