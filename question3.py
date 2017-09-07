def countExclamLoop(inputString):
    count = 0;
    for char in inputString:
        if char == '!':
            count += 1
    return count

def countExclamRecur(inputString, count=0):
    if inputString == '':
        return count
    elif inputString[0] == '!':
        return countExclamRecur(inputString[1:], count + 1)
    else:
        return countExclamRecur(inputString[1:], count)



    

