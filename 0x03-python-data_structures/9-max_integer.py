def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if not my_list:
        return None

    max_value = my_list[0]
    for num in range(len(my_list)):
        if my_list[num] > max_value:
            max_value = my_list[num]

    return (max_value)
