
import sys

# START CODE
def decode(msg: str) -> str:
    result = []
    for ch in msg:
        if 'a' <= ch <= 'z':
            result.append(chr(ord('z') - (ord(ch) - ord('a'))))
        elif 'A' <= ch <= 'Z':
            result.append(chr(ord('Z') - (ord(ch) - ord('A'))))
        else:
            result.append(ch)
    return ''.join(result)
# END CODE

def main():
    lines = sys.stdin.read().splitlines()
    if not lines or len(lines) == 0:
        print("Input is not a string")
        return
    line = lines[0].rstrip('\r\n')
    if len(line) == 0:
        print("Input is not a string")
    else:
        print(decode(line))

if __name__ == "__main__":
    main()
