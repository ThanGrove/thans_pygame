import sys, pygame, random as rnd

imgpath = 'ballimgs/'
ballimgs = (imgpath + '8-ball.png', imgpath + 'beach-ball.png', imgpath + 'rubber-ball.png',
                imgpath + 'soccer-ball.png', imgpath + 'spiked-ball.png')

class Ball:
    """A simple class to represent a ball on the screen"""
    global ballimgs

    speed = [2, 2]
    bounds = (800, 500)
    ball = None
    ballrect = None
    img = None
    diff = .005

    def __init__(self, bounds):
        rnd.seed()
        self.bounds = bounds
        sp1 = rnd.randint(1,8)
        sp2 = rnd.randint(1,8)
        self.speed = [sp1, sp2]
        print self.speed
        imgnum = rnd.randint(0, 4)
        print imgnum
        self.img = ballimgs[imgnum]
        self.ball = pygame.image.load(self.img)
        self.ballrect = self.ball.get_rect()

    def getBall(self):
        return self.ball

    def getRect(self):
        return self.ballrect

    def move(self):
        self.ballrect =self.ballrect.move(self.speed)
        if self.ballrect.left < 0 or self.ballrect.right > width:
            self.speed[0] = -self.speed[0]
        if self.ballrect.top < 0 or self.ballrect.bottom > height:
            self.speed[1] = -self.speed[1]

        diff = self.diff

        if self.speed[0] > 0:
            self.speed[0] -= diff
        elif self.speed[0] < 0:
            self.speed[0] += diff

        if self.speed[1] > 0:
            self.speed[1] -= diff
        elif self.speed[1] < 0:
            self.speed[1] += diff

        #print self.speed

        if abs(self.speed[0]) < abs(diff) and abs(self.speed[1]) < abs(diff):
            print "here"
            self.diff = -diff
            self.speed[0] = abs(self.speed[0]) + 1
            self.speed[1] = abs(self.speed[1]) + 1

if __name__ == "__main__":
    pygame.init()
    rnd.seed()
    size = width, height = 800, 500
    black = 0, 0, 0
    screen = pygame.display.set_mode(size)
    ball1 = Ball(size)
    ball2 = Ball(size)
    #ballrect = ball.get_rect()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        ball1.move()
        ball2.move()
        screen.fill(black)
        screen.blit(ball1.getBall(), ball1.getRect())
        screen.blit(ball2.getBall(), ball2.getRect())
        pygame.display.flip()
