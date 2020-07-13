# Analyzing COVID-19 Cases in New York City: Project Overview 
*This analytics project aims to explore which communities are more likely to contract COVID-19.*

In March 2020, WHO declared the disease caused by the novel coronavirus (COVID-19) outbreak a global pandemic. Since then, this virus has spread rapidly and affected more than 12 million people; while it has taken the lives of nearly 550,000 people worldwide. The U.S is among countries that are heavily affected by this pandemic. The nation accounts for more than 25% of confirmed cases worldwide, with 3.1 million confirmed cases and 134,000 reported deaths (as of Jul 9, 2020). The city of New York in the US has reported high rate cases of COVID-19 fatalities in racialized and low income Hispanic and Black communities which accounts for more than 62 percent of the related deaths in the state, (Wilson, 2020).

In this analysis project, I examine which communities are more likely to contract the virus. To do this, I use COVID testing data provided by the New York City Department of Health(updated on June 23, 2020), as well as the population and median income estimates collected from U.S. Census data (2014-2018). Moreover, I collected data about people with disability/coloured, communities in unfavorable living conditions and having underying health issues that might increase their risks of severe illness from COVID-19, according to CDC (2020).

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

The datasets are collected using the above links and merged into one dataframe with 177 rows and 29 columns. Each row represents a zip code in New York City. For each zipcode, we get the following variables:

* Zip_Code
* Neighborhood name
* Borough group
* Count of confirmed cases
* Rates of COVID cases per 100,000 People by ZCTA
* Population denominators for ZCTAs derived from intercensal estimates by the Bureau of Epidemiology Services
* Count of confirmed deaths  
* Rate of confirmed deaths per 100,000 people by ZCTA 
* Percentage of people ever tested for COVID-19 with a polymerase chain reaction (PCR) test who tested positive
* Count of people tested for COVID-19 with a PCR test
* Median Income by ZCTA
* Population by ZCTA
* Persons below poverty estimate
* Civilian (age 16+) unemployed estimate, 2014-2018 ACS
* Persons (age 25+) with no high school diploma estimate, 2014-2018 ACS
* Persons aged 65 and older estimate, 2014-2018 ACS
* Civilian noninstitutionalized population with a disability estimate, 2014-2018 ACS
* Single parent household with children under 18 estimate, 2014-2018 ACS
* Minority (all persons except white, nonHispanic) estimate, 2014-2018 ACS
* Persons (age 5+) who speak English "less than well" estimate, 2014-2018 ACS
* Housing in structures with 10 or more units estimate, 2014-2018 ACS
* Mobile homes estimate, 2014-2018 ACS
* At household level (occupied housing units), more people than rooms estimate, 2014- 2018 ACS
* Households with no vehicle available estimate, 2014-2018 ACS
* Persons in institutionalized group quarters estimate, 2014-2018 ACS
* COPD (chronic obstructive pulmonary disease (COPD), emphysema, or chronic bronchitis)
* Coronary Heart Disease
* Diabetes
* High Blood Pressure
* Obesity
* Chronic Kidney Disease

More information about the variables can be found in [the metadata](https://github.com/LilyTruong2291/COVID19-in-NYC/blob/master/Metadata.xlsx)

## Data Cleaning

After collecting the data, I needed to clean and merge it up so that it could be properly analyzed. I made the following changes and created the following variables:

* Seperated Population for each zipcode - In the original dataset, multiple population data are in the same record.
* Allocated Census tract to Zip code level so all data can be merged to one file based on Zip Code Level
* Made Columns for _rate - These columns are transformed from health and svi columns to help compare all the varialbes on equal footing.
* Made Column for Log_Median_Income - This column is transformed from Median_Income as the variable is right skew.

More detailed about data cleaning [here](https://github.com/LilyTruong2291/COVID19-in-NYC/blob/master/data_cleaning.ipynb)

## Exploratory Data Analysis (EDA)
The pivot table has shows that multiple neighborhood in Queens and Bronx county have the highest confirmed and dealth rates.

![Pivot Table for Confirmed Rates by Neighborhood](https://github.com/LilyTruong2291/COVID19-in-NYC/blob/master/images/pivot1.PNG)

![Pivot Table for Dealth Rates by Neighborhood](https://github.com/LilyTruong2291/COVID19-in-NYC/blob/master/images/pivot2.PNG)

Then, I started by looking into any correlations among the available variables.

![Correlation Analysis](https://github.com/LilyTruong2291/COVID19-in-NYC/blob/master/images/corr1.PNG)

This simple statistics method help to identify which correlations are the strongest. Figure closer to 1 (darker blue shade) indicate positive correlation; whereas figure closer to -1 (darker red shade) indicate negative correlation. Out of 19 socio-economic and health factors I tested, the strongest correlation confimred cases per 100,000 with log median income (-0.53). There are weak correlation between minority/low education/underlying health issues with confirmed COVID-19 cases. The correlation reveals that more cases are occured in middle income communities. 

I also visualized the geographic distribution of cases with a chloropleth map of NYC.

![Confirmed Cases per 100,000 (updated Jun 23, 2020)](https://github.com/LilyTruong2291/COVID19-in-NYC/blob/master/images/map1.PNG)

The darker the red shade is the higher the number. Queens, followed by Bronx appear to get hit the hardest by the virus. In addition, the map illustrates that some affluent areas in Manhattan have high number of confirmed cases. 

![Persons living below porverty per 100,000 (updated Jun 23, 2020)](https://github.com/LilyTruong2291/COVID19-in-NYC/blob/master/images/map3.PNG)

![Minority per 100,000 (updated Jun 23, 2020)](https://github.com/LilyTruong2291/COVID19-in-NYC/blob/master/images/map4.PNG)

The darker the purple shade is the higher the number. The chloropleth maps shows that some neighborhood in Bronx and Queens has high concentration of minority people living below poverty. That same areas also show the higher number of COVID cases.
More data visulization can be found [here](https://github.com/LilyTruong2291/COVID19-in-NYC/blob/master/data_eda.ipynb)

## Findings

My analysis led me to the conclusion that the available evidence does not support the hypothesis that COVID-19 disproportionately affects low-income areas. More data is needed to explore this issue further. Namely, I'd be very interested in adding employment data and commuting patterns to get a more accurate picture. 

*Thanks to **Farrokh Mansouri** for his mentorship in this domain.* 

https://www.linkedin.com/in/farrokh-mansouri-b570b1b/

