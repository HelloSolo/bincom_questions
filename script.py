from bs4 import BeautifulSoup
import re
import random
import statistics
# import requests

# response = requests.get(
#     'https://drive.google.com/open?id=1nf9WMDjZWIUnlnKyz7qomEYDdtWfW1Uf')

dataFile = open('dataFile.html')
soup = BeautifulSoup(dataFile.read(), 'html.parser')
elements = soup.select('td')

colours = []


for index in range(1, 10, 2):
    text = re.sub('\n*\s*', '', elements[index].getText().strip())
    colours.extend(text.split(','))

colourCount = {}

for colour in colours:
    if colour not in colourCount:
        colourCount[colour] = 1
    else:
        colourCount[colour] += 1

# Preparing for calculation by sorting color count
colourCount = sorted(colourCount.items(), key=lambda x: x[1])
colourCount = dict(colourCount)

# Calculating Mean
mean = sum(colourCount.values())/len(colourCount)

total = 0
for colour in colourCount:
    total += colourCount[colour]
    if mean < total:
        meanColour = colour
        break
print(f'1. Mean colour is {meanColour}')

# Mode
print(f'2. Mostly worn colour is {list(colourCount.keys())[-1]}')

# Median
median = sum(colourCount.values())/2
total = 0
for colour in colourCount:
    total += colourCount[colour]
    if median < total:
        medianColour = colour
        break
print(f'3. Median colour is {medianColour}')

# Variance
variance = statistics.variance(colourCount.values())
print(f'4. Variance of the colours is {variance}')

# Probability that a colour is red
probability = colourCount['RED']/sum(colourCount.values())
print(f'5. Probability of a colour selected at random being red {probability}')


# Recursive search algorithm
def search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return search(arr, low, mid - 1, x)
        else:
            return search(arr, mid + 1, high, x)
    else:
        return -1


arr = [3, 42, 8, 5, 3]

print(
    f'7. Index of 8 in [3,42,8,5,3,] is {search([3,42,8,5,3], 0, len(arr)-1, 8)}')


# Generate random four digits numbers of 0s and 1s and conver to base 10
randomDigits = []

for i in range(4):
    randomDigits.append(str(random.choice([0, 1])))
randomDigits = "".join(randomDigits)

print(f'8. Generated digits {randomDigits} in base ten {int(randomDigits, 2)}')

# Fibinacci Sequence
FibArray = [0, 1]


def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n < len(FibArray):
        return FibArray[n]
    else:
        FibArray.append(fibonacci(n - 1) + fibonacci(n - 2))
        return FibArray[n]


print(f'9. Sum of the first 50 fibonacci sequence is {fibonacci(50)}')
