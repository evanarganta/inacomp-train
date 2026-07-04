import sys

# START CODE
def decode(msg: str) -> str:
    # TODO: Tulis logika dekode Anda di sini
    return ""
# END CODE

def main():
    lines = sys.stdin.read().splitlines()
    if not lines or len(lines) == 0:
        print("Input is not a string")
        return
    line = lines[0].rstrip('\r\n')
    if len(line) == 0:
        print("Input is not a string")
    else:
        print(decode(line))

if __name__ == "__main__":
    main()