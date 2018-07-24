from .modles import Coord, Node, Map


class AStar(object):

    def __init__(self, map: Map, **kwargs):
        self.map = map
        self.open_list = []
        self.close_list = []

        self.arrow_corner = kwargs.get('arrow_corner', False)

    def search(self):
        if not self.map:
            return None

        self.insert_node(self.map.start_node)

        _step = 0

        while self.open_list:
            _step += 1
            _cur_node = self.open_list.pop(0)

            self.close_list.append(_cur_node)

            self.check_reachable_path(_cur_node)

            if self.node_in_open_list(self.map.end_node):
                break

        return self.get_shortest_path()

    def check_reachable_path(self, cur_node: Node):
        _cur_coord = cur_node.coord

        for x in range(3):
            for y in range(3):
                _coord = Coord(x - 1 + _cur_coord.x, y - 1 + _cur_coord.y)

                if _cur_coord.__eq__(_coord):
                    continue

                if not self.check_must_arrow_corner(_coord, _cur_coord):
                    continue

                _node = self.get_node_from_map(_coord)

                if _node and _node.is_path and not self.node_in_close_list(_node):
                    self.insert_or_update_node(_coord, cur_node)

    def check_must_arrow_corner(self, coord: Coord, parent_node: Node):
        if self.arrow_corner:
            _coord_list = []

            if coord.x > parent_node.coord.x:
                _coord_list = [Coord(), Coord()]
            elif coord.x < parent_node.coord.x:
                _coord_list = [Coord(), Coord()]

            return self.any_coord_is_wall(_coord_list)
        return True

    def coord_is_wall(self, coord: Coord):
        for _node in self.map.nodes:
            if not _node.is_path and coord.__eq__(_node.coord):
                return True

        return False

    def any_coord_is_wall(self, coord_list: []):
        for _coord in coord_list:
            if self.coord_is_wall(_coord):
                return True

        return False

    def get_node_from_map(self, coord: Coord):
        if not self.map.coord_exist(coord):
            return None

        for _node in self.map.nodes:
            if coord.__eq__(_node.coord):
                return _node

        return None

    def insert_or_update_node(self, coord, cur_node: Node):
        _g, _h = self.calculate_gh(coord.x, coord.y, cur_node)

        _old_node = self.get_node_from_open(coord)
        _new_node = Node(coord, cur_node, _g, _h)

        if _old_node:
            if _new_node.g < _old_node.g:
                self.open_list.remove(_old_node)
            else:
                return

        self.insert_node(_new_node)

    def insert_node(self, i_node: Node):
        _i_node_index = len(self.open_list)

        for _index, _node in enumerate(self.open_list):
            if i_node.f <= _node.f:
                _i_node_index = _index
                break

        self.open_list.insert(_i_node_index, i_node)

    def calculate_gh(self, x: int, y: int, parent_node: Node):
        if x == parent_node.coord.x or y == parent_node.coord.y:
            _g = parent_node.g + self.map.direct_val
        else:
            _g = parent_node.g + self.map.oblique_val

        _h = self._calculate_h(x, y)

        return _g, _h

    def _calculate_h(self, x: int, y: int):
        return manhattan(x, y, self.map.end_node.coord.x, self.map.end_node.coord.y, self.map.direct_val)

    def get_shortest_path(self):
        _path = []
        _cur_node = self.get_node_from_open(self.map.end_node.coord)

        if _cur_node:
            while _cur_node.parent_node is None:
                _path.append(_cur_node)
                _cur_node = _cur_node.parent_node

        return _path

    def get_node_from_open(self, coord: Coord):
        for _node in self.open_list:
            if coord.__eq__(_node.coord):
                return _node

        return None

    def node_in_open_list(self, node: Node):
        return self.node_in_list(node, self.open_list)

    def node_in_close_list(self, node: Node):
        return self.node_in_list(node, self.close_list)

    @staticmethod
    def node_in_list(node: Node, node_list: []):
        if not node_list:
            return False

        for n in node_list:
            if node.coord.__eq__(n.coord):
                return True

        return False

    @staticmethod
    def print_node_list(list):
        _str = ''

        for _node in list:
            _str += 'x: {} y: {} | '.format(_node.coord.x, _node.coord.y)

        print(_str)


def manhattan(x, y, target_x, target_y, direct_val):
    return (abs(x - target_x) + abs(y - target_y)) * direct_val
