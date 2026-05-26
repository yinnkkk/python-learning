import numpy as np
import matplotlib.pyplot as plt

def get_vector():
    while True:
        try:
            x = float(input("X value: "))
            y = float(input("Y value: "))
            v = np.array([x, y])
            return v, x, y
        except ValueError:
            print("Not a proper number (float)")
            continue


def plot_vector():
    v, x, y = get_vector()
    plt.axhline(0)
    plt.axvline(0)
    plt.grid()
    if x > 0:
        plt.xlim(0, x + 5)
    elif x < 0:
        plt.xlim(x - 5, 0)
    else:
        plt.xlim(-5, 5)
    if y > 0:
        plt.ylim(0, y + 5)
    elif y < 0:
        plt.ylim(y - 5, 0)
    else:
        plt.ylim(-5, 5)
    plt.xlabel("x")
    plt.ylabel("y")
    if v[0].is_integer() and v[1].is_integer():
        plt.text(x, y, f"v({int(v[0])}|{int(v[1])})")
    else:
        plt.text(x, y, f"v({v[0]}|{v[1]})")
    plt.title("2D vector visualization")
    plt.arrow(0, 0, v[0], v[1], head_width=0.2, length_includes_head=True)
    plt.show()
    

if __name__ == "__main__":
    plot_vector()


