from die import Die


def main():
    num_iterations = how_many_iterations()
    num_sides = how_many_sides()
    num_dice = how_many_dice()

    # Create dice instances
    list_dice = create_dice_instances(num_dice, num_sides)

    # set up results dictionary
    results = setup_results_dictionary(num_dice, num_sides)

    for i in range(num_iterations):
        total = roll_dice(list_dice)
        results[total] = results[total] + 1

    # print(results)
    print('TOTAL - ROLLS - PERCENTAGE')
    for i in range(num_dice, (num_dice * num_sides) + 1):
        roll = results[i]
        # percentage = round(results[i] / 10000, 1)
        percentage = round((results[i] / num_iterations) * 100, 1)
        print('   {} - {} rolls - {}%'.format(i, roll, percentage))

def how_many_sides():
    print("How many sides?")
    num_sides = input('> ')
    return int(num_sides)


def how_many_iterations():
    print("How many iterations?")
    iterations = input('> ')
    return int(iterations)


def how_many_dice():
    print("How many dice?")
    num_dice = input('> ')
    return int(num_dice)


def create_dice_instances(num_dice, num_sides):
    list_dice = []
    for i in range(num_dice):
        die = Die(num_sides)
        list_dice.append(die)
    return list_dice


def roll_dice(list_dice):
    total = 0
    for die in list_dice:
        roll_result = die.roll()
        total = total + roll_result
    return total


def setup_results_dictionary(num_dice, num_sides):
    results = {}
    for i in range(num_dice, (num_dice * num_sides) + 1):
        results[i] = 0
    return results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
