# Analyzing COVID-19 Cases in New York City: Project Overview
*The analytics project aims to explore whether the lower income neighborhood is more likely to be infected with COVID-19.*

In March 2020, WHO declared COVID-19 outbreak a global pandemic. Since then, this virus has spread rapidly and affected more than 4 million people; while it has taken the lives of nearly 290,000 people worldwide (as of May 9, 2020). New York City is among one the most severely affected cities in the world, which accounts for nearly 50% of confirmed cases in the U.S.

In this analysis project, I would like to use the datasets provided by the New York City Department of Health about the number of tests given and the number of positive COVID-19 compared with the median income in each zip code to see whether people living in the low-income areas are more likely to be affected by the virus. 

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

The datasets are collected using the above links and merge into one dataframe with 177 rows and 7 columns. Each row represents each zip code in New York City. Each zipcode, we got the following:

* Zip_Code	
* Positive	
* Total	
* Positive_Rate	
* Median_Income	
* Population	

## Data Cleaning

After collecting the data, I needed to clean it up so that it is ready for our analytics. I made the following changes and created
the following variables:

* Seperated Population for each zipcode
* Made Column for Positve_per_1000
* Made Column for Test_per_1000

## Exploratory Data Analysis (EDA)

I looked at the correlation of each variables to each others.

![Correlation Analysis](https://github.com/LilyTruong2291/COVID19-in-NYC/blob/master/heatmap.png)

I also looked at the distribution of cases using NYC map
![Confirmed Cases per 1000 (updated Jun 01, 2016)](https://github.com/LilyTruong2291/COVID19-in-NYC/blob/master/map.png)

## Findings

The analysis has shown that the data about confirmed cases based on alone does not give us enough evidence proving that COVID-19 cases mostly affect low-income areas. Knowing how rapidly the virus spreads in the community, we would need more data such as employment status, change of commuting or ridership before and after the pandemic, household size to justify whether low-income neighbourhoods are more vulnerable to this virus. 

