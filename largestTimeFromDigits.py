# submitted and accepted: 9/26/2020
def largestTimeFromDigits(array):
    #make a list of all 2 digit combinations
    twoCombo = []
    i = 0
    while i < len(array):
        #make a list of everything but the 'token'
        list = array[:i] + array[i+1:]
        #combine token with every item in the list
        for n in list:
            twoComboItem =  str(array[i]) + str(n)
            twoCombo.append(twoComboItem)
        i += 1
    print("twoCombo: " + str(twoCombo))
    #find greatest number less than 24
    time = []
    for item in twoCombo:
        currentArray = array.copy()
        currentHrLarge = 0
        if int(item) < 24 and int(item) >= currentHrLarge:
            currentHrLarge = item
            #then find greatest number less than 60 from the left over numbers
            currentArray.remove(int(currentHrLarge)//10)
            currentArray.remove(int(currentHrLarge)%10)
            print("currentArray: " + str(currentArray))
            firstCombo = str(currentArray[0]) + str(currentArray[1])
            secondCombo = str(currentArray[1]) + str(currentArray[0])
            if int(firstCombo) < 60 and int(secondCombo) < 60:
                if int(firstCombo) > int(secondCombo):
                    time.append(str(currentHrLarge) + firstCombo)
                elif int(secondCombo) > int(firstCombo):
                    time.append(str(currentHrLarge) + secondCombo)
            elif int(firstCombo) < 60:
                time.append(str(currentHrLarge) + firstCombo)
            elif int(secondCombo) < 60:
                time.append(str(currentHrLarge) + secondCombo)
    print("time: " + str(time))
    if len(time) > 0:
        numTime = []
        max = '0'
        for string in time:
            if int(string) > int(max):
                max = string
                # numTime.append(int(string))
            elif int(string) == 0:
                return "00:00"
            # else:
            #     return "00:00"
        # a = max(numTime)
        greatestTime = max
        return greatestTime[:2] + ":" + greatestTime[2:]
    return ''

if __name__ == '__main__':
    # print(largestTimeFromDigits([1,2,2,3]))
    # print(largestTimeFromDigits([5,5,5,5]))
    print(largestTimeFromDigits([1,9,6,0]))
    # print(largestTimeFromDigits([0,0,1,0]))
