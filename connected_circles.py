from tkinter import *

from simple_graph import Graph

# Constants
WIDTH, HEIGHT = 500, 400
RADIUS = 15

# Setup GUI
window = Tk()
window.title("Connected Circles")
canvas = Canvas(window, bg="white", width=WIDTH, height=HEIGHT)
canvas.pack()

circles = []


def distance(c1, c2):
    return ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2) ** 0.5


def repaint():
    canvas.delete("point")

    if not circles:
        return

    graph = Graph()
    for i in range(len(circles)):
        for j in range(i + 1, len(circles)):
            if distance(circles[i], circles[j]) <= 2 * RADIUS:
                graph.add_edge(i, j)
                graph.add_edge(j, i)

    connected_nodes = graph.dfs(0) if circles else set()

    for i, (x, y) in enumerate(circles):
        color = "red" if len(connected_nodes) == len(circles) else "blue"
        canvas.create_oval(x - RADIUS, y - RADIUS, x + RADIUS, y + RADIUS, fill=color, outline="black", tags="point")


def add_circle(event):
    circles.append((event.x, event.y))
    repaint()


canvas.bind("<Button-1>", add_circle)
window.mainloop()
