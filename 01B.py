def isDigit(char) -> bool:
    if char >= '0' and char <= '9':
        return True
    return False

def toDigit(char) -> int:
    return ord(char) - ord('0')

spellingDict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def isSpelling(line, index) -> bool:
    for key, _ in spellingDict.items():
        n = len(key)-1
        if index >= n and(line[index-n:index+1] == key):
            return True
    return False

def getSpelling(line, index) -> int:
    for key, value in spellingDict.items():
        n = len(key)-1
        if index >= n and(line[index-n:index+1] == key):
            return value
    return 0

def main():
    with open('input01A.txt', 'r') as f1:
        line = f1.readline()
        ans = 0
        while line:
            dig = []
            for i in range(len(line)):
                if isDigit(line[i]):
                    dig.append(toDigit(line[i]))
                else:
                    if isSpelling(line, i):
                        dig.append(getSpelling(line, i))
            
            s = "".join(str(i) for i in dig)
            ans += int(s[0]) * 10
            ans += int(s[-1])
            
            line = f1.readline()
        print(ans)
        f1.close()

def unitTestIsSuccess():
    s = "onetwothreeeeefourfivesixxxxxsevennneightttteennineononeoneone"
    for i in range(len(s)):
        if isSpelling(s, i):
            print(getSpelling(s, i))

main()