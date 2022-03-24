class Character:
    def __init__(self, char_name: str, health: int, char_class: str,
        char_race: str, char_faction: int, distance_traveled: int = 0,
        char_id: int = 0):
        # should have validations here
        self.char_id = char_id
        self.char_name = char_name
        self.health = health
        self.char_class = char_class
        self.char_race = char_race
        self.char_faction = char_faction
        self.distance_traveled = distance_traveled

    # python has many "dunder" methods (double-underscore)
    # often, they way they work is, some builtin function named X
    #   effectively calls a dunder method named __X__ on the object passed.
    # or, for operators like == there is __eq__, or for <  there is __lt__
    #  (so python definitely supports operator overloading)
    def __str__(self):
        return f'({self.char_id}) {self.char_name}'

    def __len__(self):
        return 1

    def __iter__(self):
        return 1 # look up how to actually do it

    # def create(self):
    #     # with statement as convenient way to automatically close some resource like a file
    #     with open('database.csv', 'w') as file:
    #         print('asdf', file=file)


    # def create(self):
    #     file = None
    #     try:
    #         file = open('database.csv', 'w')
    #         print('asdf', file=file)
    #     finally:
    #         if file:
    #             file.close()


    # def create(self):
    #     file = open('database.csv', 'w')
    #     print('asdf', file=file)
    #     file.close()

if __name__ == '__main__':
    x = Character('a', 1, 'a', 'a', 1)
    print(len([1,2]))
    print(len(x))
    for item in x:
        print(item)
