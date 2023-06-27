# UAS-PAA-II

# Hasil Run program pengurutan
Pilihan pengurutan:
1. Bubble Sort
2. Insertion Sort
Masukkan pilihan (1/2): 1

# --- Bubble Sort ---
Before sorting:
[12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7, 26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21, 17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59, 40, 7, 41, 81]
After sorting:
[1, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7, 8, 9, 9, 10, 12, 15, 15, 17, 18, 19, 19, 20, 21, 21, 21, 22, 23, 24, 25, 26, 31, 31, 32, 32, 33, 33, 36, 36, 39, 39, 40, 40, 40, 41, 43, 43, 44, 46, 48, 49, 50, 53, 54, 55, 59, 60, 62, 63, 64, 68, 71, 74, 77, 79, 81, 84, 85, 88, 89, 90, 90, 95, 97, 99]
Execution time: 0.000000 seconds
--- Bubble Sort ---
First 5 iterations:
1 1 1 2 3 
Last 5 iterations:
90 90 95 97 99 
Execution time: 0.000000 seconds

# --- Insertion Sort ---
Before sorting:
[12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7, 26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21, 17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59, 40, 7, 41, 81]
After sorting:
[1, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7, 8, 9, 9, 10, 12, 15, 15, 17, 18, 19, 19, 20, 21, 21, 21, 22, 23, 24, 25, 26, 31, 31, 32, 32, 33, 33, 36, 36, 39, 39, 40, 40, 40, 41, 43, 43, 44, 46, 48, 49, 50, 53, 54, 55, 59, 60, 62, 63, 64, 68, 71, 74, 77, 79, 81, 84, 85, 88, 89, 90, 90, 95, 97, 99]
Execution time: 0.000000 seconds
--- Insertion Sort ---
First 5 iterations:
1 1 1 2 3 
Last 5 iterations:
90 90 95 97 99 
Execution time: 0.000000 seconds

# Analisis Program Bubble&Insertion
Berdasarkan hasil run program, kita dapat melakukan analisis algoritma untuk mengevaluasi apakah ini termasuk dalam kasus terburuk (worst case), kasus terbaik (best case), atau kasus rata-rata (average case).

Worst case:
Worst case pada Bubble dan Insertion Sort terjadi ketika elemen-elemen dalam array terurut dalam urutan terbalik. Pada contoh ini, array awal tidak terurut dalam urutan terbalik, sehingga hasil run tidak termasuk dalam worst case.

Best case:
Best case pada Bubble dan Insertion Sort terjadi ketika array awal sudah terurut secara ascending. Pada contoh ini, array awal tidak terurut secara ascending, sehingga hasil run tidak termasuk dalam best case.

Average case:
Average case pada Bubble dan Insertion Sort terjadi ketika elemen-elemen dalam array memiliki urutan yang acak. Pada contoh ini, array awal memiliki elemen-elemen yang acak, sehingga hasil run dapat dianggap sebagai representasi dari average case.

Dengan demikian, berdasarkan hasil run program, kasus ini termasuk dalam average case untuk Bubble dan Insertion Sort.


