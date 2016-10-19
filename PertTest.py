import pygame
import random
import math
import VoronoiMapGen

WIDTH, HEIGHT = 256, 256

def run():

    pygame.init()
    random.seed(0)

    screen_size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(screen_size)

    map_gen = VoronoiMapGen.mapGen()
    mid_gen = MidpointDisplacement.MidpointDisplacement()
    # base_vor = map_gen.whole_new_updated(size=(WIDTH, HEIGHT), c1=-1, c2=1, c3=0)
    base_vor = map_gen.radial_drop(map_gen.negative(map_gen.full_updated(size=(WIDTH, HEIGHT))), 1.5, 0.0)
    base_mid = mid_gen.normalize(mid_gen.NewMidDis(math.log(WIDTH) / math.log(2)))
    pert_vor = map_gen.whole_new_updated(size=(WIDTH, HEIGHT), c1=-1, c2=1, c3=0)

    main_map = pygame.PixelArray(pygame.Surface((WIDTH, HEIGHT)))
  
    magnitude = math.log(WIDTH, 2) * (WIDTH / 256)

    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            offset = int(((pert_vor[x][y] - 128) / 128.0) * magnitude)
            col = clamp(base_vor[clamp(x + offset)][clamp(y + offset)], 0, 255)
            main_map[x, y] = (col, col, col)

    to_blit = main_map.make_surface()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

            
        screen.blit(to_blit, (0, 0))

        pygame.display.update()

    pygame.quit()

def clamp(val, low=0, high=WIDTH-1):
    return max(min(high, val), low)

if __name__ == "__main__":
    run()
