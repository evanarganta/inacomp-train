
import sys

# START CODE
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
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
