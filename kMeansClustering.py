
import numpy as np
import random


def distance(point1, point2):
    sum = 0.0
    for i in range(len(point1)):
        sum += pow(point1[i] - point2[i], 2)
    sum = sum ** 0.5
    return sum


def cluster(points, k):
    mins = np.min(points, axis=0)
    maxs = np.max(points, axis=0)

    clusters = np.array([np.array(points[i]) for i in range(k)])
    prev = []
    prev = np.array(prev)
    error = -1

    while (abs(error) > 0):
        labels = {}
        for i in range(k):
            labels[i + 1] = []
        for point in points:
            dists = []
            for clust in clusters:
                dists.append(distance(point, clust))
            labels[np.argmin(dists) + 1].append(point)
        prev = clusters

        try:
            clusters = np.array([np.mean(labels[i + 1], axis=0) for i in range(k)])
        except ValueError:
            clusters = prev
            break

        error = np.mean(np.mean(clusters - prev, axis=0))

    return clusters




