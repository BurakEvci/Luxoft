from parking import ParkingGrid
from visualizer import ParkingVisualizer

def main():
    # Kullanıcıdan grid boyutlarını al
    n = int(input("Grid için satır sayısını girin: "))
    m = int(input("Grid için sütun sayısını girin: "))

    # ParkingGrid sınıfını kullanarak nesne oluştur
    parking = ParkingGrid(n, m)

    # Park alanını ekrana yazdır (renkli)
    parking.display_grid_with_colors()

    # Kullanıcıdan başlangıç noktasını al ve BFS ile en yakın park yerini bul
    while True:
        while True:
            start_x = int(input("Başlangıç noktasının y koordinatını girin: "))
            start_y = int(input("Başlangıç noktasının x koordinatını girin: "))

            # Koordinatların grid içinde olup olmadığını kontrol et
            if 0 <= start_x < n and 0 <= start_y < m:
                break
            else:
                print(f"Hatalı giriş! Lütfen 0 ile {n - 1} ve 0 ile {m - 1} arasında bir koordinat girin.")

        # ParkingGrid sınıfını kullanarak nesne oluştur ve başlangıç noktasını ata
        parking.set_start_point(start_x, start_y)

        # En yakın park yerlerini bul ve sonucu yazdır
        nearest_spots, distance = parking.find_nearest_parking()
        if nearest_spots:
            print(f"\nEn Yakın Park Yerleri: {nearest_spots}")
            print(f"Mesafe: {distance}")
        else:
            print("\nBoş park yeri bulunamadı!")

        # ParkingVisualizer sınıfını kullanarak görselleştir
        visualizer = ParkingVisualizer(parking.grid, start_x, start_y)
        visualizer.visualize_grid(nearest_spots)

        # Kullanıcıya başka bir koordinat girmek isteyip istemediğini sor
        while True:
            continue_input = input("\nBaşka bir koordinat girmek ister misiniz? (Evet/Hayır): ").strip().lower()
            if continue_input == 'evet':
                break
            elif continue_input == 'hayır':
                return  # Programı sonlandır
            else:
                print("Geçersiz giriş! Lütfen 'Evet' ya da 'Hayır' yazın.")

if __name__ == "__main__":
    main()
