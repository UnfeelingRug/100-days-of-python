# 1st Input: Height (m) | 2nd Input: Weight (kg)
height = input()
weight = input()

BMI = int(float(weight) / (float(height) ** 2))
print(BMI)