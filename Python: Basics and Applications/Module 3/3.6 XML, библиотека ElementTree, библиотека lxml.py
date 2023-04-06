"""Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

Пример:

<cube color="blue">
  <cube color="red">
    <cube color="green">
    </cube>
  </cube>
  <cube color="red">
  </cube>
</cube>

Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1. Кубики,
расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3.
И т. д.

Ценность цвета равна сумме ценностей всех кубиков этого цвета.

Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
Sample Input:

<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>
Sample Output:

4 3 1"""

from xml.etree.ElementTree import XMLParser


class MaxDepth():                     # The target object of the parser
    depth = 0
    cubes = {'red': 0, 'green': 0, 'blue': 0}
    def start(self, tag, attrib):
        self.depth += 1
        self.cubes[attrib['color']] += self.depth
    def end(self, tag):
        self.depth -= 1
    def data(self, data):
        pass
    def close(self):
        return print(*self.cubes.values())


target = MaxDepth()
parser = XMLParser(target=target)
exampleXml = input()
parser.feed(exampleXml)
parser.close()
