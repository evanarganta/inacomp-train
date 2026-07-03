import sys

# START CODE
def count_vowels(s: str) -> int:
    vowels = set('aiueo')
    return sum(1 for c in s if c in vowels)
# END CODE

def main():
    lines = sys.stdin.read().splitlines()
    if lines:
        print(count_vowels(lines[0]))

if __name__ == "__main__":
    main()