# Check for duplicates in a list

def find_duplicates():
    for n, i in enumerate(numbers):
        if i in numbers[:n]:
            duplicates.append(i)
    print(duplicates)


numbers = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'x', 'x']
duplicates = []
find_duplicates()
