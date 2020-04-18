clc
clear all

% min x-value: spaced by 1: max x-value
x = -10: 1: 10;
% function
y = x'.^2'
plot(x, y)

% column labels for the table values
col_header = {'x', 'y'};

% writing coordinate values into xlsx file
xlswrite('quad_coordinates.xlsx', [x(:), y(:)], 'Sheet1', 'A2');
xlswrite('quad_coordinates.xlsx', col_header, 'Sheet1', 'A2');

% saves the plot as png
saveas(gcf,'quad_coordinates.png')