# Hasil Run program pengurutan
Pilihan penghitungan shortest path:
1. TSP (Traveling Salesman Problem) - Prim's Algorithm
2. Dijkstra
Masukkan pilihan (1/2): 1
--- TSP (Traveling Salesman Problem) - Prim's Algorithm ---
Shortest path: ['A', 'B', 'G', 'E', 'C', 'F', 'H', 'D', 'A']
![image](https://github.com/Ohwdyaa/UAS-PAA-II/assets/107343788/e24b2239-51cf-4a09-a44a-c1616a3b1e56)

--- Dijkstra ---
Masukkan titik awal: A
Shortest path from A to A : ['A']
Shortest path from A to B : ['A', 'B']
Shortest path from A to G : ['A', 'G']
Shortest path from A to C : ['A', 'G', 'C']
Shortest path from A to D : ['A', 'B', 'D']
Shortest path from A to E : ['A', 'G', 'E']
Shortest path from A to F : ['A', 'G', 'F']
Shortest path from A to H : ['A', 'G', 'H']

# Analisis TSP&Dijkstra
# 1. TSP (Traveling Salesman Problem)
   Berdasarkan hasil run menggunakan algoritma TSP dengan Prim's Algorithm yang diberikan, yaitu jalur terpendek ['A', 'B', 'G', 'E', 'C', 'F', 'H', 'D', 'A'], kita dapat melakukan analisis algoritma sebagai berikut:

a. Worst case: Algoritma Prim's memiliki kompleksitas waktu O(|V|^2), di mana |V| adalah jumlah simpul (kota) dalam grafik. Dalam kasus ini, terdapat 8 simpul (A, B, C, D, E, F, G, H), sehingga kompleksitas waktu algoritma Prim's adalah O(8^2) = O(64), yang dapat dianggap sebagai kompleksitas waktu tetap. Oleh karena itu, tidak ada perbedaan signifikan dalam kinerja algoritma antara kasus terbaik dan kasus terburuk.

b. Best case: Karena algoritma Prim's memiliki kompleksitas waktu tetap, tidak ada perbedaan dalam kinerja algoritma antara kasus terbaik dan kasus terburuk. Dalam hal ini, hasil run yang diberikan ['A', 'B', 'G', 'E', 'C', 'F', 'H', 'D', 'A'] adalah jalur terpendek yang ditemukan oleh algoritma Prim's.

c. Average case: Algoritma Prim's memiliki kompleksitas waktu tetap, sehingga tidak ada perbedaan kinerja antara kasus terbaik, terburuk, dan rata-rata. Oleh karena itu, hasil run yang diberikan ['A', 'B', 'G', 'E', 'C', 'F', 'H', 'D', 'A'] adalah hasil rata-rata yang ditemukan oleh algoritma Prim's.

Dalam kasus ini, algoritma Prim's memberikan solusi jalur terpendek yang sama setiap saat karena grafiknya relatif kecil dan tidak memiliki perubahan yang signifikan dalam kompleksitas waktu. Namun, penting untuk dicatat bahwa hasil analisis ini hanya berlaku dalam konteks grafik yang diberikan. Untuk masalah TSP dengan grafik yang lebih besar atau berbeda, kompleksitas dan performa algoritma dapat berbeda.

# 2. Dijkstra
   Berikut adalah analisis algoritma berdasarkan hasil run program:

a. Worst case:
Worst case untuk algoritma Dijkstra terjadi ketika semua titik dalam grafik saling terhubung dengan bobot yang besar. Dalam kasus ini, program akan melakukan pencarian jalur terpendek dari titik awal ke semua titik lainnya. Dalam contoh ini, tidak ada jalur yang membutuhkan langkah yang lebih dari memeriksa semua titik. Oleh karena itu, tidak ada kasus terburuk yang signifikan dalam contoh ini.

b. Best case:
Best case untuk algoritma Dijkstra terjadi ketika ada jalur terpendek langsung dari titik awal ke titik tujuan. Dalam contoh ini, jika titik tujuan hanya satu langkah dari titik awal, program akan langsung menemukan jalur terpendek tanpa perlu memeriksa titik lainnya. Misalnya, jalur terpendek dari A ke B adalah ['A', 'B'].

c. Average case:
Rata-rata kasus untuk algoritma Dijkstra terjadi ketika terdapat beberapa titik tujuan yang berbeda dengan jarak yang bervariasi dari titik awal. Dalam contoh ini, program mencari jalur terpendek dari titik awal ke semua titik lainnya. Oleh karena itu, rata-rata kasus dalam contoh ini adalah mencari jalur terpendek dari titik awal ke setiap titik lainnya.

Dalam keseluruhan, program menggunakan algoritma Dijkstra yang efisien untuk mencari jalur terpendek dari titik awal ke semua titik lainnya dalam grafik yang diberikan.
