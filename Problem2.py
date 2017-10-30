'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

def fibonacci():
    second, first = 2, 1
    while True:
        second, first = second + first, second
        yield second


def evens(series):
    for n in series:
        if n % 2 == 0:
            yield n

result = []
result.append(2)
for f in evens(fibonacci()):
    if f > 4000000:
        break
    result.append(f)
print(sum(result))
