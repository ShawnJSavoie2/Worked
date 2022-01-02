# Python 3.10

# YearsOfGrowth

def YearsOfGrowth(InitialPopulation, BirthRate, Settlers, ReferencePopulation):
    InterimPopulation = InitialPopulation
    YearsOfGrowth = 0
    while InterimPopulation < ReferencePopulation:
        InterimPopulation += InterimPopulation * BirthRate + Settlers
        YearsOfGrowth += 1
    return YearsOfGrowth, InterimPopulation


if __name__ == '__main__':
    import builtins
    class I():
        YearsOfGrowth = YearsOfGrowth
    builtins.I = I
    InitialPopulation = float(input('Enter InitialPopulation: '))
    BirthRate = float(input('Enter BirthRate: '))
    Settlers = float(input('Enter Settlers: '))
    ReferencePopulation = float(input('ReferencePopulation: '))
    YearsOfGrowth, InterimPopulation = YearsOfGrowth(InitialPopulation, BirthRate, Settlers, ReferencePopulation)
    print('YearsOfGrowth: ', YearsOfGrowth)
    print('InterimPopulation: ', InterimPopulation)
