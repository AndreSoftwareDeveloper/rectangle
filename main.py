import pytest
from point import Point
from rectangle import Rectangle


@pytest.fixture
def rectangle1():
    return Rectangle(width=3.0, height=4.0, position=Point(0.0, 0.0))


@pytest.fixture
def rectangle2():
    return Rectangle(width=2.0, height=2.0, position=Point(2.0, 2.0))


@pytest.fixture
def rectangle3():
    return Rectangle(width=3.0, height=3.0, position=Point(5.0, 2.0))


def test_intersect(rectangle1, rectangle2, rectangle3):
    assert rectangle1.intersect(rectangle2) is True
    assert rectangle1.intersect(rectangle3) is False
    assert rectangle2.intersect(rectangle3) is False
    assert rectangle1.intersect(Rectangle(width=3.0, height=2.0, position=Point(0.0, 4.0))) is True
    assert rectangle1.intersect(Rectangle(width=1.0, height=1.0, position=Point(5.0, 5.0))) is False


def test_area(rectangle1, rectangle2, rectangle3):
    assert rectangle1.area() == 12.0
    assert rectangle2.area() == 4.0
    assert rectangle3.area() == 9.0


def test_contains(rectangle1, rectangle2, rectangle3):
    assert rectangle1.contains(rectangle2) is False
    assert rectangle1.contains(rectangle3) is False
    assert rectangle2.contains(rectangle1) is False
    assert rectangle1.contains(Rectangle(width=3.0, height=2.0, position=Point(0.0, 4.0))) is False


if __name__ == "__main__":
    pytest.main()
