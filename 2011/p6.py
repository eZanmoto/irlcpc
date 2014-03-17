A, B, N = map(int, '5 7 3'.split())

found = {(0, 0): None}

agenda = [(0, 0)]

while agenda[-1][1] != N:
    x = agenda.pop()
    a, b = x

    if a < A and (A, b) not in found:
        agenda.append((A, b))
        found[(A, b)] = (x, 'fill A')

    if b < B and (a, B) not in found:
        agenda.append((a, B))
        found[(a, B)] = (x, 'fill B')

    if a != 0 and (0, b) not in found:
        agenda.append((0, b))
        found[(0, b)] = (x, 'empty A')

    if b != 0 and (a, 0) not in found:
        agenda.append((a, 0))
        found[(a, 0)] = (x, 'empty B')

    if a != 0 and b < B:
        ab = a + b
        y = (0, ab) if ab < B else (ab - B, B)
        if y not in found:
            agenda.append(y)
            found[y] = (x, 'pour A B')

    if b != 0 and a < A:
        ab = a + b
        y = (ab, 0) if ab < A else (A, ab - A)
        if y not in found:
            agenda.append(y)
            found[y] = (x, 'pour B A')

actions = ['success']
state, action = found[agenda[-1]]
actions.append(action)
while state != (0, 0):
    state, action = found[state]
    actions.append(action)

print ('\n').join(reversed(actions))
