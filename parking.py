from collections import deque
import random

class ParkingGrid:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.grid = self.generate_grid()
        self.start_x = None
        self.start_y = None

    def generate_grid(self):
        # Grid'i rastgele oluşturuyoruz (0 = boş, 1 = dolu)
        return [[random.choice([0, 1]) for _ in range(self.m)] for _ in range(self.n)]

    def set_start_point(self, x, y):
        """Başlangıç noktasını ayarlama"""
        self.start_x = x
        self.start_y = y

    def bfs(self):
        # BFS için kuyruk oluşturuluyor
        queue = deque([(self.start_x, self.start_y, 0)])  # (x, y, mesafe)
        visited = set()  # Ziyaret edilen hücreler
        visited.add((self.start_x, self.start_y))
        nearest_spots = []
        min_distance = float('inf')

        # BFS
        while queue:
            x, y, dist = queue.popleft()

            # Eğer boş park yeri bulunursa, en yakınları kaydet
            if self.grid[x][y] == 0:
                # Eğer bu park yerine olan mesafe, şimdiye kadar bulduğumuz minimum mesafeden daha kısa ise
                if dist < min_distance:
                    nearest_spots = [(x, y)]  # En yakın park yerine yeni liste
                    min_distance = dist  # Yeni minimum mesafeyi kaydet
                elif dist == min_distance:
                    nearest_spots.append((x, y))  # Aynı mesafede başka park yerleri ekle

            # Komşu hücrelere git
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy

                # Komşu hücre grid içinde olmalı ve henüz ziyaret edilmemeli
                if 0 <= nx < self.n and 0 <= ny < self.m and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist + 1))

        return nearest_spots, min_distance

    def find_nearest_parking(self):
        nearest_spots, distance = self.bfs()
        return nearest_spots, distance

    def display_grid_with_colors(self):
        # Grid'i renkli yazdırma
        RED = '\033[91m'
        GREEN = '\033[92m'
        BLUE = '\033[94m'
        RESET = '\033[0m'

        print("\nRenkli Grid:")
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if (i, j) == (self.start_x, self.start_y):
                    print(f"{BLUE}{cell}{RESET}", end=" ")  # Başlangıç noktasını mavi yazdır
                elif cell == 0:
                    print(f"{GREEN}0{RESET}", end=" ")  # Boş park yerini yeşil yazdır
                else:
                    print(f"{RED}1{RESET}", end=" ")  # Dolu park yerini kırmızı yazdır
            print()
