import pandas as pd
import numpy as np
from math import sqrt, erf

# Load data (RAW STRING FIXED)
df = pd.read_csv(r"C:\Users\Raj bandaru\Downloads\ab_outcomes.csv")

# Keep only users who reached checkout
df = df[df["reached_checkout"] == 1]

# Aggregate
summary = df.groupby("experiment_group")["completed_order_sim"].agg(
    users="count",
    conversions="sum"
).reset_index()

control = summary[summary["experiment_group"] == "control"].iloc[0]
treat   = summary[summary["experiment_group"] == "treatment"].iloc[0]

n_c, x_c = int(control["users"]), int(control["conversions"])
n_t, x_t = int(treat["users"]), int(treat["conversions"])

p_c = x_c / n_c
p_t = x_t / n_t

# Lift
abs_lift = p_t - p_c
rel_lift = abs_lift / p_c

# Two-proportion z-test (pooled)
p_pool = (x_c + x_t) / (n_c + n_t)
se_pool = sqrt(p_pool * (1 - p_pool) * (1/n_c + 1/n_t))
z = abs_lift / se_pool

# Normal CDF using error function
def norm_cdf(z):
    return 0.5 * (1 + erf(z / sqrt(2)))

p_value = 2 * (1 - norm_cdf(abs(z)))

# 95% CI (unpooled)
se_unpooled = sqrt(p_c*(1-p_c)/n_c + p_t*(1-p_t)/n_t)
ci_low = abs_lift - 1.96 * se_unpooled
ci_high = abs_lift + 1.96 * se_unpooled

print("CONTROL:   rate =", round(p_c, 4), "n =", n_c)
print("TREATMENT: rate =", round(p_t, 4), "n =", n_t)
print()
print("Absolute lift:", round(abs_lift, 5))
print("Relative lift:", round(rel_lift, 4))
print("p-value:", round(p_value, 6))
print("95% CI (absolute lift):", (round(ci_low, 5), round(ci_high, 5)))

if p_value < 0.05 and ci_low > 0:
    print("\nDecision: SHIP (statistically significant lift)")
else:
    print("\nDecision: DO NOT SHIP")
