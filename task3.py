import heapq

def dijkstra(graph, start_vertex):
    # Відстані: початково нескінченність
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0

    # Пріоритетна черга (мінімальна купа)
    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Розглядаємо лише ті вершини, які ще не були оброблені
        if current_distance > distances[current_vertex]:
            continue

        # Проходимо по сусідах поточної вершини
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо знайдений шлях коротший, оновлюємо відстань та купу
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Приклад графа (словник суміжності)
graph = {
    'Kyiv': {'Zhytomyr': 140, 'Odessa': 475, 'Cherkasy': 192, 'Kropyvnytskyi': 320},
    'Zhytomyr': {'Kyiv': 140, 'Rivne': 131, 'Khmelnytskyi': 159, 'Vinnytsia': 128},
    'Odessa': {'Kyiv': 475, 'Vinnytsia': 318, 'Mykolaiv': 133, 'Kropyvnytskyi': 294},
    'Cherkasy': {'Kyiv': 192, 'Kropyvnytskyi': 222, 'Dnipro': 218},
    'Kropyvnytskyi': {'Kyiv': 320, 'Vinnytsia': 202, 'Odessa': 294, 'Mykolaiv': 222, 'Dnipro': 252, 'Cherkasy': 222},
    'Vinnytsia': {'Khmelnytskyi': 136, 'Kropyvnytskyi': 202, 'Zhytomyr': 128, 'Chernivtsi': 202, 'Odessa': 318},
    'Rivne': {'Zhytomyr': 131, 'Lutsk': 70, 'Lviv': 211, 'Ternopil': 159, 'Khmelnytskyi': 194},
    'Khmelnytskyi': {'Vinnytsia': 136, 'Zhytomyr': 159, 'Rivne': 194, 'Ternopil': 68, 'Chernivtsi': 215},
    'Lutsk': {'Rivne': 70, 'Lviv': 154, 'Ternopil': 219},
    'Lviv': {'Rivne': 211, 'Lutsk': 154, 'Ternopil': 130, 'Uzhhorod': 187, 'IFrank': 141},
    'Mykolaiv': {'Odessa': 133, 'Kherson': 66, 'Kropyvnytskyi': 222, 'Dnipro': 302},
    'IFrank': {'Lviv': 141, 'Uzhhorod': 120, 'Ternopil': 131, 'Chernivtsi': 261},
    'Uzhhorod': {'Lviv': 187, 'IFrank': 120},
    'Chernivtsi': {'Vinnytsia': 202, 'IFrank': 261, 'Ternopil': 179, 'Khmelnytskyi': 215},
    'Ternopil': {'Rivne': 159, 'Lutsk': 219, 'Lviv': 130, 'IFrank': 131, 'Chernivtsi': 179, 'Khmelnytskyi': 68},
    'Dnipro': {'Mykolaiv': 302, 'Kropyvnytskyi': 252, 'Zaporizhzhia': 85, 'Cherkasy': 218},
    'Zaporizhzhia': {'Dnipro': 85},
    'Kherson': {'Mykolaiv': 66}
}


# Запускаємо алгоритм з вершини 'A'
print(dijkstra(graph, 'Kyiv'))