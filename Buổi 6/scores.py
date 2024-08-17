from statistics import mean, median, mode

diem_so = [8, 9, 7, 6, 8, 8, 9, 9, 7, 8]

gia_tri_trung_binh = mean(diem_so)
print(f"Điểm trung bình : {gia_tri_trung_binh}")

median = median(diem_so)
print(f"Điểm ở giữa: {median}")

try:
    mode = mode(diem_so)
    print(f"Điểm xuất hiện nhiều nhất: {mode}")
except:
    print("Không có.")