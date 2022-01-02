# Python 3.10

# Population

def Population(InitialPopulation, BirthRate, Settlers, Years):
    Population = InitialPopulation
    while Years != 0:
        Population += Population * BirthRate + Settlers
        Years -= 1
    return Population


if __name__ == '__main__':
    import builtins
    class I():
        Population = Population
    builtins.I = I
    InitialPopulation = float(input('Enter InitialPopulation: '))
    BirthRate = float(input('Enter BirthRate: '))
    Settlers = float(input('Enter Settlers: '))
    Years = float(input('Years: '))
    Population = Population(InitialPopulation, BirthRate, Settlers, Years)
    print('Population: ', Population)
