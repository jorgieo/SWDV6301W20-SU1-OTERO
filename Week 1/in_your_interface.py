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
        return self

    def __next__(self):
        

def main():
    classmates = Teams(['John', 'Steve', 'Tim'])
    print(len(classmates))
    print('Tim' in classmates) # Test __contains__
    print('Bob' in classmates) # Test __contains__

main()