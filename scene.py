class Scene():
    def __init__(self, columns, rows):
        self.cols = columns
        self.rows = rows
        self.grid = []
        for row in range(self.rows):
            self.grid.append(self.add_row(self.cols))

    def edit_tile(self, column, row, item):
        self.grid[row][column] = item

    def add_row(self, size):
        row = []
        for space in range(size):
            row.append("X")
        return row

    def save(self):
        fname = input("File name: ")
        file = open(fname, 'w')

        for row in self.grid:
            line = ""

            for char in row:
                line += char
                file.write(line)

        file.close()
