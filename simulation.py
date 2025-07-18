from grid import Grid

class Simulation:
    def __init__(self, width, height, cell_size):
        self.grid = Grid(width, height, cell_size)
        self.temp_grid = Grid(width, height, cell_size)
        self.rows = height // cell_size
        self.colums = width // cell_size
        self.run = False


    def draw(self, window):
        self.grid.draw(window)


    def count_live_neighbors(self, grid, row, column):
        live_neighbors = 0

        neighbors_offsets = [ (-1,-1), (-1,0), (-1,1), (0,-1), (1,-1), (1,0), (1,1) ]
        for offset in neighbors_offsets:
            new_row = (row + offset[0]) % self.rows
            new_column = (column + offset[1]) % self.colums
            if self.grid.cells[new_row][new_column] == 1:
                live_neighbors += 1

        return live_neighbors

    
    def update(self):
        ...


    def is_running(self):
        return self.run

    
    def start(self):
        self.run = True


    def stop(self):
        self.run = False


    def clear(self):
        if self.is_running() == False:
            self.grid.clear()


    def create_random_state(self):
        if self.is_running() == False:
            self.grid.fill_random()


    def toggle_cell(self, row, column):
        if self.is_running() == False:
            self.grid.toggle_cell(row_column)
