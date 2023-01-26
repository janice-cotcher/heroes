

class Hero(object):
    def __init__(self, name, power, identity):
        self.name = name
        self.power = power
        self.identity = identity

    def say_hello(self):
        print('Hello, evil-doers! My name is', self.name + '!')
        print('My super power is', self.power, 'so you better beware.')

    def divulge(self):
        print('My real name is', self.identity)


bruce = Hero('Batman', 'martial arts', 'Bruce Wayne')
bruce.say_hello()
bruce.divulge()
print("\n")
diana = Hero('Wonder Woman', 'super strength', 'Diana Prince')
diana.say_hello()
diana.identity = "changed!"
diana.divulge()
