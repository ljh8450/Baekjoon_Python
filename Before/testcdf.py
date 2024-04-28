
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 평균 및 표준편차 설정
mu = 0
sigma = 1

# x 값 생성
x = np.linspace(-5, 5, 1000)

# 정규 분포의 확률 밀도 함수 계산
y = norm.pdf(x, mu, sigma)

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2)
plt.fill_between(x, 0, y, where=(-1 < x) & (x < 1), color='gray', alpha=0.5)  # 구간 -1 < X < 1에 해당하는 면적을 회색으로 칠함
plt.text(0.5, 0.1, 'Area = P(-1 < X < 1)', fontsize=12, ha='center')
plt.title('Standard Normal Distribution')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.grid(True)
plt.show()