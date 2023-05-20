import numpy as np
import matplotlib.pyplot as plt

# x 범위 설정
x = np.linspace(-10, 10, 100)

# 곡선 함수 정의 (여기에서는 y = x^2)
y = x ** 2

# 그래프 그리기
plt.plot(x, y)

# 그래프 표시
plt.show()