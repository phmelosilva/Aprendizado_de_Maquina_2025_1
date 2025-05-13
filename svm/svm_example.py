from sklearn.datasets import make_circles
from sklearn.svm import SVC
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Gerar um conjunto de dados não linear
X, y = make_circles(n_samples=100, factor=0.1, noise=0.1, 
random_state=42)
# Treinar o modelo SVM com kernel polinomial
model = SVC(kernel='poly', degree=3)
model.fit(X, y)
# Criar a grade para visualizar a fronteira de decisão
xx, yy = np.meshgrid(np.linspace(-1.5, 1.5, 100), np.linspace(-1.5, 1.5, 
100))
# Prever as classificações para cada ponto na grade
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
# Plotar os dados e a fronteira de decisão
plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, alpha=0.8, cmap='coolwarm')
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolor='k', s=50)

plt.title('SVM com Kernel Polinomial')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()