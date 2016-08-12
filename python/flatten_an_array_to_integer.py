def flatten(input_array):
    if input_array == []:
        return input_array
    if isinstance(input_array[0], list):
        return flatten(input_array[0]) + flatten(input_array[1:])
    return input_array[:1] + flatten(input_array[1:])

if __name__ == '__main__':
    input_array = [[1, 2, [3]], 4]
    print flatten(input_array)
