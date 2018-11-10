import pygame
from grouper import Grouper
from brick import Brick



class Level:

    def __init__(self, screen, solids, bricks):
        self.screen = screen
        self.grouper = Grouper
        self.brick = Brick
        self.bricks = bricks
        self.background = pygame.image.load('images/background.png')
        self.rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, (self.rect.right * 3, self.rect.bottom * 3))
        self.rect = self.background.get_rect()
        self.solids = solids
        # Ground
<<<<<<< HEAD
        self.solids.add(self.grouper(0 * 3, 200 * 3, 1103 * 3, 22 * 3))
        self.solids.add(self.grouper(1136 * 3, 200 * 3, 239 * 3, 22 * 3))
        self.solids.add(self.grouper(1424 * 3, 200 * 3, 1023 * 3, 22 * 3))
        self.solids.add(self.grouper(2480 * 3, 200 * 3, 911 * 3, 22 * 3))
=======
        solids.add(self.grouper(0 * 3, 200 * 3, 1103 * 3, 22 * 3))
        solids.add(self.grouper(1136 * 3, 200 * 3, 239 * 3, 22 * 3))
        solids.add(self.grouper(2480 * 3, 200 * 3, 911 * 3, 22 * 3))
>>>>>>> origin/master
        # Small pipe
        solids.add(self.grouper(448 * 3, 168 * 3, 31 * 3, 32 * 3))
        solids.add(self.grouper(2608 * 3, 168 * 3, 31 * 3, 32 * 3))
        solids.add(self.grouper(2864 * 3, 168 * 3, 31 * 3, 32 * 3))
        # Med Pipe
        solids.add(self.grouper(608 * 3, 152 * 3, 31 * 3, 48 * 3))
        # Large Pipe
<<<<<<< HEAD
        self.solids.add(self.grouper(736 * 3, 136 * 3, 31 * 3, 64 * 3))
        self.solids.add(self.grouper(912 * 3, 136 * 3, 31 * 3, 64 * 3))
<<<<<<< HEAD
        # Solid Bricks
        self.solids.add(self.grouper(2144 * 3, 184 * 3, 63 * 3, 64 * 3))
        self.solids.add(self.grouper((2144 + 16 * 1) * 3, (184 - 16 * 1) * 3, (63 -16 * 1) * 3, 64 * 3))
        self.solids.add(self.grouper((2144 + 16 * 2) * 3, (184 - 16 * 2) * 3, (63 - 16 * 2) * 3, 64 * 3))
        self.solids.add(self.grouper((2144 + 16 * 3) * 3, (184 - 16 * 3) * 3, (63 - 16 * 3) * 3, 64 * 3))
        self.solids.add(self.grouper(2240 * 3, 184 * 3, 63 * 3, 64 * 3))
        self.solids.add(self.grouper(2240 * 3, (184 - 16 * 1) * 3, (16 + 16 * 2) * 3, 64 * 3))
        self.solids.add(self.grouper(2240 * 3, (184 - 16 * 2) * 3, (16 + 16 * 1) * 3, 64 * 3))
        self.solids.add(self.grouper(2240 * 3, (184 - 16 * 3) * 3, (16 + 16 * 0) * 3, 64 * 3))
        self.solids.add(self.grouper(2368 * 3, 184 * 3, 79 * 3, 64 * 3))
        self.solids.add(self.grouper((2368 + 16 * 1) * 3, (184 - 16 * 1) * 3, (79 - 16 * 1) * 3, 64 * 3))
        self.solids.add(self.grouper((2368 + 16 * 2) * 3, (184 - 16 * 2) * 3, (79 - 16 * 2) * 3, 64 * 3))
        self.solids.add(self.grouper((2368 + 16 * 3) * 3, (184 - 16 * 3) * 3, (79 - 16 * 3) * 3, 64 * 3))
        self.solids.add(self.grouper(2480 * 3, 184 * 3, 63 * 3, 64 * 3))
        self.solids.add(self.grouper(2480 * 3, (184 - 16 * 1) * 3, (16 + 16 * 2) * 3, 64 * 3))
        self.solids.add(self.grouper(2480 * 3, (184 - 16 * 2) * 3, (16 + 16 * 1) * 3, 64 * 3))
        self.solids.add(self.grouper(2480 * 3, (184 - 16 * 3) * 3, (16 + 16 * 0) * 3, 64 * 3))
        self.solids.add(self.grouper((2896 + 16 * 0) * 3, (184 - 16 * 0) * 3, (16 * 9) * 3, 64 * 3))
        self.solids.add(self.grouper((2896 + 16 * 1) * 3, (184 - 16 * 1) * 3, (16 * 8) * 3, 64 * 3))
        self.solids.add(self.grouper((2896 + 16 * 2) * 3, (184 - 16 * 2) * 3, (16 * 7) * 3, 64 * 3))
        self.solids.add(self.grouper((2896 + 16 * 3) * 3, (184 - 16 * 3) * 3, (16 * 6) * 3, 64 * 3))
        self.solids.add(self.grouper((2896 + 16 * 4) * 3, (184 - 16 * 4) * 3, (16 * 5) * 3, 64 * 3))
        self.solids.add(self.grouper((2896 + 16 * 5) * 3, (184 - 16 * 5) * 3, (16 * 4) * 3, 64 * 3))
        self.solids.add(self.grouper((2896 + 16 * 6) * 3, (184 - 16 * 6) * 3, (16 * 3) * 3, 64 * 3))
        self.solids.add(self.grouper((2896 + 16 * 7) * 3, (184 - 16 * 7) * 3, (16 * 2) * 3, 64 * 3))
        self.solids.add(self.grouper(3168 * 3, 184 * 3, 16 * 3, 16 * 3))
=======
        solids.add(self.grouper(736 * 3, 136 * 3, 31 * 3, 64 * 3))
        solids.add(self.grouper(912 * 3, 136 * 3, 31 * 3, 64 * 3))
>>>>>>> origin/master
=======
>>>>>>> parent of a408614... update
        # Regular Bricks
        self.bricks.add(self.brick(320 * 3, 144 * 3, 1))
        self.bricks.add(self.brick(352 * 3, 144 * 3, 1))
        self.bricks.add(self.brick(384 * 3, 144 * 3, 1))

    def blitme(self):
        self.screen.blit(self.background, self.rect)
        self.bricks.draw(self.screen)
