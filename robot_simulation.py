# -*- coding: utf-8 -*-
# Problem Set 3: Simulating robots
# Name: Ahmed Elsayed Abdelnaby Shehata 
# Collaborators (discussion):
# Time: started 28/12/2020 at 7.00 pm finished 
import math
import random
import ps3_visualize
import matplotlib.pyplot as plt


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room, where
    coordinates are given by floats (x, y).
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_new_position(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.get_x(), self.get_y()
        
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        
        return Position(new_x, new_y)

    def __str__(self):  
        return "Position: " + str(math.floor(self.x)) + ", " + str(math.floor(self.y))


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. Each tile
    has some fixed amount of dirt. The tile is considered clean only when the amount
    of dirt on this tile is 0.
    """
    def __init__(self, width, height, dirt_amount):
        """
        Initializes a rectangular room with the specified width, height, and 
        dirt_amount on each tile.

        width: an integer > 0
        height: an integer > 0
        dirt_amount: an integer >= 0
        """
        # initiating the variables and insuring its positive integars
        self.width=width
        self.height=height
        self.dirt_amount=dirt_amount
        self.tile_information={}
        if self.height <= 0 or self.width <= 0 or self.dirt_amount < 0 or type(self.width) != int or type(self.height) != int or type(self.dirt_amount) != int:
            raise ValueError ('Height,width and dirt amount has to be positive integrals')
        for i in range(0,width):
            for n in range(0,height):
                tile=(i,n)
                self.tile_information[tile]=self.dirt_amount
        
               
               
                

    def clean_tile_at_position(self, pos, capacity):
        """
        Mark the tile under the position pos as cleaned by capacity amount of dirt.

        Assumes that pos represents a valid position inside this room.

        pos: a Position object
        capacity: the amount of dirt to be cleaned in a single time-step
                  can be negative which would mean adding dirt to the tile

        Note: The amount of dirt on each tile should be NON-NEGATIVE.
              If the capacity exceeds the amount of dirt on the tile, mark it as 0.
        """
        position=(math.floor(pos.get_x()),math.floor(pos.get_y()))
        dirt_amount=self.tile_information[position]
        while dirt_amount>0:
          dirt_amount -= capacity 
        if dirt_amount<0:
           dirt_amount=0   
        self.tile_information[position]=dirt_amount
        
            
        

    def is_tile_cleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        
        Returns: True if the tile (m, n) is cleaned, False otherwise

        Note: The tile is considered clean only when the amount of dirt on this
              tile is 0.
        """
        tile=(math.floor(m),math.floor(n))
        if self.tile_information[tile]==0:
            result=True
        else:
            result=False
        return result
            

    def get_num_cleaned_tiles(self):
        """
        Returns: an integer; the total number of clean tiles in the room
        """
        number_of_cleaned_tile=0
        for i in self.tile_information:
            if self.tile_information[i]==0:
                number_of_cleaned_tile +=1
        return(number_of_cleaned_tile)
            
        
        
    def is_position_in_room(self,pos):
        """
        Determines if pos is inside the room.

        pos: a Position object.
        Returns: True if pos is in the room, False otherwise.
        """
        position=(math.floor(pos.get_x()),math.floor(pos.get_y()))
        if position in self.tile_information:
           result =True
        else:
            result= False
        return(result)

        
            
        
    def get_dirt_amount(self, m, n):
        """
        Return the amount of dirt on the tile (m, n)
        
        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer

        Returns: an integer
        """
        pos=(math.floor(m),math.floor(n))
        dirt_amount=self.tile_information[pos]
        return (dirt_amount)
    
    def get_num_tiles(self):
        """
        Returns: an integer; the total number of tiles in the room
        """
        # do not change -- implement in subclasses.
        raise NotImplementedError 
        
    def is_position_valid(self, pos):
        """
        pos: a Position object.
        
        returns: True if pos is in the room and (in the case of FurnishedRoom) 
                 if position is unfurnished, False otherwise.
        """
        # do not change -- implement in subclasses
        raise NotImplementedError         

    def get_random_position(self):
        """
        Returns: a Position object; a random position inside the room
        """
        # do not change -- implement in subclasses
        raise NotImplementedError        

class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times, the robot has a particular position and direction in the room.
    The robot also has a fixed speed and a fixed cleaning capacity.

    Subclasses of Robot should provide movement strategies by implementing
    update_position_and_clean, which simulates a single time-step.
    """
    def __init__(self, room, speed, capacity):
        """
        Initializes a Robot with the given speed and given cleaning capacity in the 
        specified room. The robot initially has a random direction and a random 
        position in the room.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        capacity: a positive interger; the amount of dirt cleaned by the robot 
                  in a single time-step
        """
        self.room=room
        self.speed=speed
        self.capacity=capacity
        
        


    def get_robot_position(self):
        """
        Returns: a Position object giving the robot's position in the room.
        """
        return (self.position)
        

    def get_robot_direction(self):
        """
        Returns: a float d giving the direction of the robot as an angle in
        degrees, 0.0 <= d < 360.0.
        """
        return(self.direction)

    def set_robot_position(self, pos):
        """
        Set the position of the robot to position.

        position: a Position object.
        """
        self.position=pos

    def set_robot_direction(self, direc):
        """
        Set the direction of the robot to direction.

        direction: float representing an angle in degrees
        """
        self.direction=direc

    def update_position_and_clean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new random position (if the new position is invalid, 
        rotate once to a random new direction, and stay stationary) and mark the tile it is on as having
        been cleaned by capacity amount. 
        """
        # do not change -- implement in subclasses
        raise NotImplementedError

#%%
# === Problem 2
class EmptyRoom(RectangularRoom):
    """
    An EmptyRoom represents a RectangularRoom with no furniture.
    """  
    def get_num_tiles(self):
        """
        Returns: an integer; the total number of tiles in the room
        """
        number_of_tiles=len(self.tile_information)
        return number_of_tiles
        
        
    def is_position_valid(self, pos):
        """
        pos: a Position object.
        
        Returns: True if pos is in the room, False otherwise.
        """
        return self.is_position_in_room(pos)
        
    def get_random_position(self):
        """
        Returns: a Position object; a valid random position (inside the room).
        """
        random_position=random.choice(list(self.tile_information))
        return(random_position)
    
# a=RectangularRoom(5,5, 4)
# c=EmptyRoom(5,5,4)
# print(c.get_num_tiles())
# b=a.clean_tile_at_position(Position(1,1), 4)
# b=a.clean_tile_at_position(Position(2,2), 2)
# print(a.is_tile_cleaned( 2, 2))
# print(a.is_tile_cleaned( 3, 3))
# print(a.get_num_cleaned_tiles())
# random_position=c.get_random_position()
# print(random_position)
class FurnishedRoom(RectangularRoom):
    """
    A FurnishedRoom represents a RectangularRoom with a rectangular piece of 
    furniture. The robot should not be able to land on these furniture tiles.
    """
    def __init__(self, width, height, dirt_amount):
        """ 
        Initializes a FurnishedRoom, a subclass of RectangularRoom. FurnishedRoom
        also has a list of tiles which are furnished (furniture_tiles).
        """
        # This __init__ method is implemented for you -- do not change.
        
        # Call the __init__ method for the parent class
        RectangularRoom.__init__(self, width, height, dirt_amount)
        # Adds the data structure to contain the list of furnished tiles
        self.furniture_tiles = []
        
    def add_furniture_to_room(self):
        """
        Add a rectangular piece of furniture to the room. Furnished tiles are stored 
        as (x, y) tuples in the list furniture_tiles 
        
        Furniture location and size is randomly selected. Width and height are selected
        so that the piece of furniture fits within the room and does not occupy the 
        entire room. Position is selected by randomly selecting the location of the 
        bottom left corner of the piece of furniture so that the entire piece of 
        furniture lies in the room.
        """
        # This addFurnitureToRoom method is implemented for you. Do not change it.
        furniture_width = random.randint(1, self.width - 1)
        furniture_height = random.randint(1, self.height - 1)

        # Randomly choose bottom left corner of the furniture item.    
        f_bottom_left_x = random.randint(0, self.width - furniture_width)
        f_bottom_left_y = random.randint(0, self.height - furniture_height)

        # Fill list with tuples of furniture tiles.
        for i in range(f_bottom_left_x, f_bottom_left_x + furniture_width):
            for j in range(f_bottom_left_y, f_bottom_left_y + furniture_height):
                self.furniture_tiles.append((i,j))             
        
    def is_tile_furnished(self, m, n):
        """
        Return True if tile (m, n) is furnished.
        """
        position=(m,n)
        if position in self.furniture_tiles:
          result= True
        else:
            result=False
        return (result)
             
        
    def is_position_furnished(self, pos):
        """
        pos: a Position object.

        Returns True if pos is furnished and False otherwise
        """
        x_coordinate=math.floor(pos.get_x())
        y_coordinate=math.floor(pos.get_y())
        return(self.is_tile_furnished(x_coordinate,y_coordinate))
        
    def is_position_valid(self, pos):
        """
        pos: a Position object.
        
        returns: True if pos is in the room and is unfurnished, False otherwise.
        """
        position_exist=self.is_position_in_room(pos) 
        has_furniture=self.is_position_furnished(pos)
        if position_exist==True and has_furniture==False:
            result=True
        else:
            result=False
        return(result)
        
    def get_num_tiles(self):
        """
        Returns: an integer; the total number of tiles in the room that can be accessed.
        """
        number_of_furnishried_tiles=len(self.furniture_tiles)
        number_of_tiles=len(self.tile_information)
        number_of_available_tiles=number_of_tiles-number_of_furnishried_tiles
        return number_of_available_tiles
        
    def get_random_position(self):
        """
        Returns: a Position object; a valid random position (inside the room and not in a furnished area).
        """
        random_position=random.choice(list(self.tile_information))
        return(random_position)
    

# === Problem 3
### the StandardRobot parent class is robot so it means that we have the speed ,room and capacity
class StandardRobot(Robot):
    
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall or furtniture, it *instead*
    chooses a new direction randomly.
    """
    def update_position_and_clean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new random position (if the new position is invalid, 
        rotate once to a random new direction, and stay stationary) and clean the dirt on the tile
        by its given capacity. 
        """
        #first we need to get the robot current position from the parent class Robot 
        # to do so we need to start the robot at a random position in the room using the attributes 
        # get_random_position from the room 
        the_room=self.room
        random_position=the_room.get_random_position()
        # to set the robot at a random position at the beginning of the simulation 
        current_position=Position(random_position[0],random_position[1])
        # create a list from 0 to 360 to choose a random angle from 
        direction_angle=[]
        for i in range (361):
            direction_angle.append(i)
        # set a random angle to move in 
        random_angle=random.choice(direction_angle)
        new_position=current_position.get_new_position(random_angle,self.speed)
        # check if the position valid and that means it is in the room and non_furnishried
        is_the_position_valid=the_room.is_position_valid(new_position)
        if is_the_position_valid ==True:
               current_position=new_position
            # set the robot new position and new direction
               the_room.clean_tile_at_position(current_position,self.capacity)
               self.set_robot_position(current_position)
               self.set_robot_direction(random_angle)
        
            
# Uncomment this line to see your implementation of StandardRobot in action!
#test_robot_movement(StandardRobot, EmptyRoom)
#test_robot_movement(StandardRobot, FurnishedRoom)

####### Important to run animation of the simulation use run_simulation_anim
def run_simulation_anim(num_robots, speed, capacity, width, height, dirt_amount, min_coverage, num_trials,
                  robot_type):
    """
    Runs num_trials trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction min_coverage of the room.

    The simulation is run with num_robots robots of type robot_type, each       
    with the input speed and capacity in a room of dimensions width x height
    with the dirt dirt_amount on each tile.
    
    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    capacity: an int (capacity >0)
    width: an int (width > 0)
    height: an int (height > 0)
    dirt_amount: an int
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                FaultyRobot)
    """
    # create an empty room using the width,the height and the dirt_amount and empty trial results list
    trial_results_time=[]
    # doing the simulation for a number of trials 
    for trial in range(num_trials):
       anim = ps3_visualize.RobotVisualization(num_robots, width, height,False,.1)
       the_room=EmptyRoom(width, height, dirt_amount)
    # create a standard type robot 
       the_Robot=robot_type(the_room, speed, capacity)
       all_Robots=[the_Robot]* num_robots
    #the number of tile cleaned divided by the total number of tiles in the room 
       coverage=0
       time_taken=0
       while coverage < min_coverage:
        for index,robot in enumerate(all_Robots):
          time_taken +=1
          robot.update_position_and_clean()
    #it has to be float to make sure it can give us a fraction 
          coverage=float(the_room.get_num_cleaned_tiles()/the_room.get_num_tiles())
          anim.update(the_room,all_Robots)
          if coverage == min_coverage:
             break
       trial_results_time.append(time_taken)
    avg_time_taken=sum(trial_results_time)/len(trial_results_time)
    anim.done()
    return(trial_results_time,avg_time_taken)
# this to run simulation without animation to see the robot movement
def run_simulation(num_robots, speed, capacity, width, height, dirt_amount, min_coverage, num_trials,
                  robot_type):
    """
    Runs num_trials trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction min_coverage of the room.

    The simulation is run with num_robots robots of type robot_type, each       
    with the input speed and capacity in a room of dimensions width x height
    with the dirt dirt_amount on each tile.
    
    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    capacity: an int (capacity >0)
    width: an int (width > 0)
    height: an int (height > 0)
    dirt_amount: an int
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                FaultyRobot)
    """
    # create an empty room using the width,the height and the dirt_amount and empty trial results list
    trial_results_time=[]
    # doing the simulation for a number of trials 
    for trial in range(num_trials):
       the_room=EmptyRoom(width, height, dirt_amount)
    # create a standard type robot 
       the_Robot=robot_type(the_room, speed, capacity)
       all_Robots=[the_Robot]* num_robots
    #the number of tile cleaned divided by the total number of tiles in the room 
       coverage=0
       time_taken=0
       while coverage < min_coverage:
        for index,robot in enumerate(all_Robots):
          time_taken +=1
          robot.update_position_and_clean()
    #it has to be float to make sure it can give us a fraction 
          coverage=float(the_room.get_num_cleaned_tiles()/the_room.get_num_tiles())
          if coverage == min_coverage:
             break
       trial_results_time.append(time_taken)
    avg_time_taken=sum(trial_results_time)/len(trial_results_time)
    return(trial_results_time,avg_time_taken)

(simulation_result_1,avg_time_1)=run_simulation(1, 1.0, 1, 5, 5, 3, 1.0, 50, StandardRobot)
(simulation_result_9,avg_time_9)=run_simulation(1, 1.0, 1, 5, 5, 3, 0.9, 50, StandardRobot)
(simulation_result_8,avg_time_8)=run_simulation(1, 1.0, 1, 5, 5, 3, 0.8, 50, StandardRobot)
(simulation_result_1_robot,avg_time_1_robot)=run_simulation(1, 1.0, 1, 20, 20, 3, 0.5, 50, StandardRobot)
##############################################################################################
##############################################################################################
### to run simulation un comment the next line and comment what after 
(simulation_result_3_robots,avg_time_3_robots)=run_simulation_anim(5, 1.0, 1, 20, 20, 3, 0.5, 1, StandardRobot)
# print ('avg time steps: ' + str(avg_time_1))
# print ('avg time steps: ' + str(avg_time_9))
# print ('avg time steps: ' + str(avg_time_8))
# print ('avg time steps: ' + str(avg_time_1_robot))
# #### here I will play with the simulation result plot the time taken in each trial for the 5*5 room for 50 trials 
# time_taken_1=simulation_result_1
# time_taken_9=simulation_result_9
# time_taken_8=simulation_result_8
# number_of_trials=list(range(1,len(time_taken_1)+1))
# plt.plot(number_of_trials,time_taken_1)
# plt.plot(number_of_trials,time_taken_9)
# plt.plot(number_of_trials,time_taken_8)
# plt.legend(['to clean 100% of the room area ','to clean 90% of the room area','to clean 80% of the room area'])
# plt.xlabel('time_taken')
# plt.ylabel('number_of_trials')
# plt.title('50 trial to clean 80% compared to 90% and 100% of a 5*5 room')
# plt.figure()
# #this plot to compare the avaearge time_taken to clean 80,90 and 100% percent of the room 
# avg_time=[avg_time_1,avg_time_9,avg_time_8]
# robots=[1,.9,.8]
# plt.plot(robots,avg_time)
# plt.xlabel('percentage of cleanage')
# plt.ylabel('time taken to clean the room ')
# plt.title('compare between the time taken to clean 80 % ,90 % and 100 percent of the room ')

#plt.show()
