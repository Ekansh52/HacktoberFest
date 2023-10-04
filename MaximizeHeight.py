"""
Dynamic Programming: Maximize Height for basketball players
Here is the explanation for the code:
1. The maximum sum ending at index i, where we choose from A is m[i][0].
2. The maximum sum ending at index i, where we choose from B is m[i][1].
3. For the base case, the maximum sum ending at index 0 is 0.
4. The maximum sum ending at index i can be calculated by the following:
5. The maximum sum ending at index i - 1, where we choose from B, plus A[i - 1].
6. The maximum sum ending at index i - 1, where we choose from A, plus B[i - 1].
7. The maximum sum ending at index i - 1, where we skip, plus 0.
8. The maximum sum ending at index i - 1, where we choose from A is m[i - 1][0].
9. The maximum sum ending at index i - 1, where we choose from B is m[i - 1][1].
10. The maximum sum ending at index i - 1, where we skip is 0.
11. The maximum sum ending at index i, where we choose from A is m[i][0].
12. The maximum sum ending at index i, where we choose from B is m[i][1].
13. The maximum sum ending at index i can be calculated by the following:
14. The maximum sum ending at index i - 1, where we choose from B, plus A[i - 1].
15. The maximum sum ending at index i - 1, where we choose from A, plus B[i - 1].
16. The maximum sum ending at index i - 1, where we skip, plus 0.
17. The maximum sum ending at index i - 1, where we choose from A is m[i - 1][0].
18. The maximum sum ending at index i - 1, where we choose from B is m[i - 1][1].
19. The maximum sum ending at index i - 1, where we skip is 0.
20. The maximum sum ending at index i, where we choose from A is m[i][0].
21. The maximum sum ending at index i, where we choose from B is m[i][1]. 
"""
def f(A, B):
  m = [0] * (len(A) + 1)

  for i in range(0, len(A) + 1):
    m[i] = [0, 0]

  for i in range(1, len(A) + 1):
    # Choose from A or skip
    m[i][0] = max(A[i - 1] + m[i - 1][1], m[i - 1][0])
    # Choose from B or skip
    m[i][1] = max(
      B[i - 1] + m[i - 1][0], m[i - 1][1])

  return max(m[len(A)])

a = [9, 3, 5, 7, 3]
b = [5, 8, 1, 4, 5]

print(f(a, b))
