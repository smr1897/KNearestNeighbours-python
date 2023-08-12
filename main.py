import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

points = {"blue": [[2,4],[1,3],[2,3],[3,2],[2,1]],
          "red": [[5,6],[4,5],[4,6],[6,6],[5,4]]}

new_point = [3,3]

def euclidian_distance(x,y):
    np.sqrt(np.sum(np.array(x) - np.array(y) ** 2))

class KNearestNeighbours:

    def __init__(self,k=3):
        self.k = k
        self.point = None

    def fir(self,points):
        self.points = points

    def predict(self,new_point):
        distances = []

        for category in self.points:
            for point in self.points[category]:
                distance = euclidian_distance(point,new_point)
                distances.append(distance)

        categories = [category[1] for category in sorted(distances)[:self.k]]
        result = Counter(categories).most_common(1)[0][0]
        return result