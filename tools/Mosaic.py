class Mosaic:
    @staticmethod
    def generate_array(x, y, element=None):
        return [[element for _ in range(x)] for _ in range(y)]

    @staticmethod
    def fill_with_string(array, start, end, string, pad=(0, 0)):
        start_x, start_y = start[0] - 1 + pad[0], start[1] - 1 + pad[1]
        end_x, end_y = end[0] - 1, end[1] - 1
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                array[y][x] = string

    @staticmethod
    def fill_row_with_array(array, start, end, fill, pad=(0, 0)):
        start_x, start_y = start[0] - 1 + pad[0], start[1] - 1 + pad[1]
        end_x, end_y = end[0] - 1, end[1] - 1
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                index = int((x - start_x) / int((end_x - start_x + 1) / len(fill)))
                if len(fill) > index:
                    array[y][x] = fill[index]

    @staticmethod
    def fill_col_with_array(array, start, end, fill, pad=(0, 0)):
        start_x, start_y = start[0] - 1 + pad[0], start[1] - 1 + pad[1]
        end_x, end_y = end[0] - 1, end[1] - 1
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                index = int((y - start_y) / int((end_y - start_y + 1) / len(fill)))
                if len(fill) > index:
                    array[y][x] = fill[index]
