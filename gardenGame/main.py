import pygame

pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Relaxing Garden")
clock = pygame.time.Clock()

PLOT_SIZE = 80
NUM_PLOTS = 6
PLOT_Y = 340
MARGIN = (WIDTH - (NUM_PLOTS * PLOT_SIZE)) // 2

SKY = (135, 206, 235)  # sky blue
SOIL = (101, 67, 33)    # soil brown
SEED = (60, 40, 20)     # seed brown
GREEN = (80, 170, 80) # plant green
PETAL = (255, 130, 170)  # petal pink
CENTER = (255, 220, 90)  # flower center yellow

STAGE_GROWTH_TIME = 5  # seconds for spending time in each stage before growing
MAX_STAGE = 3  # number of stages before fully grown


class Plant:
    def __init__(self):
        self.stage = 0
        self.growth_time = 0.0 #timer

    def update(self, dt): # class method to update the growth of the plant based on time
        if self.stage < MAX_STAGE: # if the plant is not fully grown
            self.growth_time += dt # increment the growth time by the time passed since the last update
            if self.growth_time >= STAGE_GROWTH_TIME: # if the growth time exceeds the threshold for the current stage
                self.stage += 1 # move to the next stage
                self.growth_time = 0.0 # reset the growth time for the next stage


plots = [None] * NUM_PLOTS # One slot per plot, initialized to None.

def plot_rect(index):
    return pygame.Rect(MARGIN + index * PLOT_SIZE, PLOT_Y, PLOT_SIZE-4, PLOT_SIZE-4)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(NUM_PLOTS):
                if plot_rect(i).collidepoint(event.pos) and plots[i] is None: #if rectangle is clicked and plot is empty
                    plots[i] = Plant()  # Plant a seed in the plot

    screen.fill(SKY)  # sky blue
    for i in range(NUM_PLOTS):
        rect = plot_rect(i)
        pygame.draw.rect(screen, SOIL, rect, border_radius = 8)  # plot
        if plots[i] is not None:
            pygame.draw.circle(screen,SEED, rect.center, 8)  # seed
    pygame.display.flip()
    clock.tick(60)

pygame.quit()