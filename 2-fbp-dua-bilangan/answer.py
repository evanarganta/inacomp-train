import sys

# START CODE
def gcd(a: int, b: int) -> int:
    # TODO: Tulis logika Anda di sini
    return 0
# END CODE

def main():
    line = sys.stdin.read().strip()
    if not line:
        return
    parts = line.split()
    if len(parts) >= 2:
        a = int(parts[0])
        b = int(parts[1])
        print(gcd(a, b))

if __name__ == "__main__":
    main()