import sys

# START CODE
def reverse_string(s: str) -> str:
    # TODO: Tulis logika Anda di sini
    return ""
# END CODE

def main():
    lines = sys.stdin.read().splitlines()
    if lines:
        print(reverse_string(lines[0]))

if __name__ == "__main__":
    main()