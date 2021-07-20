'''
Meta class experiment :p
'''

class customClassConstructor(type):
    def __cmd__(self, func): ## Our own method for the construction of classes by inheriting from type.
        func()

def create_new_class(Name='', bases=(), init=None, methods={"m":"m"}):
    m = {"__init__":init}
    for key, values in methods.items():
        m[key] = values
    cls = type(Name, bases, m) # Using type to create the class
    return cls

def person_init(self, name):
    self.name = name

def person_speak(self, msg):
    print(msg)

def person_jump(self):
    print('jumped!')

PersonClass = create_new_class(
    "Person",
    (),
    init=person_init,
    methods={"speak":person_speak, "jump":person_jump} ## keys are the name of the methods, while the values are the funcs.
    )

joe = PersonClass("Joe") # PersonClass is like type, but is really just 'Person'
joe.speak("wassup")

def planet_init(self, name, star):
    self.name = name
    self.star = start

def planet_destroy():
    print('destroyed :(')

c = customClassConstructor('Planet', (), {"__init__":planet_init})
customClassConstructor.__cmd__(c, planet_destroy)
