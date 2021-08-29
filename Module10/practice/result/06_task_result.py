id_points = [(3, 17), (5, 42), (1, 13), (2, 25), (5, 23), (4, 100), (7, 78)]

id_points.sort(key=lambda points: points[0])
id_points.sort(key=lambda points: points[1], reverse=True)

print(id_points)
