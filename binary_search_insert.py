

def binary_search(a_list, a_value):
    lower_index = 0
    upper_index = len(a_list) - 1

    while lower_index <= upper_index:

        divide_index = lower_index + int((upper_index - lower_index)/2)

        if a_list[divide_index] == a_value:
            return divide_index
        elif a_value < a_list[divide_index]:
            upper_index = divide_index - 1
        else:
            lower_index = divide_index + 1

    return -1


def binary_insert(a_list, a_value):
    lower_index = 0
    upper_index = len(a_list) - 1

    while lower_index <= upper_index:

        divide_index = lower_index + int((upper_index - lower_index)/2)

        if a_list[divide_index] == a_value:
            a_list.insert(divide_index, a_value)
            return
        elif a_value < a_list[divide_index]:
            upper_index = divide_index - 1
        else:
            lower_index = divide_index + 1

    if lower_index >= len(a_list):
        a_list.append(a_value)
        return
    if a_value > a_list[lower_index]:
        a_list.insert(lower_index+1, a_value)
    else:
        a_list.insert(lower_index, a_value)
    a = 3

if __name__ == "__main__":
    print("test binary search/insert")
    test_list = ['A', 'D', 'F', 'H', 'I', 'K', 'L', 'M', 'P']
    print(binary_search(test_list, 'K'))
    print(binary_search(test_list, 'Z'))
    print(binary_search(test_list, 'U'))
    print(binary_search(test_list, 'P'))
    print(binary_search(test_list, 'A'))

    test_list = ['D', 'F', 'H', 'I', 'K', 'L', 'M', 'P']
    binary_insert(test_list, 'B')
    print(test_list)
    binary_insert(test_list, 'Y')
    print(test_list)
    binary_insert(test_list, 'X')
    print(test_list)
