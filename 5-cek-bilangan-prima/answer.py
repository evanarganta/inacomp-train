import sys

# START CODE
def is_prime(n: int) -> bool:
    # TODO: Tulis logika Anda di sini
    return False
# END CODE

def main():
    lines = sys.stdin.read().splitlines()
    if lines:
        n = int(lines[0])
        if is_prime(n):
            print("YA")
        else:
            print("TIDAK")

if __name__ == "__main__":
    main()