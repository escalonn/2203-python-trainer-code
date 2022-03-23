import csv
from character import Character

class FileDatabase:
    def __init__(self):
        self.characters = []
        with open('database.csv', 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                char = Character(
                    char_id=int(row[0]), char_name=row[1], health=int(row[2]),
                    char_class=row[3], char_race=row[4],
                    char_faction=int(row[5]), distance_traveled=int(row[6]))
                self.characters.append(char)


    def create_character(self, char: Character):
        # check for duplicate ID
        if char.char_id != 0:
            if any(c.char_id == char.char_id for c in self.characters):
                raise Exception('duplicate ID')
        # add to in-memory collection
        self.characters.append(char)
        # (call commit() to push to file)


    def commit(self):
        # handle generating a primary key value
        max_id = max(c.char_id for c in self.characters)
        for char in self.characters:
            if char.char_id == 0:
                max_id += 1
                char.char_id = max_id
        # write the rows
        with open('database.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for char in self.characters:
                # this needs to be in the right order vs reading
                writer.writerow([
                    char.char_id, char.char_name, char.health, char.char_class,
                    char.char_race, char.char_faction, char.distance_traveled])
