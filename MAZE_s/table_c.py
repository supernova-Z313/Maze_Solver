class Table:
    def __init__(self, x=10, y=10):
        # 0:empty  1:wall  2:full  3:start  4:end  (*:road)
        self.x = x
        self.y = y
        self.start = None
        self.end = None
        self.now_layer = []
        self.steps = []
        self.table = {(i, j): [0] for j in range(y)for i in range(x)}

    def add_border(self):
        for i in self.table:
            if i[0] in [0, self.x-1] or i[1] in [0, self.y-1]:
                self.table[i] = [1]

    def add_wall(self, *args):
        for i in args:
            self.table[i] = [1]

    def add_st_end(self, start=(1, 1), end=(8, 8)):
        self.start = start
        self.end = end
        self.now_layer.append(start)
        self.table[start] = [3]
        self.table[end] = [4]

    def block_round(self, block=(1, 1)):
        list_f_b = []
        ending = None
        e1, e2 = block
        for i in [0, 1]:
            for j in [1, 0]:
                if i == 1 and j == 1:
                    continue
                if self.table.get((e1+i, e2+j)) == [0]:
                    list_f_b.append((e1+i, e2+j))
                if self.table.get((e1-i, e2-j)) == [0]:
                    list_f_b.append((e1-i, e2-j))
                if self.table.get((e1-i, e2-j)) == [4]:
                    ending = (e1-i, e2-j)
                if self.table.get((e1+i, e2+j)) == [4]:
                    ending = (e1+i, e2+j)
        return list_f_b, ending

    def processing(self):
        while True:
            next_g = []
            finish = False
            for i in self.now_layer:
                next_l, position = self.block_round(i)
                if position is not None:
                    self.table[position] = [4, i]
                    self.now_layer.clear()
                    finish = True
                else:
                    for j in next_l:
                        self.table[j] = [2, i]
                        next_g.append(j)
            if finish:
                return finish
            elif not self.now_layer:
                return finish
            else:
                self.now_layer.clear()
                self.steps.append(next_g.copy())
                self.now_layer = next_g.copy()

    def step_by_step(self):
        return self.steps

    def road(self):
        road_l = []
        last_block = self.end
        while True:
            if self.table[self.table[last_block][1]] == [3]:
                break
            road_l.append(self.table[last_block][1])
            last_block = self.table[last_block][1]
        road_l.reverse()
        return road_l

    def add_road(self):
        final_l = self.road()
        for i in final_l:
            self.table[i][0] = "."

    def dict_shape(self):
        return self.table

    def print_shape(self):
        shape = self.dict_shape()
        for ind, i in enumerate(shape, start=1):
            print(shape[i][0], end=" ")
            if ind % self.x == 0:
                print()

    def print_beautiful_shape(self):
        shape = self.dict_shape()
        shape_c = []
        line_l = []
        for ind, i in enumerate(shape, start=1):
            if shape[i][0] in [2, 0]:
                print(" ", end=" ")
                line_l.append(" ")
            elif shape[i][0] == 3:
                print("S", end=" ")
                line_l.append("S")
            elif shape[i][0] == 4:
                print("E", end=" ")
                line_l.append("E")
            else:
                print(shape[i][0], end=" ")
                line_l.append(f"{shape[i][0]}")
            if ind % self.x == 0:
                print()
                shape_c.append(line_l.copy())
                line_l.clear()
        return shape_c


if __name__ == "__main__":
    Table()
