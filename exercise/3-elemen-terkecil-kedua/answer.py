import sys

# START CODE
def second_smallest(n: int, arr: list) -> int:
    # TODO: Tulis logika Anda di sini
    return 0
# END CODE

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:]]
    print(second_smallest(n, arr))

if __name__ == "__main__":
    main()