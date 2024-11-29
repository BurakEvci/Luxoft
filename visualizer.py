import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle


class ParkingVisualizer:
    def __init__(self, grid, start_x, start_y):
        self.grid = grid
        self.start_x = start_x
        self.start_y = start_y

    def visualize_grid(self, nearest_spots):
        n = len(self.grid)
        m = len(self.grid[0])

        # Matplotlib figür ve eksen oluştur
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.set_xlim(0, m)
        ax.set_ylim(0, n)

        # Grid sınırlarını belirginleştir
        ax.set_xticks(range(m + 1))
        ax.set_yticks(range(n + 1))
        ax.grid(color="black", linewidth=1)
        ax.set_xticklabels([])
        ax.set_yticklabels([])

        # Hücreleri tek tek renklendir
        for i in range(n):
            for j in range(m):
                if self.grid[i][j] == 0:  # Boş park yerleri
                    color = "#30fc03"  # Yeşil
                else:  # Dolu park yerleri
                    color = "red"  # Kırmızı

                # Kareyi çiz
                rect = Rectangle((j, n - i - 1), 1, 1, facecolor=color, edgecolor="black")
                ax.add_patch(rect)

        # Başlangıç noktasına mavi bir daire çiz
        start_circle = Circle((self.start_y + 0.5, n - self.start_x - 0.5), 0.3, color="blue", zorder=1)
        ax.add_patch(start_circle)

        # Başlangıç noktasının en yakın park yeri olup olmadığını kontrol et
        if (self.start_x, self.start_y) in nearest_spots:
            # Başlangıç noktasına yıldız ekle (üstte)
            # Yıldızı dairenin biraz üstüne kaydırıyoruz
            ax.text(self.start_y + 0.5, n - self.start_x - 0.5 + 0.3, "*", color="yellow", ha="center", va="center",
                    fontsize=55, fontweight="bold", zorder=2)

        # Diğer en yakın park yerlerine yıldız ekle
        for x, y in nearest_spots:
            if (x, y) != (self.start_x, self.start_y):
                ax.text(y + 0.5, n - x - 0.5, "*", color="yellow", ha="center", va="center", fontsize=55,
                        fontweight="bold", zorder=2)

        # Görselleştirme
        plt.title("Park Alanı")
        plt.show()
