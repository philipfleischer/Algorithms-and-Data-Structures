def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

#print(sum([1,2,7,9]))  

def sum_rec(numbers):
    if not numbers:
        return 0
    print("Calling sum_rec(%s)" % numbers[0:])
    remaining_sum = sum_rec(numbers[1:])
    print("Calling sum_rec(%s) returning %d + %d" 
        % (numbers, numbers[0], remaining_sum))
    return numbers[0] + remaining_sum

print(sum_rec([1,2,7,9]))  