
import sys

# START CODE
def longest_substring_of(s: str) -> int:
    last_seen = {}
    start = 0
    max_len = 0
    for i, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= start:
            start = last_seen[ch] + 1
        last_seen[ch] = i
        cur_len = i - start + 1
        if cur_len > max_len:
            max_len = cur_len
    return max_len
# END CODE

def main():
    lines = sys.stdin.read().splitlines()
    if lines:
        line = lines[0].rstrip('\r\n')
        print(longest_substring_of(line))

if __name__ == "__main__":
    main()
