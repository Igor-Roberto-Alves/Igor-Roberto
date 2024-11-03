def find_lake(matrix):
    def neighbors(index):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),(1,1),(1,-1),(-1,1),(-1,-1)]
        neighbors = []
        for dx, dy in directions:
            x, y = index[0] + dx, index[1] + dy
            if 0 <= x < n and 0 <= y < m:
                neighbors.append((x, y))
        return neighbors

    n = len(matrix)
    m = len(matrix[0])
    visitados = set()  
    count = 0
    water = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '0' and (i, j) not in visitados:
                count += 1
                fila = [(i, j)]
                ilha = set()
                ilha.add((i,j))
                while fila:
                    atual = fila.pop(0)
                    if atual not in visitados:
                        visitados.add(atual)
                        for vizinho in neighbors(atual):
                            if matrix[vizinho[0]][vizinho[1]] == '0' and vizinho not in visitados:
                                ilha.add((vizinho[0],vizinho[1]))
                                fila.append(vizinho)

                lista_ilha = [v for v in ilha]
                lista_ilha.sort()
                water.append(lista_ilha)
                
    for conjunto in water:
        for zero in conjunto: #não terá zeros nas bordas
            if zero[0] == 0 or zero[0] == n-1 or zero[1] == 0 or zero[1] == m-1:
                water.remove(conjunto)
                break
            

    
    return water

# Testando com a matriz
matriz = [
    ['1', '1', '1', '1', '1'],
    ['1', '0', '0', '0', '1'],
    ['0', '1', '0', '1', '1'],
    ['1', '1', '0', '0', '1'],
    ['1', '1', '1', '1', '1']
]

print(find_lake(matriz))