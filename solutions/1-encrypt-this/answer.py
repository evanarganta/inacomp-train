
import sys

def encrypt_word(word):
    if not word:
        return ""
    first_ascii = str(ord(word[0]))
    if len(word) == 1:
        return first_ascii
    chars = list(word)
    chars[1], chars[-1] = chars[-1], chars[1]
    return first_ascii + "".join(chars[1:])

def main():
    line = sys.stdin.read().strip()
    if not line:
        return
    words = line.split(" ")
    result = [encrypt_word(w) for w in words]
    print(" ".join(result))

if __name__ == "__main__":
    main()
