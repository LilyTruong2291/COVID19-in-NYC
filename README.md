# Analyzing COVID-19 Cases in New York City: Project Overview
*This analytics project aims to explore whether lower income neighborhoods are more likely to contract COVID-19.*

In March 2020, WHO declared the disease caused by the novel coronavirus outbreak a global pandemic. Since then, this virus has spread rapidly and affected more than 4 million people; while it has taken the lives of nearly 290,000 people worldwide (as of May 9, 2020). New York City is among one the most severely affected cities in the world, which accounts for nearly 50% of confirmed cases in the U.S.

In this analysis project, I examine whether people living in low-income areas are more likely to be contract the virus. To do this, I use COVID testing data provided by the New York City Department of Health, as well as U.S. Census data from 2018.

## Code and Resources Used

**Python Version:** 3.6

**Server:** Microsoft Azure Notebook

**Packages:** numpy, pandas, matplotlib, seaborn, geopandas

**Instataltion:** 
!pip install geopandas

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

I looked at the correlation of each variables to each others.

![Correlation Analysis](https://github.com/LilyTruong2291/COVID19-in-NYC/blob/master/heatmap.png)

I also looked at the distribution of cases using NYC map
![Confirmed Cases per 1000 (updated Jun 01, 2016)](https://github.com/LilyTruong2291/COVID19-in-NYC/blob/master/map.png)

## Findings

The analysis has shown that the data about confirmed cases based on alone does not give us enough evidence proving that COVID-19 cases mostly affect low-income areas. Knowing how rapidly the virus spreads in the community, we would need more data such as employment status, change of commuting or ridership before and after the pandemic, household size to justify whether low-income neighbourhoods are more vulnerable to this virus. 

*The project I worked directly under the guidance of my mentor  Farrokh Mansouri https://www.linkedin.com/in/farrokh-mansouri-b570b1b/*
