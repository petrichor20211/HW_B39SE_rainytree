import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
T = np.arange(323, 403, 10)
inv_T = 1 / T
Ir = np.array([0.00323*10**(-6), 0.00708*10**(-6), 0.01669*10**(-6), 0.0325*10**(-6), 0.06984*10**(-6), 0.1588*10**(-6), 0.3189*10**(-6), 0.6538*10**(-6)])
In_Ir = np.log(Ir)

# 绘制图表
plt.plot(inv_T, In_Ir, marker='o', linestyle='-', color='b', label='Data Points')
plt.title('In(Ir) vs. 1/T')
plt.xlabel('1/T(k^(-1))')
plt.ylabel('In(Ir)')
plt.legend()
for xt, yt in zip(inv_T,In_Ir):
    plt.text(xt, yt, f'({xt:.4}, {yt:.2})', ha='center', va='bottom')
# plt.savefig(r'D:\Desktop\23秋\B39SE\LAB1')
plt.show()
# 计算斜率
# 使用最小二乘法计算斜率
slope, intercept = np.polyfit(inv_T, np.log(Ir), 1)
print("斜率:", slope)
