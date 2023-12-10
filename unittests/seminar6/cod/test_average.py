"""Comparison of averages."""
import pytest
from Average import AverageGenerator, AverageComparator


def test_find_average_type_error():
    """Test type error."""
    with pytest.raises(TypeError):
        AverageGenerator('Not list')


def test_find_average_empty_error():
    """Test empty error."""
    with pytest.raises(ValueError):
        AverageGenerator()


def test_find_average_size_error():
    """Test size error."""
    with pytest.raises(ValueError):
        AverageGenerator(1, 10, 100)


def test_find_average_checker_integration():
    """All tests integration."""
    avg1 = AverageGenerator(5, 1, 100)
    assert isinstance(avg1, AverageGenerator)


def test_find_average_end_to_end():
    """End-to-end test"""
    avg1 = AverageGenerator(5, 1, 100)
    avg2 = AverageGenerator(5, 1, 100)
    assert AverageComparator.avg_compare(avg1.average, avg2.average)


@pytest.mark.parametrize("first_avg, second_avg, expected",
                         [(10, 5, 'First average is gross than second.'),
                          (5, 10, 'First average is less than second.'),
                          (10, 10, 'Averages are equal.')])
def test_is_prime(first_avg, second_avg, expected):
    """Parametrized tests for comparator."""
    assert AverageComparator.avg_compare(first_avg, second_avg) == expected
