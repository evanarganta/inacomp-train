import sys

# START CODE
def base64_to_decimal(s: str) -> int:
    # TODO: Tulis logika Anda di sini
    return 0
# END CODE

def main():
    lines = sys.stdin.read().splitlines()
    if lines:
        line = lines[0].rstrip('\r\n')
        print(base64_to_decimal(line))

if __name__ == "__main__":
    main()