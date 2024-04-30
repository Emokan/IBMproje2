import math

# Noktaların Tanımlanması
points = [(1, 2), (3, 5), (-2, 7), (8, -1)]

# Öklid Mesafesi İçin Bir Fonksiyon Yazma
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Mesafelerin Hesaplanması
distances = []
min_distance = float('inf')
min_points = ()

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)
        if distance < min_distance:
            min_distance = distance
            min_points = (points[i], points[j])

# Minimum Mesafenin Bulunması ve İlgili Noktaların Yazdırılması
print("Minimum mesafe:", min_distance)
print("İlgili noktalar:", min_points)

