def isDigit(char) -> bool:
    if char >= '0' and char <= '9':
        return True
    return False

def toDigit(char) -> int:
    return ord(char) - ord('0')

with open('input01A.txt', 'r') as f1:
    line = f1.readline()
    ans = 0
    while line:
        i, j = 0, len(line)-1
        while i < len(line) and not isDigit(line[i]):
            i += 1
        while j >= 0 and not isDigit(line[j]):
            j -= 1
        ans += toDigit(line[i]) * 10
        ans += toDigit(line[j])
        line = f1.readline()
    print(ans)
    f1.close()