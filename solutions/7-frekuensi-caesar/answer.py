
import sys
from collections import Counter

# START CODE
def decrypt_caesar(ciphertext: str) -> str:
    counts = Counter(ciphertext)
    max_count = max(counts.values())
    candidates = [ch for ch, c in counts.items() if c == max_count]
    most_common_char = min(candidates)

    shift = (ord(most_common_char) - ord('E')) % 26

    result = []
    for ch in ciphertext:
        decrypted = chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
        result.append(decrypted)
    return ''.join(result)
# END CODE

def main():
    line = sys.stdin.readline().strip()
    if line:
        print(decrypt_caesar(line))

if __name__ == "__main__":
    main()
