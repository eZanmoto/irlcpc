height, width = map(int, '9 8'.split())

grid = [""".CCC....
ECBCBB..
DCBCDB..
DCCC.B..
D.B.ABAA
D.BBBB.A
DDDDAD.A
E...AAAA
EEEEEE..
""".split('\n')[i] for i in xrange(height)
]

chars = set(('').join(grid))
chars.remove('.')

above = {}

for char in chars:
    top = 0
    while char not in grid[top]:
        top += 1

    bot = height - 1
    while char not in grid[bot]:
        bot -= 1

    left = 0
    while char not in [grid[i][left] for i in xrange(height)]:
        left += 1

    right = width - 1
    while char not in [grid[i][right] for i in xrange(height)]:
        right -= 1

    above[char] = set(
        grid[top][left:right]
      + grid[bot][left:right]
      + ('').join(grid[i][left] for i in xrange(top, bot+1))
      + ('').join(grid[i][right] for i in xrange(top, bot+1))
    )
    above[char].remove(char)

stack = []
while len(above) > 0:
    for c, aboves in above.items():
        if len(aboves) == 0:
            char = c
            break
    stack.append(char)
    del above[char]
    for _, aboves in above.items():
        aboves.discard(char)

print ('').join(reversed(stack))
