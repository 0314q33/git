def sum_even(number):
    total=0
    for unm in numbers:
        if unm%2==0:
            total=total+unm
    return total
numbers=[1,2,3,4,5,6,7,8,9]
print(sum_even(numbers))