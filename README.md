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
