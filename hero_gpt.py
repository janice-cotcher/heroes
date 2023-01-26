class Hero(object):
    # constructor method that initializes the name, power and identity attributes
    def __init__(self, name, power, identity):
        self.name = name
        self.power = power
        self.identity = identity

    # method that greets the evil-doers and says the name and power of the hero
    def say_hello(self):
        print('Hello, evil-doers! My name is', self.name + '!')
        print('My super power is', self.power, 'so you better beware.')

    # method that reveals the real identity of the hero
    def divulge(self):
        print('My real name is', self.identity)


# creating an object of class Hero
bruce = Hero('Batman', 'martial arts', 'Bruce Wayne')
# calling the say_hello() and divulge() methods on bruce object
bruce.say_hello()
bruce.divulge()

# creating an object of class Hero
diana = Hero('Wonder Woman', 'super strength', 'Diana Prince')
# calling the say_hello() and divulge() methods on diana object
diana.say_hello()
# changing the identity attribute of diana object
diana.identity = "changed!"
# calling the divulge() method on diana object after changing the identity
diana.divulge()
