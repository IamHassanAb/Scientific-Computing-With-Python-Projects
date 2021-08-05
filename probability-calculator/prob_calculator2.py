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
    count = 0
    expected_balls_lst = []
    for key,values in expected_balls.items():
        for i in range(values):
            expected_balls_lst.append(key)
    srt = sorted(expected_balls_lst)
    for i in range(num_experiments):
        ran_draw_dict = {}
        copy_hat = copy.deepcopy(hat)
        ran_draw_lst = copy_hat.draw(num_balls_drawn)
        srt2 = sorted(ran_draw_lst)
        if all(i in ran_draw_lst for i in expected_balls_lst):
            count+=1
        # for color in ran_draw_lst:
        #     ran_draw_dict[color] = ran_draw_dict.get(color, 0) + 1
        #
        # for items1, in ran_draw_dict.items():
        #     print(i)
        # print(ran_draw_dict.items())
        # for ran_draw_items in ran_draw_dict.items():
        #     for expected_balls_items in expected_balls.items():
        #         if ran_draw_items[0] == expected_balls_items[0]:
        #             # if ran_draw_items[1] == expected_balls_items[1]:
        #             print(ran_draw_items[1], expected_balls_items[1])
        #         #         count+=1
    return (1 - count/num_experiments)