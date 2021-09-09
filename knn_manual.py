import math
import statistics

# variabel yang digunakan 
train_input = [[11, 26], [15, 29], [19, 28], [18, 30], [
    16, 26], [23, 25], [25, 22], [21, 24], [23, 25], [29, 24]]
train_target = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
nama = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
k = 3
input = [19, 25]
panjang_kelas = len(train_target)

# jarak euclidean
print('------ nilai euclidean ------')
var = []
for i in range(panjang_kelas):
    euclidean = math.sqrt(
        (train_input[i][0]-input[0])**2 + (train_input[i][1]-input[1])**2)
    var.append([euclidean, nama[i], train_target[i]])
    print(var[i])

# mengurutkan dari nilai terkecil
print('------ Diurutkan dari terdekat ------')
var.sort()
print(var)

modus = []
print('------ diambil data teratas sesuai nilai k ------')
for i in range(k):
    print(var[i][2])
    
    modus.append(var[i][2])

klasifikasi = statistics.mode(modus)

print('------ hasil klasifikasi ------')
print(klasifikasi)