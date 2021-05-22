from turtle import Turtle
from random import randrange, choice

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def add_car():
    tim = Turtle()
    tim.shape("square")
    tim.penup()
    tim.shapesize(stretch_len=2, stretch_wid=0.5)
    tim.setpos(240, randrange(-220, 220, 20))
    tim.setheading(180)
    tim.color(choice(colors))
    return tim


class Car(Turtle):
    car_speed = 3
    count = 1

    def __init__(self):
        super().__init__()
        self.hideturtle() # Hide turtle created by self object , if not done it will display turtle at (0, 0)
        self.cars = []

    # def add_car(self):
    #     if Car.count % 9 == 0:
    #         self.cars.append(add_car())
    #     Car.count += 1

    # Below add car & checks if new car object created does not collide with any other car at distance of
    # 50 px.
    def add_car(self):
        car_add = True
        car_obj = add_car()
        for car in self.cars:
            if car.distance(car_obj) < 50:
                car_obj.clear()
                car_obj.hideturtle()
                car_add = False
                break
        if car_add:
            self.cars.append(car_obj)

    def remove_car(self, car):
        # Not necessary but if removed will reduce number of obj. in list hence will speed up 'for' loop.
        if car.xcor() < - 300:
            car.clear()
            car.hideturtle()
            self.cars.remove(car)

    def move_car(self, car):
        car.fd(Car.car_speed)
