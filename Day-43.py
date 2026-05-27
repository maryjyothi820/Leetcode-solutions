593.Valid_square
class Solution:
    def validSquare(self, p1, p2, p3, p4):

        def distance(a, b):
            return (a[0] - b[0])**2 + (a[1] - b[1])**2

        points = [p1, p2, p3, p4]

        distances = set()

        for i in range(4):
            for j in range(i + 1, 4):
                distances.add(distance(points[i], points[j]))

        return len(distances) == 2 and 0 not in distances
