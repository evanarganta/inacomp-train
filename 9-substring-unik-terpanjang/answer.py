import sys

# START CODE
def longest_substring_of(s: str) -> int:
    # TODO: Tulis logika Anda di sini
    return 0
# END CODE

def main():
    lines = sys.stdin.read().splitlines()
    if lines:
        line = lines[0].rstrip('\r\n')
        print(longest_substring_of(line))

if __name__ == "__main__":
    main()