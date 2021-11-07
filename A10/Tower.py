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
def stack(n, moves = 0, count = 1):
    if count == n:
        return 2 * moves + 1
    if count == 1 or count == 2:
        return stack(n, moves + count, count + 1)
    return stack(n, 2 * moves + 1, count + 1)

def tower(n):
    moves = 0
    if n <= 3:
        return stack(n)
    k = math.floor(n - math.sqrt(2 * n + 1) + 1)
    moves = stack(k)
    moves += 2 * stack(n - k - 1) + 2
    return moves

    

def main():
  # read number of disks and print number of moves
    for line in sys.stdin:
        line = line.strip()
        num_disks = int(line)
        print(tower(num_disks))

if __name__ == "__main__":
    main()
