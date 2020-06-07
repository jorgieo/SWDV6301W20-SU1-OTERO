"""
Singleton Example
"""

class ElectedPresident():
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = 'The President'
        return cls.__instance


if __name__ == '__main__':

    president = ElectedPresident()
    El_Presidente = ElectedPresident()

    print("Test if the instances are the same:")
    print(president == El_Presidente)