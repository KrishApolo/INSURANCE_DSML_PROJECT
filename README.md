Problem Statement:
Insurnce companies need to predict t=he accurate insurance cost of health insurance for individuals to set the premium appropriately. 
However traditional methods of premium prediction often rely on board actuarial tables and historical averages, which may not accoent for nuancce differences among individuals.
By leveraging machine learning techiques, insurers can predict more accurately the insurnce costs tailered to individual profiles, leading to more competetive pricing 
and better risk management.

Primary Insurance cost prediction needs:

Ehance precision y the use of individual data bit not relying on historical averages.
Increase in competetivness among companies to provide attractive prices.
Improving customer satisfaction rate by fair and transperant premium prices.
Enable personalized offerings to cater more individual needs and preferences.
Risk assesment based on variuos indidividual factors to identify key factors for premium setup.
New policy developements based on key factors effecting the premuim prices.
Strategic decision making and Customer engagement.

**We have obtained below Insights from EDA:**

_Graphical Analysis_
There is no clear inference between diabetes, BP problems and number of surgeries, like there are people with no surgeries have diabetes and BP.
People with cancer history in family are not suffering much from chronic diseases.
Age and number of surgeries are slightly positively corelated, Age and premium price have higher correlation.

_Outlier and null value interpretation_
No null values in the data
Not many outliers were observed in data except for Premium Price and Weight, however considering the fact that difference between upper limit and outliers is minimum and chances of having higher weight are inferred to occur, we can choose to ignore these outliers now, no corrections are required.

_Hypothesis Testing_
We have calculated CI for average premium price of the population and provided estimates as below:

90% CI of Premium Price is 24009.10842241373 to 24664.319569472682 
95% CI of Premium Price is 23946.235207694965 to 24727.192784191448 
99% CI of Premium Price is 23823.17343500595 to 24850.254556880463

From Ttest we have enough evidence to conclude below inferences:
Premium Price is dependent of Diabetes, BP, History of Cancer, Transplants and Chronic diseases.
We do not have enough evidence to conclude that Premium Price is dependent of Known allergies.

From Kruskal's test we have enough evidence to conclude that Premium Price is dependent on number of surgeries.

From Chi2 we do not have enough evidence to say that AnyChronicDiseaes id dependent on HistoryofCancerinFamly.

From regression Analysis we have below inferences:
Height, BP and Known allergies highly affects the model, we can try to remove these factors one by one and check further.
R2 and adjusted R2 are not much different affect of number of features is not very significant.
VIF is not very high for any factor no factor is multicollinear.

**Machine learning Model:**
_Basic linear regression_
Traget variable is Premium Price which is a continous numeric value, we started with linear regression to check various dependencies 
and found that many values are not linearly variable with target value.

However no multi-colinearity was observed between data.

Basis linear regression provided us with R2-0.635 and adjusted R2 - 0.631 for testdata which is not satisfactory.
tried removing some unimportant features like known allergies and height, however no much improovement observed in the scores.

_Decission tree regressor_
We tried decission tree regressor with different hyperparametrs which produced 0.7.. R2 score which was still not satisfactory.

_Random Forest regressor_
I proceeded to random forest regressor which provided 0.76 OOB score and 0.88 R2 on test data.
I have applied grid search for various parameters but was only able to achieve slight improovement in OOB score 0.76, I stick with grid_search however.
Finalized model was for Grid search Random Forest for deployment which gave .76 OOB score and 88% R2 score.

**Deployment**
Deplyment was made by pycharm using stremlit software, encountered a few issues in the process however the deployment ws successfull.

Application Link:
https://insurancepredapppy-67smzxjhpfjekaurmxujzx.streamlit.app/



