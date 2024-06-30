# Development and Validation of a Prognostic Clinical Risk Score for Subsequent Atopic Dermatitis Risk: Supplementry materials  <br>
 Supplementary materials for the development and validation of atopic dematitis score in utero <br>
 * Full prognosis model can be found in score_algorithm.py <br>
 * Questionnaire.py file is the questionnaire form of the model. Run this code to answer the questions and get an AD risk result per patient.

## Background
The rise in prevalence of atopic dermatitis has been correlated with numerous elements of the exposome, modern-day lifestyle, and familial history. <br>
A prognostic atopic dermatitis clinical risk score can empower clinicians to diagnose AD earlier on or to educate caregivers on proven preventive modalities for atopic conditions.  <br>
Atopic dermatitis can start at a very early age, thus we integrated ONLY prenatal predictors in our prognostic model. <br>
We aimed to develop a clinical risk score to assess the risk of developing atopic dermatitis using a large and diverse cohort and easily-assessed risk factors. <br> 


## Development - The score's computation

The score was computed in 2 steps: <br>
By Group: Each group was assigned a weight according to the pseudo R square values from a multivariate logistic regression. The groups each have an individual effect on the model, making the R-squared value cumulative. There is almost no interaction effect between the groups, allowing us to measure their individual effects separately <br>
By Variable: Individual variables are assigned an OR according to a logistic regression model fitted specifically for that group. The OR is then normalized with the group’s weight to calculate the final point of the variable. For example, the following table shows the R2 group value and corresponding weight ratio and the subsequent table shows the calculation of an individual variable's weights using its respective OR. The equation below demonstrates the mathematical description described in the tables.  <br>

Here is an example for the points computation by group and by variable: <br>

| Group           | R2  | Explanatory Weight Ratio for points |
|-----------------|-----|-------------------------------------|
| Group1          | 0.2 | 20                                  |
| Group2          | 0.1 | 10                                  |
| Group3          | 0.1 | 10                                  |

Variables from group1: <br>

| Group Variables | OR  | Normalized score to the group’s weight |
|-----------------|-----|----------------------------------------|
| Var1            | 1   | 4                                      |
| Var2            | 2   | 8                                      |
| Var3            | 1   | 4                                      |
| Var4            | 0.5 | 2                                      |
| Var5            | 0.5 | 2                                      |

 
Var1 Points = (OR_var1g1 / Sum OR_g1) * W_g1 

Combining all the information we collected, this is the final score: <br>

R_n = (W_g1 * Σ(S_g1n) + W_g2 * Σ(S_g2n) + W_g3 * Σ(S_g3n)) / Max{S_n} + C


Where: <br>
Rn denote the AD risk per patient so that Rn ⋲ [C,1] <br>
Sn is the score according to the patient’s parameters <br> 
C denote the underlying population prevalence of AD <br> 
W is the group’s assign weight, W ⋲ [0,1] <br>


## The Risk Score Groups

Risk groups were assigned according to the final score: <br>

The thresholds for the groups were defined according to the distribution of scores in the development (not validation) dataset, depicted below. The median of the AD population is at 0.5 score (the “high risk” group). Between 0.35-0.5 is the most mixed population (the “medium risk” group) and bellow 0.35 the prevalence of the control group is the highest (“low risk” group).


<img src="images/score dist.png"/>


Result:

| Risk Score     | Risk Group | Dist. |
|----------------|------------|-------|
| Rn ≥ 0.5       | High       | 30%   |
| 0.35 ≤ Rn<0.5  | Medium     | 30%   |
| Rn < 0.35      | Low        | 40%   |

### ANOVA

There was a significant difference in means among the risk groups in relation to the actual cases of atopic dermatitis (ANOVA, p<0.001)

|             | LR Chisq | df | P-Value |
|-------------|----------|----|---------|
| Score Group | 1891     | 2  | <.0001  |

