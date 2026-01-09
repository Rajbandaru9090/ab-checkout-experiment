# A/B Experimentation – Checkout Conversion Optimization

## Business Problem
Checkout friction is a common cause of cart abandonment in e-commerce.
This project evaluates whether simplifying the checkout flow increases
order completion rates without harming user behavior.

## Hypothesis
Reducing checkout friction will increase checkout conversion rate without
negatively impacting guardrail metrics.

## Dataset
Instacart Online Grocery Shopping Dataset (public).
Because the dataset contains only completed orders, checkout completion
was modeled probabilistically to simulate realistic funnel behavior.

## Experiment Design
- Unit of experimentation: User
- Randomized 50/50 assignment into control and treatment groups
- Primary metric: Checkout conversion rate
- Guardrail metric: Cart abandonment rate
- Treatment effect simulated conservatively (~5% relative lift)

## Methodology
1. Built a user-level funnel using SQL
2. Randomly assigned users to control and treatment groups
3. Simulated checkout completion outcomes
4. Aggregated experiment metrics using SQL
5. Performed statistical inference using a two-proportion z-test in Python

## Results
| Metric | Control | Treatment |
|------|--------|-----------|
| Checkout Conversion Rate | 39.95% | 42.26% |
| Relative Lift | — | **+5.76%** |
| p-value | — | < 0.001 |

95% Confidence Interval (absolute lift): **[1.88 pp, 2.73 pp]**

## Decision
The treatment produced a statistically significant and practically
meaningful lift in checkout conversion. Based on these results,
the recommendation is to **ship the checkout simplification**.

## Tools Used
- SQL (SQLite)
- Python (Pandas, NumPy)
- Statistical testing (two-proportion z-test)

## Notes
This project focuses on experimental design and causal inference rather
than visualization, reflecting real-world product experimentation workflows.
