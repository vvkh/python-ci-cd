def generate(max_number):
    result = []
    for number in range(1, max_number):
        if number % 15 == 0:
            next_element = 'fizzbuzz'
        elif number % 3 == 0:
            next_element = 'fizz'
        elif number % 5 == 0:
            next_element = 'buzz'
        else:
            next_element = number
        result.append(next_element)
    return result
