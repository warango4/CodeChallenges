'''REFERENCES
https://www.codewars.com/kata/58905bfa1decb981da00009e/train/python
https://github.com/newtonsspawn/codewars_challenges/blob/master/Python/3%20kyu/The%20Lift/dinglemouse.py
'''


class Dinglemouse(object):
    
    def __init__(self, queues, capacity):
        self.queues = list(map(list, queues))
        self.capacity = capacity
        self.passengers = []
    
    def theLift(self):
        floors = len(self.queues)
        floors_visited = [0]
        
        def empty(queues):
            '''Check if the queue of passengers is not empty'''
            try:
                return all(map(empty, queues))
            except:
                return False

        def up_or_down(start, direction, floors, floors_visited):
            # If I'm coming up, I have to have all the floors of the building
            if direction == 'up': floors = [i for i in range(start, floors)]
            #Else, I have to go to the first floor
            else: floors = [i for i in range (start, -1, -1)]

            for floor in floors:
                # Assume you don't have to stop
                stop = False
                floors_to_remove = []
                
                # If current floor is in the list where the passengers have to go, stop and remove floor.
                if floor in self.passengers:
                    stop = True
                    self.passengers = [i for i in self.passengers if i != floor]
                # For each passenger in the current floor
                for passenger in self.queues[floor]:
                    # If direction is up and the passenger goes to a higher floor than the current one
                    # Stop and add the passenger if there is still some capacity
                    # Save the passengers to remove from the list of passengers of each floor because they were already carried in the lift
                    if direction == 'up':
                        if passenger > floor:
                            stop = True
                            if len(self.passengers) < self.capacity:
                                self.passengers.append(passenger)
                                floors_to_remove.append(passenger)
                    # If direction is down and the passenger goes to a lower floor than the current one
                    # Stop and add the passenger if there is still some capacity
                    # Save the passengers to remove from the list of passengers of each floor because they were already carried in the lift
                    else:
                        if passenger < floor:
                            stop = True
                            if len(self.passengers) < self.capacity:
                                self.passengers.append(passenger)
                                floors_to_remove.append(passenger)
                
                # Remove the passengers which have already been carried in the lift
                for passenger in floors_to_remove:
                    self.queues[floor].remove(passenger)
                
                # If the lift stopped in the current floor and the last visited is not the current one, add it
                if stop and (floors_visited[-1] != floor):
                    floors_visited.append(floor)
                
                # Check if there are still passengers
                if not empty(self.passengers):
                    continue
                elif empty(self.queues):
                    # Go back the the first floor and end 
                    if floors_visited[-1] != 0: floors_visited.append(0)
                    break
                # Go up or down if there are no more floors to each way respectively
                elif (direction == 'up' and empty(self.queues[floor + 1:])): up_or_down(floor, 'down', floors, floors_visited)
                elif (direction == 'down' and empty(self.queues[:floor])): up_or_down(floor, 'up', floors, floors_visited)
            
            return
        
        up_or_down(floors_visited[-1], 'up', floors, floors_visited)

        return floors_visited

if __name__ == '__main__':
    lift = Dinglemouse(((), (), (5, 5, 5), (), (), (), ()), 5)
    print(lift.theLift())

    lift = Dinglemouse(((), (), (1, 1), (), (), (), ()), 5)
    print(lift.theLift())

    lift = Dinglemouse(((), (3,), (4,), (), (5,), (), ()), 5)
    print(lift.theLift())

    lift = Dinglemouse(((), (0,), (), (), (2,), (3,), ()), 5)
    print(lift.theLift())