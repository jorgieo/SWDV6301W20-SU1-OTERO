"""
Factory Pattern Example
"""

from abc import ABCMeta, abstractmethod

class Relative(metaclass=ABCMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_emergency_contact = False

    @abstractmethod
    def set_emegency_contact(self):
        pass
    @abstractmethod
    def reset_emegency_contact(self):
        pass

    def __str__(self):
        return f"{self.name}:\n\tAge: {self.age}\n\tRelationship: {self.__class__.__name__}\n\t" \
               f"Emergency Contact? {self.is_emergency_contact}"

class Spouse(Relative):

    def set_emegency_contact(self):
        self.is_emergency_contact = True

    def reset_emegency_contact(self):
        self.is_emergency_contact = False

class Parent(Relative):

    def set_emegency_contact(self):
        self.is_emergency_contact = True

    def reset_emegency_contact(self):
        self.is_emergency_contact = False


class Sibling(Relative):

    def set_emegency_contact(self):
        self.is_emergency_contact = True

    def reset_emegency_contact(self):
        self.is_emergency_contact = False


class Child(Relative):

    def set_emegency_contact(self):
        self.is_emergency_contact = True

    def reset_emegency_contact(self):
        self.is_emergency_contact = False


class RelativeFactory():
    @classmethod
    def create(cls, relation, *args):
        relation = relation.lower().strip()

        if relation == 'spouse':
            return Spouse(*args)
        elif relation == 'parent':
            return Parent(*args)
        elif relation == 'sibling':
            return Sibling(*args)
        elif relation == 'child':
            return Child(*args)

if __name__ == '__main__':
    persons = [('Spouse','Mary', 28), ('Parent', 'Bob', 55), ('Sibling', 'Jack', 32), ('Child', 'Marie', 4)]
    relationships = []
    for person in persons:
        relationships.append(RelativeFactory.create(person[0], person[1], person[2]))

    for relation in relationships:
        if relation.__class__.__name__ == 'Spouse':
            relation.set_emegency_contact()
        print(relation)