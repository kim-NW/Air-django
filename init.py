class Human:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        print(f"hello my name is {self.name}")

class Player(Human):  
    def __init__(self, name, xp):
        self.xp = xp
    
class Fan(Human):
    def __init__(self, name, fav_team):
        self.fav_team = fav_team
    

# nico_player = Player("nico", 10)
# nico_player.say_hello()
# nico_fan = Fan("nico_fan", "dontknow")
# nico_fan.say_hello()
nico = Player("nico", 10)
nico.say_hello()