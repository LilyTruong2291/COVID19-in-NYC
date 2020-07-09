# Analyzing COVID-19 Cases in New York City: Project Overview
*This analytics project aims to explore which communities are more likely to contract COVID-19.*

In March 2020, WHO declared the disease caused by the novel coronavirus (COVID-19) outbreak a global pandemic. Since then, this virus has spread rapidly and affected more than 12 million people; while it has taken the lives of nearly 550,000 people worldwide. The U.S is among countries that are heavily affected by this pandemic. The nation accounts for more than 25% of confirmed cases worldwide, with 3.1 million confirmed cases and 134,000 reported deaths (as of Jul 9, 2020). The city of New York in the US has reported high rate cases of COVID-19 fatalities in racialized and low income Hispanic and Black communities which accounts for more than 62 percent of the related deaths in the state, (Wilson, 2020).

In this analysis project, I examine which communities are more likely to contract the virus. To do this, I use COVID testing data provided by the New York City Department of Health, as well as the population and median income estimates collected from U.S. Census data (2014-2018). Moreover, I collected data about people with disability/coloured, communities in unfavorable living conditions and having underying health issues that might increase their risks of severe illness from COVID-19, according to CDC (2020).

## Code and Resources Used

**Python Version:** 3.6

**Server:** Microsoft Azure Notebook

**Packages:** numpy, pandas, matplotlib, seaborn, geopandas

**Instataltion:** !pip install geopandas

**Dataset:**
* United States Census Bureau. B01001 SEX BY AGE, 2018 American Community Survey 5-Year Estimates. U.S. Census Bureau, American Community Survey Office. http://www.census.gov/.
* NYC Department of Health and Mental Hygiene.coronavirus-data. https://github.com/nychealth/coronavirus-data/blob/master/tests-by-zcta.csv
* Social Vulnerability Index per Tract Census Level. Agency for Toxic Substances and Disease Registry. https://svi.cdc.gov/
* 500 Cities: Local Data for Better Health. Centers of Disease Control and Prevention.https://www.cdc.gov/features/500-cities-project/index.html
* USPS ZIP Code Crosswalk. Office of Policy Development and Research. https://www.huduser.gov/portal/datasets/usps_crosswalk.html

## Data Collection

The datasets are collected using the above links and merged into one dataframe with 177 rows and 7 columns. Each row represents a zip code in New York City. For each zipcode, we get the following variables:

* Zip_Code:  Modified ZCTA 
* E_POV:  Persons below poverty estimate, 2014-2018 ACS
* E_UNEMP:  Civilian (age 16+) unemployed estimate, 2014-2018 ACS
* E_NOHSDP:  Persons (age 25+) with no high school diploma estimate, 2014-2018 ACS
* E_AGE65:  Persons aged 65 and older estimate, 2014-2018 ACS
* E_DISABL:  Civilian noninstitutionalized population with a disability estimate, 2014-2018 ACS
* E_SNGPNT:  Single parent household with children under 18 estimate, 2014-2018 ACS
* E_MINRTY:  Minority (all persons except white, nonHispanic) estimate, 2014-2018 ACS
* E_LIMENG:  Persons (age 5+) who speak English "less than well" estimate, 2014-2018 ACS
* E_MUNIT:  Housing in structures with 10 or more units estimate, 2014-2018 ACS
* E_MOBILE:  Mobile homes estimate, 2014-2018 ACS
* E_CROWD:  At household level (occupied housing units), more people than rooms estimate, 2014- 2018 ACS
* E_NOVEH:  Households with no vehicle available estimate, 2014-2018 ACS
* E_GROUPQ:  Persons in institutionalized group quarters estimate, 2014-2018 ACS
* NEIGHBORHOOD_NAME:  Neighborhood name
* BOROUGH_GROUP:  Borough group
* COVID_CASE_COUNT:  Count of confirmed cases
* COVID_CASE_RATE:  Rates of COVID cases per 100,000 People by ZCTA
* POP_DENOMINATOR:  Population denominators for ZCTAs derived from intercensal estimates by the Bureau of Epidemiology Services
* COVID_DEATH_COUNT:  Count of confirmed deaths  
* COVID_DEATH_RATE:  Rate of confirmed deaths per 100,000 people by ZCTA 
* PERCENT_POSITIVE:  Percentage of people ever tested for COVID-19 with a polymerase chain reaction (PCR) test who tested positive
* TOTAL_COVID_TESTS:  Count of people tested for COVID-19 with a PCR test
* geoid:  
* Median_Income:  Median Income by ZCTA
* Population:  Population by ZCTA
* Log_Median_Income:  Transformed variable of Median_Income
* E_POV_rate:  E_POV per  100,000 by ZCTA
* E_UNEMP_rate:  E_UNEMP per 100,000 people by ZCTA
* E_NOHSDP_rate:  E_NOHSDP per 100,000 people by ZCTA
* E_AGE65_rate:  E_AGE65 per 100,000 people by ZCTA
* E_DISABL_rate:  E_DISABL per 100,000 people by ZCTA
* E_SNGPNT_rate:  E_SNGPNT per 100,000 people by ZCTA
* E_MINRTY_rate:  E_MINRTY per 100,000 people by ZCTA
* E_LIMENG_rate:  E_LIMENG per 100,000 people by ZCTA
* E_MUNIT_rate:  E_MUNIT per 100,000 people by ZCTA
* E_MOBILE_rate:  E_MOBILE per 100,000 people by ZCTA
* E_CROWD_rate:  E_CROWD per 100,000 people by ZCTA
* E_NOVEH_rate:  E_NOVEH per 100,000 people by ZCTA
* E_GROUPQ_rate:  E_GROUPQ per 100,000 people by ZCTA
* COPD:  Respondents aged ≥18 years who report ever having been told by a doctor, nurse, or other health professional that they had chronic obstructive pulmonary disease (COPD), emphysema, or chronic bronchitis.
* Coronary Heart Disease:  Respondents aged ≥18 years who report ever having been told by a doctor, nurse, or other health professional that they had angina or coronary heart disease.
* Diabetes:  Respondents aged ≥18 years who report ever been told by a doctor, nurse, or other health professional that they have diabetes other than diabetes during pregnancy.
* High Blood Pressure:  Respondents aged ≥18 years who report ever having been told by a doctor, nurse, or other health professional that they have high blood pressure. Women who were told high blood pressure only during pregnancy and those who were told they had borderline hypertension were not included.
* Obesity:  Adult obesity among adults aged ≥18 years
* Chronic Kidney Disease:  Respondents aged ≥18 years who report ever having been told by a doctor, nurse, or other health professional that they have kidney disease
* COPD_rate:  COPD estimates per 100,000 people by ZCTA
* Coronary Heart Disease_rate:  Coronary Heart Disease per 100,000 people by ZCTA
* Diabetes_rate:  Diabetes per 100,000 people by ZCTA
* High Blood Pressure_rate:  High Blood Pressure per 100,000 people by ZCTA
* Obesity_rate:  Obesity per 100,000 people by ZCTA
* Chronic Kidney Disease_rate:  Chronic Kidney Disease per 100,000 people by ZCTA


