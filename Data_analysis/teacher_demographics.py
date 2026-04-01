"""
Calculate teacher demographics statistics
"""
import numpy as np

# Teacher ages
teacher_ages = [49, 42]

# Calculate mean and standard deviation
mean_age = np.mean(teacher_ages)
std_age = np.std(teacher_ages, ddof=1)  # ddof=1 for sample standard deviation

print(f"Teacher Demographics:")
print(f"N = {len(teacher_ages)}")
print(f"Mean age (M) = {mean_age:.2f} years")
print(f"Standard deviation (SD) = {std_age:.2f} years")
print(f"\nFormatted for paper: (M = {mean_age:.2f} years, SD = {std_age:.2f}, N = {len(teacher_ages)})")
