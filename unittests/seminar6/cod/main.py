"""Comparison of averages."""
from Average import AverageGenerator, AverageComparator

if __name__ == '__main__':
    print(avg1 := AverageGenerator(5, 1, 100))
    print(avg2 := AverageGenerator(5, 1, 100))
    print(AverageComparator.avg_compare(avg1.average, avg2.average))
    print(AverageComparator.avg_compare(avg2.average, avg1.average))
    print(AverageComparator.avg_compare(avg1.average, avg1.average))
