import math
class point:
    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


    def reset(self) -> None:
        self.move(0, 0)

    def calculate_distance(self, other: "Point") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

    