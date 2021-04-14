class Iphone:
    def call(self):
        print('Hi sent by Iphone')


class People:
    def __init__(self, name):
        self.name = name
        self.phone = Iphone()

    def hi(self):
        self.phone.call()


if __name__ == '__main__':
    leo = People('len')
    leo.hi()
