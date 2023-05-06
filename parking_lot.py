class ParkingLot:

    # here we are defining level a and level b. having them as none as any parking spots can be taken coz empty.
    def __init__(self):
        self.level_a = [None] * 20
        self.level_b = [None] * 20


    #  this method assign_parking_spot takes in the value of the vehicle no as input and then,
    #  checks if we have any empty space in both the levels,
    #  if available it assigns the spot otherwise return parking lot being full
    def assign_parking_spot(self, vehicle_number):
        for i, spot in enumerate(self.level_a):
            if spot is None:
                self.level_a[i] = vehicle_number
                return {'level': 'a', 'spot': i + 1}
        for i, spot in enumerate(self.level_b):
            if spot is None:
                self.level_b[i] = vehicle_number
                return {'level': 'b', 'spot': i + 21}
        return 'Cannot park as all the spots are taken on both levels'


    # this method retrieve_parking_spot checks if the vehicle no that is provided is present in the parking or not
    # if present it return the level and the spot otherwise asks to check the vehicle no as it's no present
    def retrieve_parking_spot(self, vehicle_number):
        if vehicle_number in self.level_a:
            spot = self.level_a.index(vehicle_number)
            return {'level': 'a', 'spot': spot + 1}
        elif vehicle_number in self.level_b:
            spot = self.level_b.index(vehicle_number)
            return {'level': 'b', 'spot': spot + 21}
        else:
            return 'Cannot find vehicle in the parking, can you please check if you have entered the correct vehicle no'


# here in the main we're giving option on the terminal to the user to either assign or retrieve the car in the parking
# by entering 1 you can get a parking spot for a vehicle if any spot is empty
# by entering 2 you can get the parking spot on which you've parked the car
# by entering 3 you can exit it

if __name__ == '__main__':
    parking_lot = ParkingLot()
    while True:
        print('Enter 1 to assign a parking spot')
        print('Enter 2 to retrieve a parking spot')
        print('Enter 3 to exit')
        choice = input()
        if choice == '1':
            vehicle_number = input('Enter vehicle number: ')
            result = parking_lot.assign_parking_spot(vehicle_number)
            print(result)
        elif choice == '2':
            vehicle_number = input('Enter vehicle number: ')
            result = parking_lot.retrieve_parking_spot(vehicle_number)
            print(result)
        elif choice == '3':
            break
        else:
            print('Invalid choice')
