class Teams:
    def __init__(self, members):
        self.__myTeam = members

    def __len__(self):
        return len(self.__myTeam)

    def __contains__(self, x):
        """Method to return membership test"""

        if x in self.__myTeam:
            return True
        return False
    
    def __iter__(self):
        return iter(self.__myTeam)

    def __next__(self):
        return next(self.__myTeam)

def main():
    classmates = Teams(['John', 'Steve', 'Tim'])
    print(len(classmates))
    
    # Tests for __contains__ method
    print('Tim' in classmates) 
    print('Sam' in classmates)
    
    # Test for __iter__ method
    for name in classmates:
        print(name)

main()