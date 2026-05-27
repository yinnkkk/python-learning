import numpy as np
import matplotlib.pyplot as plt

def menu():
    while True:
        try:
            choice = int(input("1. plot vectors\n2. plot vectors (and save as img)\n3. transform vectors with matricex\n4. quit\nEnter: "))
        except ValueError:
            print("This was not a valid number.")
            continue
        if choice == 1:
            x, y, v = get_vector()
            plot_vector(x,y,v)
        elif choice == 2:
            x,y,v = get_vector()
            plot_vector(x,y,v,save = True)
        elif choice == 3:
            transformed_vector()
        elif choice == 4:
            break
        else:
            print("This was not a proper number. ")
    
        
            
def get_vector():
    while True:
        try:
            x = float(input("X value: "))
            y = float(input("Y value: "))
            v = np.array([x, y])
            return x, y, v
        except ValueError:
            print("Not a proper number (float)")
            continue


def plot_vector(x, y, v, save = False):
    plt.axhline(0)
    plt.axvline(0)
    plt.grid()
    limit = max(abs(x), abs(y)) + 5
    plt.xlim(-limit, limit)
    plt.ylim(-limit, limit)
    plt.axis("equal")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.arrow(0, 0, v[0], v[1], head_width=0.2, length_includes_head=True)
    length = round(np.linalg.norm(v), 2)
    if v[0].is_integer() and v[1].is_integer():
        plt.text(x + 0.1, y + 0.1, f"v({int(v[0])}|{int(v[1])}) | {length}")
    else:
        plt.text(x + 0.1, y + 0.1, f"v({v[0]}|{v[1]}) | {length}")
    plt.title("2D vector visualization")
    if save:
        plt.savefig("Vector.png")
    plt.show()

def transformed_vector():
    A = transform()
    x, y, v = get_vector()
    w = A @ v
    plot_two_vectors(v,w)
    

def transform():
    while True:
        try:
            a = float(input("a value?: "))
            b = float(input("b value?: "))
            c = float(input("c value?: "))
            d = float(input("d value?: "))

            A = np.array([[a, b], [c, d]])
            return A
        except ValueError:
            print("Not a proper number.")

def plot_two_vectors(v, w):
    plt.axhline(0)
    plt.axvline(0)
    plt.grid()
    limit = max(abs(v[0]), abs(v[1]), abs(w[0]), abs(w[1])) + 5
    plt.xlim(-limit, limit)
    plt.ylim(-limit, limit)
    plt.axis("equal")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.arrow(0, 0, v[0], v[1], head_width=0.2, length_includes_head=True)
    plt.arrow(0, 0, w[0], w[1], head_width=0.2, length_includes_head=True)
    length = round(np.linalg.norm(v), 2)
    if v[0].is_integer() and v[1].is_integer():
        plt.text(v[0] + 0.1, v[1] + 0.1, f"original v({int(v[0])}|{int(v[1])})")
    else:
        plt.text(v[0] + 0.1, v[1] + 0.1, f"original v({v[0]}|{v[1]})")
    if w[0].is_integer() and w[1].is_integer():
        plt.text(w[0] + 0.1, w[1] + 0.1, f"original w({int(w[0])}|{int(w[1])})")
    else:
        plt.text(w[0] + 0.1, w[1] + 0.1, f"original w({w[0]}|{w[1]})")
    plt.title("2D vector visualization")
    plt.show()


    
if __name__ == "__main__":
    menu()


