def swap():
    """
    Function that swaps the first and last elements of the list, regardless of length
    :param name: a list of at least two elements
    :return: the same list with the first and last elements swapped
    """
    name = [1, 2, 3, 4, 5, 6, 7]
    print(name)
    x = name[-1]
    name[-1] = name[0]
    print(name)
    name[0] = x
    print(name)
swap()


states = ['Maryland', 'Texas', 'Ohio']
print(states)

def rotate_left():
    """
    Given a list of ints length 3, return a list with the elements "rotated left" so [1, 2, 3] yields [2, 3, 1].
    :param list_one: A list consisting of exactly three integers
    :return: a list where all the elements have been shifted 1 place to the left
    """

    states = ['Maryland', 'Texas', 'Ohio']
    print(states)
    states[0] = states[1]
    states[1] = states[2]
    states[2] = states[0]
    print(states)


rotate_left()


def max_end():
    """
    This function will find if the first or last element of an list is larger, then set all the elements
    of that list to that value.
    :param list_one: A list consisting of three elements - all integers
    :return: A list where all the elements are the larger of the first or last element of the original list
    """
    albums = [1, 2, 3]
    if albums[0] > albums[-1]:
        albums = (albums[0]), (albums[0]), (albums[0])


        print(albums)
    else

max_end()



