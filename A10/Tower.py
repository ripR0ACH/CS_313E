import sys
import math

# Input  : n the number of disks
# Output : returns the number of transfers using four needles
def num_moves (n):
    if n == 1:
        return 1
    k = math.floor(n - math.sqrt(2 * n + 1) + 1)
    if n > 1 and k > 0:
        return num_moves(n - 1) + num_moves(n - k - 1) + 1
    return 0

# def tower(n, source, destination, temp):
#     if n >= 1:
#         k = math.floor(n - math.sqrt(2 * n + 1) + 1)
#         source = [i + 1 for i in range(n)]
#         spare1 = [source[:k]]
#         spare2 = [source[k:]]
#         dest = []
#         before = tower(n - k - 1, source, temp, destination)
#         after = tower(n - 1, temp, destination, source)
#         return before + after + 1
#     return 1

def main():
  # read number of disks and print number of moves
    for line in sys.stdin:
        line = line.strip()
        num_disks = int (line)
        print (num_moves (num_disks))

if __name__ == "__main__":
    main()
