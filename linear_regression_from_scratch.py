import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42)
def generate_data_inputs():
    noise = np.random.randn(50)
    x = np.random.uniform(0,10,50)
    return noise, x

def true_function(noise, x, m=3, b=5):
    y = m * x + b + noise
    return y

def predict(x, m_pred, b_pred):
    return m_pred * x + b_pred

def calculate_loss(error):
    loss = np.mean(error ** 2)
    return loss

def calculate_gradients(error, x):
    m_gradient = 2 * np.mean(error * x)
    b_gradient = 2 * np.mean(error)
    return m_gradient, b_gradient

def training(x, y, learning_rate = 0.01):
    loss_history = []
    m_pred = 0
    b_pred = 0
    for epoch in range(1,1000):
        y_guess = predict(x,m_pred,b_pred)
        error = y_guess - y
        mean_error = np.mean(error)
        loss = calculate_loss(error)
        loss_history.append(loss)
        m_gradient, b_gradient = calculate_gradients(error, x)
        m_pred = m_pred - learning_rate * m_gradient
        b_pred = b_pred - learning_rate * b_gradient
        if epoch % 100 == 0:
            print(f"epoch: {epoch} | mean error: {mean_error:.4f} | loss: {loss:.4f} | guessed m: {m_pred:.4f} | guessed b: {b_pred:.4f}")
        if len(loss_history) >= 200:
            current_losses = np.mean(loss_history[-100:])
            previous_losses = np.mean(loss_history[-200:-100])
            improvement = previous_losses - current_losses
            if improvement < 0.0001:
                print(f"Stopped early at epoch {epoch}")
                return m_pred, b_pred, loss_history
    return m_pred, b_pred, loss_history
    
def plot_results(m_pred, b_pred, x, y, m=3, b=5):
    x_line = np.linspace(0, 10, 100) 
    y_line = m_pred * x_line + b_pred
    true_line = m * x_line + b
    line_error = true_line - y_line
    overlap_loss = np.mean(line_error ** 2)
    print(f"Line difference MSE: {overlap_loss:.4f}")
    plt.figure()
    plt.scatter(x,y, label = "Data Points")
    plt.plot(x_line, y_line, label = "Guessed Function")
    plt.plot(x_line, true_line, label = "True Function")
    plt.xlabel("X-Axis")
    plt.ylabel("Y_Axis")
    plt.show()

def plot_loss(loss_history):
    plt.figure()
    plt.plot(loss_history)
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("Loss over time")
    plt.show()

def menu():
    noise, x = generate_data_inputs()
    y = true_function(noise, x)
    m_pred, b_pred, loss_history = training(x, y, learning_rate = 0.01)
    plot_results(m_pred, b_pred, x, y)
    plot_loss(loss_history)

if __name__ == "__main__":
    menu()

