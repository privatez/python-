import unittest

from core.algorithm.astar import Node, Coord, Map, AStar


class Test(unittest.TestCase):

    def test_astar(self):
        _width = 9
        _height = 7

        _start_node = Node(Coord(2, 3), None, 0, 0)
        _end_node = Node(Coord(6, 3), None, 0, 0)

        _node_list = []
        _wall_coord_list = [Coord(4, 2), Coord(4, 3), Coord(4, 4)]

        for x in range(_width):
            for y in range(_height):
                _coord = Coord(x, y)
                _is_path = True

                for _wall_coord in _wall_coord_list:
                    if _coord.__eq__(_wall_coord):
                        _is_path = False

                _node_list.append(Node(_coord, None, 0, 0, _is_path))

        from core.algorithm.astar import Map
        astar = AStar(Map(_node_list, _width, _height, _start_node, _end_node))
        self.assertListEqual(astar.search(), [])


if __name__ == '__main__':
    unittest.main()
