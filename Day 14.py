

file = open(r"Inputs/Day 14 Input.txt", "r")

w=101
h=103
print((w//2) - 1, (w // 2) + 1)
def move(bot, cycles, w, h):
    bot[0][0] = (bot[0][0] + (bot[1][0] * cycles)) % (w)
    bot[0][1] = (bot[0][1] + (bot[1][1] * cycles)) % (h)
    return bot

bots = []
quad_count = [0,0,0,0]
for line in file:
    
    bot = [list(map(lambda y: int(y), x[2:].split(','))) for x in line.strip().split(' ')]

    bot = move(bot, 100, w, h)

    if bot[0][0] <= ((w // 2) - 1):
        if bot[0][1] <= ((h // 2) - 1):
            quad_count[0] += 1
        elif bot[0][1] >= ((h // 2) + 1):
            quad_count[1] += 1
    elif bot[0][0] >= ((w // 2) + 1):
        if bot[0][1] <= ((h // 2) - 1):
            quad_count[2] += 1
        elif bot[0][1] >= ((h // 2) + 1):
            quad_count[3] += 1

print(quad_count[0] * quad_count[1] * quad_count[2] * quad_count[3])

