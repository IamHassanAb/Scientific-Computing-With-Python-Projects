import random
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**balls):
        self.contents = []
        self.balls = balls
        for k,v in balls.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self,balls_to_draw):
        #Draws No. of balls at random
        #If the number of balls to draw exceeds the available quantity, return all the balls.
        content = self.contents
        balls_drawn = []
        if balls_to_draw>=len(content):
            return content
        for rn in range(balls_to_draw):
            ball = random.choice(content)
            content.remove(ball)
            balls_drawn.append(ball)
        content = self.contents
        return balls_drawn

hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
print(hat.draw(20))
print(len(hat.contents))