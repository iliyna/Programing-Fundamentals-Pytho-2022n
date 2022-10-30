class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == 'mammal':
            return f'Mammals in {self.name}: {", ".join(self.mammals)}' \
                   f'\nTotal animals: {Zoo.__animals}'
        elif species == 'fish':
            return f'Fishes in {self.name}: {", ".join(self.fishes)}' \
                   f'\nTotal animals: {Zoo.__animals}'
        elif species == 'bird':
            return f'Birds in {self.name}: {", ".join(self.birds)}' \
                   f'\nTotal animals: {Zoo.__animals}'


zoo_name = input()
zoo = Zoo(zoo_name)
num = int(input())
for i in range(num):
    comm = input().split(' ')
    species_add = comm[0]
    name_add = comm[1]
    zoo.add_animal(species_add, name_add)
species_output = input()
print(zoo.get_info(species_output))

