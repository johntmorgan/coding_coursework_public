# definition of enumerations used in elevator system
class ElevatorState(enum.Enum):
  IDLE = 1
  UP = 2
  DOWN = 3

class Direction(enum.Enum):
  UP = 1
  DOWN = 2

class DoorState(enum.Enum):
  OPEN = 1
  CLOSE = 2

from abc import ABC, abstractmethod
class Button(ABC):
    def __init__(self, status):
        self.__status = status

    def press_down():
        None

    @abstractmethod
    def is_pressed(self):
        pass

class HallButton(Button):
    def __init__(self, button_sign):
        self.__button_sign = button_sign

    def is_pressed(self):
        pass

class ElevatorButton(Button):
    def __init__(self, destination_floor_number):
        self.__destination_floor_number = destination_floor_number

    def is_pressed(self):
        pass

class ElevatorPanel:
    def __init__(self, floor_buttons, open_button, close_button):
        self.__floor_buttons = floor_buttons
        self.__open_button = open_button
        self.__close_button = close_button


class HallPanel:
    def __init__(self, up, down):
        self.__up = up
        self.__down = down

class Display:
    def __init__(self, floor, capacity, direction):
        self.__floor = floor
        self.__capacity = capacity
        self.__direction = direction

    def show_elevator_display():
        None

    def show_hall_display():
        None

class ElevatorCar:
    def __init__(self, id, door, state, display, panel):
        self.__id = id
        self.__door = door
        self.__state = state
        self.__display = display
        self.__panel = panel

    def move():
        None

    def stop():
        None

  class Door:
      def __init__(self, state):
          self.__state = state

      def isOpen():
          pass

  class Floor:
      def __init__(self, display, panel):
          self.__display = display
          self.__panel = panel

      def is_bottom_most(self):
          None

      def is_top_most(self):
          None

  class __ElevatorSystem(object):
    __instances = None

    def __new__(cls):
      if cls.__instances is None:
          cls.__instances = super(__ElevatorSystem, cls).__new__(cls)
      return cls.__instances

  class ElevatorSystem(metaclass=__ElevatorSystem):
      def __init__(self, building):
        self.__building = building

      def monitoring():
          None

      def dispatcher():
          None

  class __Building(object):
    __instances = None

    def __new__(cls):
      if cls.__instances is None:
          cls.__instances = super(__Building, cls).__new__(cls)
      return cls.__instances

  class Building(metaclass=__Building):
    def __init__(self):
      self.__floor = []
      self.__elevator = []
