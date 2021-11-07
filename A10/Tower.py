import sys
import math

# Input  : n the number of disks
# Output : returns the number of transfers using four needles
# def num_moves (n):
#     if n == 1:
#         return 1
#     k = math.floor(n - math.sqrt(2 * n + 1) + 1)
#     if n > 1 and k > 0:
#         return num_moves(n - 1) + num_moves(n - k - 1) + 1
#     return 0
def stack(n, moves):
    if n == 1:
        return moves + n
    print(moves)
    if n == 2:
        return stack(n - 1, moves + n)
    return stack(n - 1, moves + moves + 1)

def tower(n):
    # if n >= 1:
    # k = math.floor(n - math.sqrt(2 * n + 1) + 1)
    print(stack(n, 0))
    # return 1

def main():
  # read number of disks and print number of moves
    for line in sys.stdin:
        line = line.strip()
        num_disks = int(line)
        print(tower(num_disks))

if __name__ == "__main__":
    main()