## Data Cleaning

After collecting the data, I needed to clean and merge it up so that it could be properly analyzed. I made the following changes and created the following variables:

* Seperated Population for each zipcode - In the original dataset, multiple population data are in the same record.
* Allocated Census tract to Zip code level so all data can be merged to one file
* Made Columns for _rate - These columns are transformed from health and svi columns to help compare all the varialbes on equal footing.
* Made Column for Log_Median_Income - This column is transformed from Median_Income as the variable is right skew.


## Exploratory Data Analysis (EDA)

I started by looking into any correlations among the available variables.

![Correlation Analysis](https://github.com/LilyTruong2291/COVID19-in-NYC/blob/master/corr.PNG)

The correlation coefficient between test given ratio and median income is -0.22 (R^2 = 0.048, p=0.003). That shows absence in the linear relationship between these two variables, which indicates that low-income communities don’t test at a lesser amount compared to other areas. When comparing a confirmed case ratio and median income, the correlation coefficient is -0.51 (R^2 = 0.257, p=0.00), which demonstrates a moderate negative association. Regarding the positive rate and median income, the correlation coefficient is -0.64 (R^2 = 0.405, p=0.00), which also shows a moderate negative association.

I also visualized the geographic distribution of cases with a chloropleth map of NYC.

![Confirmed Cases per 100,000 (updated Jun 23, 2020)](https://github.com/LilyTruong2291/COVID19-in-NYC/blob/master/map1.PNG)
![Confirmed Death per 100,000 (updated Jun 23, 2020)](https://github.com/LilyTruong2291/COVID19-in-NYC/blob/master/map2.PNG)

The darker the red shade is the higher the number. The map illustrates that some affluent areas in Manhattan have high number of confirmed cases. 

![Below Poverty per 100,000 (updated Jun 23, 2020)](https://github.com/LilyTruong2291/COVID19-in-NYC/blob/master/map3.PNG)
![Minority per 100,000 (updated Jun 23, 2020)](https://github.com/LilyTruong2291/COVID19-in-NYC/blob/master/map4.PNG)
![Crowded Households per 100,000 (updated Jun 23, 2020)](https://github.com/LilyTruong2291/COVID19-in-NYC/blob/master/map5.PNG)

The darker the purple shade is the higher the number. 

## Findings

My analysis led me to the conclusion that the available evidence does not support the hypothesis that COVID-19 disproportionately affects low-income areas. More data is needed to explore this issue further. Namely, I'd be very interested in adding employment data, commuting patterns, and household size to get a more accurate picture. 

*Thanks to **Farrokh Mansouri** for his mentorship in this domain.* 

https://www.linkedin.com/in/farrokh-mansouri-b570b1b/

