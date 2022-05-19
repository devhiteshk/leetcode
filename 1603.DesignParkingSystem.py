class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.Park = [big, medium, small]
        

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.Park[0] == 0:
                return False
            else:
                self.Park[0] -= 1
                return True
            
        if carType == 2:
            if self.Park[1] == 0:
                return False
            else:
                self.Park[1] -= 1
                return True
            
        if carType == 3:
            if self.Park[2] == 0:
                return False
            else:
                self.Park[2] -= 1
                return True
        