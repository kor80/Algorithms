import turtle
# import BinaryTree as tree

sc = turtle.Screen()
t = turtle.Turtle()
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
NODE_RADIUS = 15
INFO_SIZE = 10
EDGE_LENGTH = 200
STARTING_EDGE_ANGLE = 80
EDGE_ANGLE_DECREASING_FACTOR = 20


def draw_node(info: int):
    t.down()
    t.circle(NODE_RADIUS)
    t.up()
    t.left(90)
    t.forward(NODE_RADIUS // 2)
    t.down()
    t.write(info, font=("Arial", INFO_SIZE, "normal"))
    t.up()
    t.right(180)
    t.forward(NODE_RADIUS // 2)


def draw_edge(direction: int, angle): #-1 left, 1 right
    t.left(direction * angle)
    t.down()
    t.forward(EDGE_LENGTH)
    t.up()
    t.right(direction * angle)
    t.forward(NODE_RADIUS * 2)
    t.left(90)


def draw_tree(root, angle):
    if root is None:
        return
    draw_node(root.info)
    if root.lc is None:
        return
    position = t.pos()
    draw_edge(-1, angle)
    draw_tree(root.lc, angle - EDGE_ANGLE_DECREASING_FACTOR)
    t.setpos(position)
    if root.rc is None:
        return
    draw_edge(1, angle)
    draw_tree(root.rc, angle - EDGE_ANGLE_DECREASING_FACTOR)


if __name__ == '__main__':
    sc.setup(SCREEN_WIDTH, SCREEN_HEIGHT, startx=0, starty=0)

    sc.bgcolor("black")
    t.color("white")

    t.hideturtle()
    t.speed(1000)
    t.up()
    t.sety(SCREEN_HEIGHT / 3)

    # Test Values
    # n1 = tree.BinaryTree(3, None, None)
    # n2 = tree.BinaryTree(7, None, None)
    # n3 = tree.BinaryTree(13, None, None)
    # n4 = tree.BinaryTree(17, None, None)
    # n5 = tree.BinaryTree(6, n1, n2)
    # n6 = tree.BinaryTree(15, n3, n4)
    # root = tree.BinaryTree(10, n5, n6)

    # draw_tree(root, STARTING_EDGE_ANGLE)

    turtle.exitonclick()
