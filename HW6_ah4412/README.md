# HW6

**Team:** Andrea Hassler (ah4412), Jerome Louison (jl9489), Tiffany Patafio (tp1600)

## Assignment 1: Completed individually
In this assignment, we forked another student's repository containing their HW4 assignment on CitiBike data. We evaluated their hypotheses, their processing of the data, and suggested a test to use. Then we made a pull request to the original owner.

Forked repository located here: AHassler/PUI2018_yy2908
Markdown file with review located here: AHassler/PUI2018_yy2908/HW4_yy2908/CitibikeReview_ah4412.md

## Assignment 2: Completed by Jerome (jl9489) with corrections and additions made by Andrea (ah4412)
In this assignment, we searched for papers that used tests from 3 categories. We then documented the tests, variables, variables types, question answered, and H0 and alpha. We stored this information in the table below.



The following chart shows three different research papers taken from peer-reviewed journal PLOS ONE.

| **Statistical Analyses**	|  **IV(s)**  |  **IV type(s)** |  **DV(s)**  |  **DV type(s)**  |  **Control Var** | **Control Var type**  | **Question to be answered** | **_H0_** | **alpha** | **link to paper**| 
|:----------:|:----------|:------------|:-------------|:-------------|:------------|:------------- |:------------------|:----:|:-------:|:-------|
| Logistic Regression	| Height of tree cavity	| Continuous |	Presence of Leisler's bat (Nyctalus leisleri) |	Dichotomous |	N/A |	N/A	| What is the odds probability of Leisler's bat presence as tree cavity height changes? |	Tree cavity height does not have a relationship to the odds probability of bat presence.<sup>1</sup> |	0.05<sup>1</sup>	| https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0200742&type=printable
Correlation	| Mimicry score	| Continuous	| Automatic imitation combined score	| Continuous	| N/A |	N/A	| Are mimicry and automatic imitation positively related? |	Mimicry scores and automatic imitation scores are not positively correlated. |	0.05	| https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0183784
ANOVA	| Level of Education<sup>2</sup>	| Categorical	| Kessler Psychological Distress Scale	| Continuous	| N/A	| N/A	| Do differences exist between levels of education on psychological distress?	| Differences do not exist between levels of education on the pschological distress score.	| 0.05	| https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0202818&type=printable

<sup>1</sup> This study was actually examining how the power of the test changed over different sampling ratios of species presence relative to the actual population ratio. This was accomplished using the bat population, since the true ratio is known, and randomly simulating varying ratios. The _H0_ and alpha above represent what a typical null and significance level of one of those tests might be on a sample in reality.  

<sup>2</sup> This was one of many demographic factors studied, including locality, sex, ethnicitiy, etc.


## Assignment 3: Jerome (jl9489) and Tiffany Patafio (tp1600) worked together equally on Assignment 3. Andrea (ah4412) reviewed.

In this assignment, we reproduced the analysis of the Hard to Employ program in NY. Specifically, we reproduced the results of testing the null for "Ever employed in a CEO transitional job" using a z-test and the results of testing the null of "Convicted of a felony" using a chi-square test.


## Assignment 4: Jerome (jl9489) started the assignment and then Andrea (ah4412) mainly worked alone to finish her copy.
In this assignment, we performed three tests on CitiBike data, comparing night riders with day riders. First, we processed the data to meet the needs of each test and produced relevant plots. Then, we conducted a KS test, Pearson's R, and Spearman's R.





