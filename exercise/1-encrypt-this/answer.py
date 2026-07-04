import sys

def encrypt_word(word):
    if not word:
        return ""
    # TODO: Write your encryption logic here
    return ""

def main():
    line = sys.stdin.read().strip()
    if not line:
        return
    words = line.split(" ")
    result = [encrypt_word(w) for w in words]
    print(" ".join(result))

if __name__ == "__main__":
    main()