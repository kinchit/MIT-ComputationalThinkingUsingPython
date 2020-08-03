animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def how_many(aDict):
    count = 0
    for letter in aDict:
        for num in aDict[letter]:
            count += 1
    return count

def biggest(aDict):
    #count = 0
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result

print(how_many(animals))
print(biggest(animals))