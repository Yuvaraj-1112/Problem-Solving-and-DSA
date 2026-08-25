server = 100
clock = [95,93,97]

print("Server clock :", server)

for i in range(len(clock)):
    print(f"client {i +1} before sync {clock[i]}")
    clock[i] = server
    print(f'client {i+1} after sync {clock[i]}\n')