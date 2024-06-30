import matplotlib.pyplot as plt

def bresenham_line_drawing(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    return points

def plot_line(points):
    x_values, y_values = zip(*points)
    plt.plot(x_values, y_values, marker='o', color='blue')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Bresenham Line Drawing Algorithm')
    plt.grid()
    plt.show()

x1, y1 = map(int, input("Enter the starting point (x1, y1): ").split())
x2, y2 = map(int, input("Enter the ending point (x2, y2): ").split())

points = bresenham_line_drawing(x1, y1, x2, y2)
plot_line(points)
