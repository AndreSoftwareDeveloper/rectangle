from dataclasses import dataclass, field

from point import Point


@dataclass
class Rectangle:
    width: float
    height: float
    position: Point = field(default_factory=lambda: Point(0.0, 0.0))

    def area(self) -> float:
        return self.width * self.height

    def contains(self, other: "Rectangle") -> bool:
        x_condition = (
                other.position.x.__ge__(self.position.x) and
                (other.position.x + other.width).__le__(self.position.x + self.width)
        )

        y_condition = (
                other.position.y.__ge__(self.position.y) and
                (other.position.y + other.height).__le__(self.position.y + self.height)
        )

        return x_condition and y_condition

    def intersect(self, other: "Rectangle") -> bool:
        x_overlap = (
                self.position.x.__le__(other.position.x + other.width) and
                (self.position.x + self.width).__ge__(other.position.x)
        )

        y_overlap = (
                self.position.y.__le__(other.position.y + other.height) and
                (self.position.y + self.height).__ge__(other.position.y)
        )

        touch_condition = (
                x_overlap and
                y_overlap and
                ((self.position.x + self.width).__eq__(other.position.x) or
                 self.position.x.__eq__(other.position.x + other.width) or
                 (self.position.y + self.height).__eq__(other.position.y) or
                 self.position.y.__eq__(other.position.y + other.height))
        )

        return touch_condition if touch_condition is True else x_overlap and y_overlap
