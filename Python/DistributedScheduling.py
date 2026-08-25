tasks = [5,2,7,1,4]
load = [0,0,0]

for i,task in enumerate(tasks):
    min_process = load.index(min(load))
    load[min_process] += task
    print(f'Task {i+1} assigned to the processor {min_process + 1}')

for i in range(len(load)):
    print(f'Processor{i+1} Load = {load[i]}')
    