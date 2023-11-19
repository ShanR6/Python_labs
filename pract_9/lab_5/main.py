import numpy as np
import time
from scipy.stats import multivariate_normal


def multivariate_normal_logpdf(X, m, C):
    N, D = X.shape

    det_C = np.linalg.det(C)

    inv_C = np.linalg.inv(C)

    diff = X - m

    log_pdf = -0.5 * D * np.log(2 * np.pi) - 0.5 * np.log(det_C) - 0.5 * np.sum(diff @ inv_C * diff, axis=1)
    return log_pdf


X = np.array([[1, 2], [3, 4], [5, 6]])
m = np.array([2, 3])
C = np.array([[1, 0], [0, 1]])

start_time = time.time()
log_pdf = multivariate_normal_logpdf(X, m, C)
end_time1 = time.time() - start_time

start_time = time.time()
scipy_log_pdf = multivariate_normal(m, C).logpdf(X)
end_time2 = time.time() - start_time

print(f"Логарифм плотности:\n{log_pdf}\n", f"Время работы: {end_time1}\n", sep="")
print(f"Логарифм плотности(scipy):\n{scipy_log_pdf}\n", f"Время работы: {end_time2}\n", sep="")
print(f"Разница во времени:{end_time1 - end_time2}\nРазница по точности вычисления: {log_pdf - scipy_log_pdf}")
