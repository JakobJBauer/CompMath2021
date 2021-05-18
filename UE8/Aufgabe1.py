# Decorator was already used last exercise

class Example:

    classText = "I am a variable in this class"

    def __init__(self, _id):
        self.instanceText = "I differ every instance! ID: " + str(_id)

    def instancePrint(self):
        print(self.instanceText)

    @classmethod
    def classPrint(cls):
        print(cls.classText)

    @staticmethod
    def staticPrint():
        staticText = "I can't access anything in the class or instance I am called in"
        print(staticText)
