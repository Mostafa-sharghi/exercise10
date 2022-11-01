class elevator:
    def __init__(self, number_floor=10, current_flor=0):
        self.number_floor = number_floor
        self.current_floor = current_flor




    def move_floor(self, floor):
        while self.current_floor != floor:
            if floor > self.current_floor:
                high.upward()
            else:
                high.downward()
        print('Your current floor is :',high.current_floor)



    def upward(self):
        print('Your current floor is :', self.current_floor)
        self.current_floor +=1



    def downward(self):
        print('Your current floor is :', self.current_floor)
        while high.current_floor != 0:
            self.current_floor -=1
            print(high.current_floor)





high = elevator()
high.move_floor(7)
high.downward()