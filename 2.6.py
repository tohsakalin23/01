class Shape:
    """图形基类"""
    _count=0
    def __init__(self):
        self.__area=None
        self._dimensions=None
        Shape._count+=1
    def _calc_area(self):
        """计算面积（子类必须重写）"""
        raise NotImplementedError("子类必须实现此方法")
    def get_area(self):
        """公开方法：获取面积"""
        if self.__area is None:
            self.__area=self._calc_area()
        return self.__area
    @classmethod
    def get_total_count(cls):
        return cls._count
    def __str__(self):
        return f"{self.__class__.__name__}(area={self.get_area():.2f})"
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self._dimensions={"radius": radius}
    def _calc_area(self):
        radius=self._dimensions["radius"]
        return 3.14159 * radius * radius
class Rectangle(Shape):
    def __init__(self,width,height):
        super().__init__()
        self._dimensions={"width": width, "height": height}
    def _calc_area(self):
        width=self._dimensions["width"]
        height=self._dimensions["height"]
        return width * height
def test_shapes():
    print("=== 图形计算器测试 ===\n")
    circle=Circle(5)
    rectangle=Rectangle(4, 6)
    shapes=[circle, rectangle]
    for shape in shapes:
        area=shape.get_area()
        print(f"{shape}:面积={area:.2f}")
    print(f"\n创建的图形总数: {Shape.get_total_count()}")
if __name__=="__main__":
    test_shapes()