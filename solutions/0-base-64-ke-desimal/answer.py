
import sys

# START CODE
def base64_to_decimal(s: str) -> int:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    value = 0
    for ch in s:
        value = value * 64 + alphabet.index(ch)
    return value
# END CODE

def main():
    lines = sys.stdin.read().splitlines()
    if lines:
        line = lines[0].rstrip('\r\n')
        print(base64_to_decimal(line))

if __name__ == "__main__":
    main()
