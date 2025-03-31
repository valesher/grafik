import numpy as np
import matplotlib.pyplot as plt

# Создаем диапазон значений x
x = np.linspace(-5, 5, 400)
y = x**2 / 2 - 2

# Создаем график
plt.figure(figsize=(6, 6))
plt.plot(x, y, label=r'$y=\frac{x^2}{2} - 2$', color='b')

# Добавляем оси координат
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Добавляем сетку
plt.grid(True, linestyle='--', alpha=0.6)

# Подписываем оси
plt.xlabel("X")
plt.ylabel("Y")

# Добавляем легенду
plt.legend()

# Показываем график
plt.show()