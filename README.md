# Development and Validation of a Prognostic Clinical Risk Score for Subsequent Atopic Dermatitis Risk  <br>
 Supplementary materials for the development and validation of atopic dematitis score in utero <br>
 * Full prognosis model can be found in score_algorithm.py <br>
 * Questionnaire.py file is the questionnaire form of the model. Run this code to answer the questions and get an AD risk result per patient.

## Development - The score's computation

The score was computed in 2 steps: <br>
By Group: Each group was assigned a weight according to the pseudo R square values from a multivariate logistic regression. The groups each have an individual effect on the model, making the R-squared value cumulative. There is almost no interaction effect between the groups, allowing us to measure their individual effects separately <br>
By Variable: Individual variables are assigned an OR according to a logistic regression model fitted specifically for that group. The OR is then normalized with the group’s weight to calculate the final point of the variable. For example, the following table shows the R2 group value and corresponding weight ratio and the subsequent table shows the calculation of an individual variable's weights using its respective OR. The equation below demonstrates the mathematical description described in the tables.  <br>


| Group           | R2  | Explanatory Weight Ratio for points |
|-----------------|-----|-------------------------------------|
| Group1          | 0.2 | 20                                  |
| Group2          | 0.1 | 10                                  |
| Group3          | 0.1 | 10                                  |


## Table 1 **<br>**

Characteristics of Training & Validation sets

```
| Category                       | Sub-category                          | IFPS2 Control (n=1,418) | IFPS2 AD up to 1Y (n=389) | P-Value | LEUMIT Control (n=63,852) | LEUMIT AD up to 3Y (n=7,370) | P-Value |
|--------------------------------|---------------------------------------|-------------------------|---------------------------|---------|---------------------------|------------------------------|---------|
| Sex                            | Male (%)                              | 663 (46.8)              | 221 (41.1)                | <.001   | 33,072 (51.8)             | 4173 (56.6)                 | <.001   |
| Urbanity                       | Urban (%)                             | 411 (29)                | 138 (35.5)                | <.05    | 37,431 (58.6)             | 4674 (63.4)                 | <.001   |
| Birth Season                   | Autumn                                | 501 (35.3)              | 160 (41.1)                | <.05    | 16,709 (28.3)             | 2085 (28.3)                 | <.001   |
|                                | Summer                                | 314 (22.1)              | 92 (23.7)                 | -       | 16,095 (25.2)             | 1868 (25.3)                 | -       |
|                                | Winter                                | 585 (41.3)              | 130 (33.4)                | -       | 16,016 (25.1)             | 1779 (24.1)                 | -       |
|                                | Spring                                | 18 (1.3)                | 7 (1.8)                   | -       | 15,032 (23.5)             | 1638 (22.2)                 | -       |
| Family History                 | Smoke record (%)                      | 298 (21)                | 54 (13.9)                 | <.01    | 11,787 (18.5)             | 1575 (21.4)                 | <.001   |
|                                | Parent with an atopic condition (%)   | 308 (21.7)              | 132 (33.9)                | <.001   | 22,594 (35.2)             | 3620 (49.1)                 | <.001   |
|                                | Parents with atopic dermatitis (%)    | 100 (7.1)               | 81 (20.8)                 | <.001   | 2934 (4.6)                | 710 (9.6)                   | <.001   |
|                                | Both Parents Atopic (%)               | 36 (2.5)                | 21 (5.4)                  | <.01    | 2410 (3.8)                | 455 (6.2)                   | <.001   |
| Sibling History                | First Born (%)                        | 388 (27.4)              | 121 (31.1)                | 0.16    | 23,069 (36.1)             | 3541 (48)                   | <.001   |
|                                | Sibling with an atopic condition (%)  | 162 (11.4)              | 81 (20.8)                 | <.001   | 19,500 (30.5)             | 2553 (34.6)                 | <.001   |
|                                | Siblings with atopic dermatitis (%)   | 111 (7.8)               | 92 (23.7)                 | <.001   | 6854 (10.7)               | 1520 (20.6)                 | <.001   |
| Systemic Antibiotics taken     | 0                                     | -                       | -                         | -       | 49,298 (77.2)             | 5010 (68)                   | <.001   |
| during pregnancy               | 1                                     | -                       | -                         | -       | 9508 (14.9)               | 1543 (20.9)                 | -       |
|                                | 2                                     | -                       | -                         | -       | 3211 (5)                  | 520 (7.1)                   | -       |
|                                | 3                                     | -                       | -                         | -       | 1835 (2.9)                | 297 (4.1)                   | -       |

```


## Table 2 : Predictive Probability of AD Across Assessed Variables **<br>**

The adjusted and unadjusted association between variables and outcome (AD). <br>
This table demonstrated the varaiables individual effect within each group and withing the complete model. 

<img src="table 2.png"/>

