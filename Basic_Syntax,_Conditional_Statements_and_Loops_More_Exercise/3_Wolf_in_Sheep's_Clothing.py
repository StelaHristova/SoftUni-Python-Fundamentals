animals = input()

animals_list = animals.split(', ')
number_of_animals = len(animals_list)
animals_list_reversed = list(reversed(animals_list))

if animals_list_reversed[0] == 'wolf':
    print("Please go away and stop eating my sheep")
else:
    for i in range(number_of_animals):
        current_animal = animals_list_reversed[i]
        if current_animal == 'wolf':
            sheep_to_be_eaten = i
            print(f"Oi! Sheep number {sheep_to_be_eaten}! You are about to be eaten by a wolf!")
