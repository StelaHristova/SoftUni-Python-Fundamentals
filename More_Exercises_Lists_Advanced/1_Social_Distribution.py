population = [int(number) for number in input().split(", ")]
minimum_wealth = int(input())

added_sum = 0

for num in range(0, len(population)):
    if (sum(population) // minimum_wealth) < len(population):
        print("No equal distribution possible")
        exit()

    if population[num] < minimum_wealth:
        added_sum += (minimum_wealth - population[num])
        population[num] = minimum_wealth

    while added_sum > 0:
        index = population.index(max(population))
        if (added_sum + minimum_wealth) <= max(population):
            population[index] -= added_sum
            added_sum = 0
        else:
            population[index] -= minimum_wealth
            added_sum -= population[index]
            population[index] = minimum_wealth

print(population)


