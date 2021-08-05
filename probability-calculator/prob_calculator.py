import copy
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



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    countFailed = 0
    copy_hat_contents = copy.copy(hat.contents)
    for i in range(num_experiments):
        drawn_balls_lst = hat.draw(num_balls_drawn)
        for i in expected_balls.keys():
            count = 0
            for j in range(len(drawn_balls_lst)):
                if drawn_balls_lst[j] == i:
                    count = count + 1
            if count < expected_balls.get(i):
                countFailed = countFailed + 1
                break
        hat.contents = copy.copy(copy_hat_contents)

    return 1 - countFailed / num_experiments
