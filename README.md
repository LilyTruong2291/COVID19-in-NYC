# Analyzing COVID-19 Cases in New York City: Project Overview
*This analytics project aims to explore whether lower income neighborhoods are more likely to contract COVID-19.*

In March 2020, WHO declared the disease caused by the novel coronavirus (COVID-19) outbreak a global pandemic. Since then, this virus has spread rapidly and affected more than 4 million people; while it has taken the lives of nearly 290,000 people worldwide (as of May 9, 2020). New York City is among one the most severely affected cities in the world, which accounts for nearly 50% of confirmed cases in the U.S.

In this analysis project, I examine whether people living in low-income areas are more likely to contract the virus. To do this, I use COVID testing data provided by the New York City Department of Health, as well as the population and median income estimates collected from U.S. Census data (2014-2018).

## Code and Resources Used

**Python Version:** 3.6

**Server:** Microsoft Azure Notebook

**Packages:** numpy, pandas, matplotlib, seaborn, geopandas

**Instataltion:** !pip install geopandas

**Dataset:**
* United States Census Bureau. B01001 SEX BY AGE, 2018 American Community Survey 5-Year Estimates. U.S. Census Bureau, American Community Survey Office. http://www.census.gov/.
* NYC Department of Health and Mental Hygiene.coronavirus-data. https://github.com/nychealth/coronavirus-data/blob/master/tests-by-zcta.csv

## Data Collection

The datasets are collected using the above links and merged into one dataframe with 177 rows and 7 columns. Each row represents a zip code in New York City. For each zipcode, we get the following variables:

* Zip_Code	
* Positive	
* Total	
* Positive_Rate	
* Median_Income	
* Population	

## Data Cleaning

After collecting the data, I needed to clean it up so that it could be properly analyzed. I made the following changes and created the following variables:

* Seperated Population for each zipcode - In the original dataset, multiple population data are in the same record.
* Made Column for Positve_per_1000 - This column is transformed from Positive Column to help compare the Positve and Test records on equal footing.
* Made Column for Test_per_1000 - This column is transformed from Test Column to help compare the Positve and Test records on equal footing.

## Exploratory Data Analysis (EDA)

I started by looking into any correlations among the available variables.

![Correlation Analysis](https://github.com/LilyTruong2291/COVID19-in-NYC/blob/master/heatmap.PNG)

The correlation coefficient between test given ratio and median income is -0.22 (R^2 = 0.048, p=0.003). That shows absence in the linear relationship between these two variables, which indicates that low-income communities don’t test at a lesser amount compared to other areas. When comparing a confirmed case ratio and median income, the correlation coefficient is -0.51 (R^2 = 0.257, p=0.00), which demonstrates a moderate negative association. Regarding the positive rate and median income, the correlation coefficient is -0.64 (R^2 = 0.405, p=0.00), which also shows a moderate negative association.

I also visualized the geographic distribution of cases with a chloropleth map of NYC.

![Confirmed Cases per 1000 (updated Jun 01, 2016)](https://github.com/LilyTruong2291/COVID19-in-NYC/blob/master/map.png)

The map illustrates that some affluent areas in Manhattan have high number of confirmed cases. 

## Findings

My analysis led me to the conclusion that the available evidence does not support the hypothesis that COVID-19 disproportionately affects low-income areas. More data is needed to explore this issue further. Namely, I'd be very interested in adding employment data, commuting patterns, and household size to get a more accurate picture. 

*The project I worked directly under the guidance of my mentor Farrokh Mansouri https://www.linkedin.com/in/farrokh-mansouri-b570b1b/*
