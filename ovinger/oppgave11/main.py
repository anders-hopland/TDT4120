from sys import stdin, stderr

def best_path(nm, prob):
    length = len(nm)
    finals = [0] * length
    visited = [0] * length
    finals[0] = prob[0]

    for i in range(length):
        for j in range(length):

            #Checking for occurence of edge
            if nm[i][j] == 1:
                if finals[j] < finals[i] * prob[j]:
                    visited[j] = i
                    finals[j] = finals[i] * prob[j]

    #Not fpund a way
    if visited[-1] == 0:
        print(0)
    
    path = []
    next = length - 1

    while True:
        path.append(next)
        if next == 0:
            result = ""
            path.reverse()
            for i in path:
                result += str(i) + "-"
            
            print(result[:-1])
            return
        next = visited[next]

n = int(stdin.readline())
probabilities = [float(x) for x in stdin.readline().split()]
neighbour_matrix = []
for line in stdin:
    neighbour_row = [0] * n
    neighbours = [int(neighbour) for neighbour in line.split()]
    for neighbour in neighbours:
        neighbour_row[neighbour] = 1
    neighbour_matrix.append(neighbour_row)
best_path(neighbour_matrix, probabilities)