The table above describes the result of ANOVA (Analysis of Deviance Table, Type III tests) for logistic regression. Results show a statistically significant effect of the score group levels (Low, Medium, High) which allows us to reject the null hypothesis and state that the score group has a strong effect on the response variable (AD diagnosis). 

## Description of Variables
| Category                      | Sub-category                          | Type       | Level                           | Description                                                  |
|-------------------------------|---------------------------------------|------------|--------------------------------|--------------------------------------------------------------|
| Demography                    |                                       |            |                                |                                                              |
|                               | Sex                                   | Binary     | Male/Female                    | Sex                                                          |
|                               | Urbanity                              | Binary     | Urban/Not urban                | Living environment                                           |
|                               | Birth Season                          | Categorical| Autumn/Summer/Spring/Winter    | Season of birth                                              |
| Social Economic Status (SES)  |                                       |            |                                |                                                              |
|                               | SES                                   | Categorical| Medium-Low/Medium-High         | Social Economic status                                       |
|                               | Smoke record                          | Binary     | Smokers/Non Smokers            | A family member with a documented smoking history            |
| Family History                |                                       |            |                                |                                                              |
|                               | Maternal Atopic                       | Binary     | Yes/No                         | Maternal atopic diagnosis                                    |
|                               | Paternal Atopic                       | Binary     | Yes/No                         | Paternal atopic diagnosis                                    |
|                               | Parents with atopic dermatitis        | Binary     | Yes/No                         | At least one parent with an AD diagnosis                     |
|                               | Systemic Antibiotics taken during pregnancy | Categorical | 0/1/2/3                    | Number of systemic antibiotics prescribed during pregnancy  |
| Sibling History               |                                       |            |                                |                                                              |
|                               | First Born                            | Binary     | First Born/Not                 | A child without siblings                                      |
|                               | Percent of Sibling with an atopic condition | Continuous| Yes/No                    | Total siblings with atopic condition divided by total number of siblings |
|                               | Siblings with atopic dermatitis       | Binary     | Yes/No                         | At least one sibling with an AD diagnosis                     |


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

<img src="images/table 2.png"/>

## Results

_**The joint distribution of age at first AD diagnosis and AD Score**_ <br>

<img src="images/score age dist.png"/>

Depiction of the correlation between the age at first diagnosis of AD (x-axis) and AD risk scores (y-axis). <br>
The majority cases of infant AD were diagnosed before 6 months old. <br>
Higher risk score is more common in infants up to 6 months old. <br>



_**Prevalance of AD by risk group**_ <br>
Comparing results from the development data set to validation and standard of care <br>

|                                 | AD base risk in population | Low | Low dev. | Medium | Medium dev. | High | High dev. |
|---------------------------------|----------------------------|-----|----------|--------|-------------|------|-----------|
| Parental History of Atopy       | 10                         | 8   | -2       | -      | -           | 14   | 4         |
| AD Risk Score - Development Dataset | 10                     | 5   | -5       | 10     | 0           | 17   | 7         |
| AD Risk Score - Validation Dataset  | 20                     | 15  | -5       | 22     | 2           | 38   | 18        |

*All numbers represent prevalence in population (%).  
**The deviation is from the base risk according to the relevant population. <br>

The relative risk chages by group compared to the base risk in the population: <br>


<img src="images/result.png"/>


Representation of the prevalence of AD across different risk groups, <br>
with 95% confidence intervals for the prevalence estimates : <br>

<img src="images/AD prevalence.png"/>


The score was validated on the Infant Feeding Practices Study (IFPS2), a nationally distributed questionnaire study of US households. <br>
Variation in AD risk across different group’s scores relative to the existing rates of AD within the groups is presented. <br> 
Both iterations of the score (internal and external validations) perform better than the standard of care for both low and high-risk groups. <br>


_**Odds Ratios of the risk groups**_ <br>


<img src="images/forest plot.png"/>


Results show that the infants in the “medium” and “high” group scores had significantly higher risk for AD.
Infants in the “High” group are 4 times more likely to develop AD than the “Low” group.

