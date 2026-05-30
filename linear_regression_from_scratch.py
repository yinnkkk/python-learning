import numpy as np
import matplotlib.pyplot as plt


# -----------------------------
# Settings
# -----------------------------
SEED = 3
NOISE_STRENGTH = 1
TRUE_M = 3
TRUE_B = 5
LEARNING_RATE = 0.01
DATA_AMOUNT = 50
EPOCHS = 1000


np.random.seed(SEED)


# -----------------------------
# Data generation
# -----------------------------
def generate_data_inputs():
    noise = np.random.randn(DATA_AMOUNT) * NOISE_STRENGTH
    x = np.random.uniform(0, 10, DATA_AMOUNT)
    return noise, x


def true_function(noise, x):
    y = TRUE_M * x + TRUE_B + noise
    return y


# -----------------------------
# Model logic
# -----------------------------
def predict(x, m_pred, b_pred):
    return m_pred * x + b_pred


def calculate_loss(error):
    return np.mean(error ** 2)


def calculate_gradients(error, x):
    m_gradient = 2 * np.mean(error * x)
    b_gradient = 2 * np.mean(error)
    return m_gradient, b_gradient


# -----------------------------
# Training
# -----------------------------
def training(x, y):
    loss_history = []

    m_pred = 0
    b_pred = 0

    for epoch in range(1, EPOCHS + 1):
        y_guess = predict(x, m_pred, b_pred)

        error = y_guess - y
        mean_error = np.mean(error)
        loss = calculate_loss(error)

        loss_history.append(loss)

        m_gradient, b_gradient = calculate_gradients(error, x)

        m_pred = m_pred - LEARNING_RATE * m_gradient
        b_pred = b_pred - LEARNING_RATE * b_gradient

        if epoch % 100 == 0:
            print(
                f"epoch: {epoch} | "
                f"mean error: {mean_error:.4f} | "
                f"loss: {loss:.4f} | "
                f"guessed m: {m_pred:.4f} | "
                f"guessed b: {b_pred:.4f}"
            )

        if len(loss_history) >= 200:
            current_losses = np.mean(loss_history[-100:])
            previous_losses = np.mean(loss_history[-200:-100])
            improvement = previous_losses - current_losses

            if abs(improvement) < 0.0001:
                print(f"Stopped early at epoch {epoch}")
                break

    return m_pred, b_pred, loss_history


# -----------------------------
# Plotting
# -----------------------------
def plot_results(m_pred, b_pred, x, y):
    x_line = np.linspace(0, 10, 100)

    learned_line = m_pred * x_line + b_pred
    true_line = TRUE_M * x_line + TRUE_B

    line_error = true_line - learned_line
    overlap_loss = np.mean(line_error ** 2)

    print(f"Line difference MSE: {overlap_loss:.4f}")

    plt.figure()
    plt.scatter(x, y, label="Data Points")
    plt.plot(x_line, learned_line, label="Guessed Function")
    plt.plot(x_line, true_line, label="True Function")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title("Linear Regression From Scratch")
    plt.legend()
    plt.show()


def plot_loss(loss_history):
    plt.figure()
    plt.plot(loss_history, label="Loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("Loss Over Time")
    plt.legend()
    plt.show()


# -----------------------------
# Main program
# -----------------------------
def menu():
    noise, x = generate_data_inputs()
    y = true_function(noise, x)

    m_pred, b_pred, loss_history = training(x, y)

    print("\nFinal Result:")
    print(f"True m: {TRUE_M}")
    print(f"Learned m: {m_pred:.4f}")
    print(f"True b: {TRUE_B}")
    print(f"Learned b: {b_pred:.4f}")
    print(f"Final loss: {loss_history[-1]:.4f}")

    plot_results(m_pred, b_pred, x, y)
    plot_loss(loss_history)


if __name__ == "__main__":
    menu()