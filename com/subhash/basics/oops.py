

# define class with private, public, static and class methods

class Animal:
    def getType(self):
        return "Animal"


class Person(Animal):

    # pass - use 'pass' keyword to avoid errors because of incomplete code

    # class level (static) variables/attribute
    num_of_hands = 2;

    def __init__(self):
        self.name = "Subhash"

#    oops!! no function overloading :O
#
#    def __init__(self, name):
#        self.name = name
#
#   either use same function with default value to optional arguments
#   OR
#   use class level (static) different factory methods @classmethod

    @classmethod
    def with_name(cls, name):
        obj = cls()
        obj.name = name
        return obj;

    def getType(self):
        return "Person"


if __name__ == "__main__":
    print('Persons always have ', Person.num_of_hands, ' hands')

    # name is not class attribute
    # print('Persons always have ', Person.name, ' name')

    p1 = Person()
    print(p1.name)

    p2 = Person.with_name("SUBHASH")
    print(p2.name)

    print(p2.name, ' is of type: ', p2.getType())

    a = Animal()
    a.name_new = 'some animal' # OMG what is this? you can add new attributes to objects anytime!!! :O
    print(a.name_new, ' is of type: ', a.getType())
