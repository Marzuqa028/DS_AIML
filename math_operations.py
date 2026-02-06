def power(base, exp):
    res = base ** exp
    return res

def average(numbers_list):
    sum = 0
    for num in numbers_list:
        sum = sum+num
    avg = sum/len(numbers_list)
    return avg
