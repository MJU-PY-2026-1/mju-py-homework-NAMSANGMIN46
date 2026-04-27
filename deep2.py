import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import datasets
from sklearn.metrics import mean_squared_error

diabetes = datasets.load_diabetes()
print("전체 특성 목록:", diabetes.feature_names)
# 결과: ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
X = diabetes.data[:, [2, 8]]
y = diabetes.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
def plot_results(title, w, b, mse):
    print(f"[{title}]")
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"학습된 가중치(w): {w}, 편향(b): {b:.2f}\n")

    fig = plt.figure(figsize=(15, 5))

    w1, w2 = w[0], w[1]

    ax1 = fig.add_subplot(131)
    ax1.scatter(X_test[:, 0], y_test, color='dodgerblue', alpha=0.6)
    x1_range = np.array([X_test[:, 0].min(), X_test[:, 0].max()])
    y1_line = w1 * x1_range + w2 * X_test[:, 1].mean() + b
    ax1.plot(x1_range, y1_line, color='red', linewidth=3)
    ax1.set_xlabel('BMI')
    ax1.set_ylabel('Progression')
    ax1.set_title('BMI Effect (Test Data)')

    ax2 = fig.add_subplot(132)
    ax2.scatter(X_test[:, 1], y_test, color='darkorange', alpha=0.6)
    x2_range = np.array([X_test[:, 1].min(), X_test[:, 1].max()])
    y2_line = w1 * X_test[:, 0].mean() + w2 * x2_range + b
    ax2.plot(x2_range, y2_line, color='red', linewidth=3)
    ax2.set_xlabel('S5')
    ax2.set_ylabel('Progression')
    ax2.set_title('S5 Effect (Test Data)')

    ax3 = fig.add_subplot(133, projection='3d')
    ax3.scatter(X_test[:, 0], X_test[:, 1], y_test, color='teal', alpha=0.5)

    x1_grid = np.linspace(X_test[:, 0].min(), X_test[:, 0].max(), 10)
    x2_grid = np.linspace(X_test[:, 1].min(), X_test[:, 1].max(), 10)
    X1_mesh, X2_mesh = np.meshgrid(x1_grid, x2_grid)
    Y_mesh = w1 * X1_mesh + w2 * X2_mesh + b

    ax3.plot_surface(X1_mesh, X2_mesh, Y_mesh, color='red', alpha=0.4, edgecolor='gray', linewidth=0.5)
    ax3.set_xlabel('BMI')
    ax3.set_ylabel('S5')
    ax3.set_zlabel('Progression')
    ax3.set_title('3D Regression Plane')

    plt.show()

model = LinearRegression()
model.fit(X_train, y_train)
y_pred_sklearn = model.predict(X_test)
mse_sklearn = mean_squared_error(y_test, y_pred_sklearn)

plot_results("LinearRegression 클래스 결과", model.coef_, model.intercept_, mse_sklearn)

learning_rate = 0.5
epochs = 5000
n_samples = X_train.shape[0]


w_gd = np.zeros(X_train.shape[1])
b_gd = 0.0

for i in range(epochs):
    y_pred_train = np.dot(X_train, w_gd) + b_gd
    error = y_pred_train - y_train
    dw = (2 / n_samples) * np.dot(X_train.T, error)
    db = (2 / n_samples) * np.sum(error)
    w_gd = w_gd - learning_rate * dw
    b_gd = b_gd - learning_rate * db

y_pred_gd = np.dot(X_test, w_gd) + b_gd
mse_gd = mean_squared_error(y_test, y_pred_gd)

plot_results("Gradient Descent 결과", w_gd, b_gd, mse_gd)