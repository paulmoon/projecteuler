import itertools
import time

def coordinates(length, width):
    return itertools.product(range(length), range(width))

def neighbours(xy, graph_len):
    x, y = xy[0], xy[1]
    neighbour_list = []
    if x != 0:
        neighbour_list.append((x-1, y))
    if x != graph_len-1:
        neighbour_list.append((x+1, y))
    if y != 0:
        neighbour_list.append((x, y-1))
    if y != graph_len-1:
        neighbour_list.append((x, y+1))
    return neighbour_list

# source and target are tuples of (x, y) coordinate
def dijkstra(matrix, source, target):
    x, y = source[0], source[1]
    m_length = len(matrix)
    dist = {(x, y): float("inf") for (x, y) in list(coordinates(m_length, m_length))}
    cloud = {(x, y): float("inf") for (x, y) in list(coordinates(m_length, m_length))}

    # Initialize source vertex values
    dist[(x, y)] = 0
    cloud[(x, y)] = 0
    # Update source vertex's neighbours
    for v in neighbours((x, y), m_length):
        if dist[(x, y)] + matrix[v[0]][v[1]] < dist[v]:
            dist[v] = matrix[v[0]][v[1]]
        cloud[v] = dist[v]

    while cloud:
        # u = the vertex connected to the cloud (but not in it) with the minimum value
        u = min(cloud, key=cloud.get)
        del cloud[u]
        if dist[u] == -1:
            break

        for v in neighbours(u, m_length):
            if cloud.get(v):
                alt = dist[u] + matrix[v[0]][v[1]]
                if alt < dist[v]:
                    dist[v] = alt
                    cloud[v] = dist[v]
                if v == (target[0], target[1]):
                    return dist
    return dist

def main():
    start = time.clock()
    matrix = [[int(x) for x in line.strip().split(",")] for line in open("matrix.txt", "r")]

    length = len(matrix)
    solution = matrix[0][0]
    matrix = dijkstra(matrix, (0, 0), (length-1, length-1))

    print (matrix[(length-1, length-1)] + solution)
    print (time.clock() - start)

if __name__ == '__main__':
    main()
