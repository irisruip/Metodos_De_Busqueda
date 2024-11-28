# Representamos el grafo como un diccionario donde cada nodo apunta a sus vecinos con sus valores heurísticos
graph = {
    "A": [("B", 8), ("C", 7)],
    "B": [("D", 9)],
    "C": [("E", 9), ("F", 6)],
    "D": [("G", 0), ("H", 1)],
    "F": [("H", 1), ("I", 0)],
    "E": [],
    "G": [],
    "H": [],
    "I": []
}

# Función para el método de Escalada por Máxima Pendiente
def simple_hill_climbing(graph, start, goals):
    visited = []
    current = start
    while current not in goals:
        visited.append(current)
        neighbors = graph[current]
        if not neighbors:
            break  # Si no hay vecinos, terminamos
        # Seleccionamos el vecino con la heurística más baja
        current = min(neighbors, key=lambda x: x[1])[0]
    visited.append(current)
    return visited


# Función para el método de Escalada Simple
def steepest_ascent_hill_climbing(graph, start, goals):
    visited = []
    current = start
    while current not in goals:
        visited.append(current)
        neighbors = graph[current]
        if not neighbors:
            break  # Si no hay vecinos, terminamos
        current = neighbors[0][0]  # Selección del primer vecino (izquierda a derecha)
    visited.append(current)
    return visited



# Nodo inicial y nodos meta
start_node = "A"
goal_nodes = {"G", "I"}

# Menú interactivo
def menu():
    while True:
        print("\n--- Resolución del Ejercicio N° 3 ---")
        print("1. Método de Escalada Simple")
        print("2. Método de Escalada por Máxima Pendiente")
        print("3. Comparar ambos métodos")
        print("4. Salir")
        
        option = input("Selecciona una opción: ")
        
        if option == "1":
            simple_path = simple_hill_climbing(graph, start_node, goal_nodes)
            print("\nResultado con Método de Escalada Simple:")
            print("Secuencia de nodos visitados:", " → ".join(simple_path))
        elif option == "2":
            steepest_path = steepest_ascent_hill_climbing(graph, start_node, goal_nodes)
            print("\nResultado con Método de Escalada por Máxima Pendiente:")
            print("Secuencia de nodos visitados:", " → ".join(steepest_path))
        elif option == "3":
            simple_path = simple_hill_climbing(graph, start_node, goal_nodes)
            steepest_path = steepest_ascent_hill_climbing(graph, start_node, goal_nodes)
            print("\nComparación de métodos:")
            print("Método de Escalada Simple:", " → ".join(simple_path))
            print("Método de Escalada por Máxima Pendiente:", " → ".join(steepest_path))
        elif option == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el menú
menu()