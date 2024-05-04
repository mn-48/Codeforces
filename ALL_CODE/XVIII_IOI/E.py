def optimal_eating(pieces):
  """
  Calculates the total size of pieces eaten by Alice and Bob optimally.

  Args:
      pieces: A list of integers representing the sizes of persimmon pieces.

  Returns:
      A tuple containing the total size eaten by Alice and Bob respectively.
  """
  n = len(pieces)
  pieces.sort()  # Sort pieces in ascending order

  alice_total, bob_total = 0, 0
  turn = True  # True for Alice, False for Bob

  for piece in pieces:
    if turn:
      alice_total += piece
    else:
      bob_total += piece
    turn = not turn  # Switch turns

  return alice_total, bob_total

# Read input
n = int(input())
pieces = list(map(int, input().split()))

# Calculate optimal eating
alice_eat, bob_eat = optimal_eating(pieces)

# Print output
print(alice_eat, bob_eat)
