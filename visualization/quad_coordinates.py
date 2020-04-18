import xlrd
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

# setting up the canvas
fig = plt.figure()
canvas = FigureCanvasAgg(fig)

# accessing the xlsx file
cwd = os.getcwd()
data_file = 'c:\workspace\shree\MatLab\quad_coordinates.xlsx'
book = xlrd.open_workbook(data_file)
sheet = book.sheet_by_name("Sheet1")

# reading coordinates from the xlsx file
col_x_vals = sheet.col_values(0, 2)
col_y_vals = sheet.col_values(1, 2)

# plotting the coordinates
plt.plot(col_x_vals, col_y_vals)

# customizing the figure
plt.xlabel('x values')
plt.ylabel('y values')
#plt.title('Matplotlib plot')

# saving the figure
canvas.print_figure('images/quad_coordinates.eps')
canvas.print_figure('c:\workspace\shree\LaTex\project_report\images\quad_coordinates.eps')

