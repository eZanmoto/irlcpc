m, n = map(int, '6 4'.split())

MODS = [(-1,-2),(-2,-1),(-1,2),(2,-1),(0, 0),(1,-2),(-2,1),(1,2),(2,1)]

def kill_from((x, y)):
    global MODS
    return set((x+x_, y+y_) for (x_, y_) in MODS)

def knights(m, state, bad, states, remaining):
    for x in xrange(m):
        for y in xrange(m):
            new_knight = (x, y)
            if new_knight not in bad:
                s = state|set([new_knight])
                if remaining > 1:
                    knights(m, s, bad|kill_from(new_knight), states, remaining-1)
                else:
                    s_ = 0
                    for i in xrange(m*m):
                        s_ += 2**i if (i/m, i%m) in s else 0
                    states.add(s_)

def print_states(m, states):
    for knights in states:
        for i in xrange(m*m):
            print ('K' if knights & 2**i else '.'),
            if (i+1) % m == 0:
                print
        print

states = set()
knights(m, set(), set(), states, n)
print len(states)
