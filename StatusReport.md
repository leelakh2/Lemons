
# Status Report: Group Lemons

## Overview

The goal of our project is to understand the relationship between shark attacks and weather patterns. Specifically, we want to see if changes in temperature and tropical cyclone activity have any noticeable relationship with the number and severity of shark attacks. To explore this, we are using three datasets: historical shark attack records, NOAA's Global Historical Climatology Network - Monthly (GHCN-M) temperature data, and NOAA's International Best Track Archive for Climate Stewardship (IBTrACS) tropical cyclone data.

So far, we have found and prepared our three datasets and have started working through some of the challenges involved in cleaning and connecting them. One of the biggest decisions we made was to narrow our project from a global analysis to focusing on the United States, Australia, and South Africa. We believe this change will make the project more manageable while still allowing us to explore our original research question.

## Progress on Project Tasks

### Data Collection and Preparation

We have collected all three datasets needed for our project and made adjustments to reduce their sizes and prepare them for integration.

**Shark Attack Data:** Leela was responsible for finding the historical shark attack dataset. The updated CSV contains 39,230 records and includes information such as the date, country, state, location, activity, injuries, and whether the attack was fatal. After looking through the data, we found that the United States had the most recorded attacks with 2,593, followed by Australia with 1,536 and South Africa with 599. These three countries have 4,728 records combined across all available years. When limiting the records to 1945 onward, we have 3,654 records remaining before further cleaning. The OpenRefine archive files, as well as the cleanest CSV, are uploaded to our Github repository.  
[Original Shark Attack Data](GSAF5(1).xls)  

**Temperature Data:** Kaylee was responsible for finding and preparing NOAA's GHCN-M dataset. The original dataset was very large, so she filtered it to include records from 1945 onward and removed stations near the North and South Poles where shark attacks are unlikely to occur. This helped reduce the size of the file while keeping the temperature information we need. The processed dataset and the script used to prepare it have been added to our GitHub repository.  
[Temperature Data Processing Script](kaylee_script_to_shrink_data.py)  

**Tropical Cyclone Data:** Jiya and Catie were responsible for finding and preparing NOAA's IBTrACS dataset. Since the original file was also very large, they filtered it to include storms that occurred from 1945 onwards and were confirmed main track records. This allowed us to keep important information such as storm dates, locations, wind speeds, and intensity while making the file easier to store and work with. The processed dataset and the Python script used to prepare it have also been added to GitHub. The data was then uploaded to an OpenRefine project for cleaning and integration.  
[Cyclone Data Processing Script](prepare_ibtracs.py)  

### Data Quality Assessment and Cleaning

One issue we have noticed is that the datasets contain location information in different formats. For example, the shark attack data includes specific beaches, cities, and states, while the temperature and cyclone datasets use geographic coordinates or weather station locations. We will need to make these locations consistent before connecting the datasets, such as linking them to nearby cities and states to compare more easily.

The **shark attack dataset** also contains missing information and unnecessary columns. The updated CSV has 185 columns, but 170 of them are completely empty. We will need to remove these unnecessary columns and decide how to handle records with missing information. Many of these columns have been deleted, and a lot of the typos and incorrectly inputted locations have been fixed based on references to Wikidata and the Internet to determine the authenticity of different listed locations. Most of the data is complete, but the typos have altered the accuracy level and limit the ability to automatically cluster attacks from the same areas.  
[Cleaned Shark Attack Data](Shark-Attack-Data.csv)  
[Shark Attack OpenRefine Project](Shark-Attack-Data.openrefine.tar.gz)

The **temperature dataset** was filtered to only include stations in the United States, Australia, and South Africa, which reduced it from 1,043,655 rows to 558,396 rows. One issue we noticed is that the dataset uses different country codes than expected, such as “SF” for South Africa and “AS” for Australia, so we had to be careful when filtering. The temperature data also has missing values, since many years are missing temperatures for one or more months. We decided to leave these blank instead of filling them in so we do not add estimated values.  
[Stations to Cities Data](station_cities.csv)  
[Nearest City Matching Script](nearest_city_matching.ipynb)  
[Temperature OpenRefine History](openrefine_history_ghcnm.json)  
[Stations OpenRefine History](openrefine_history_stations.json)  

The **cyclone dataset** was filtered to only contain data from storms that occurred in the year 1945 or after. Additionally, we chose to only keep records with the "main" track type, meaning the data is associated with the primary track of the storm. After applying these filters, there are a total 508,181 records documenting 8,620 unique storms. While processing the data, there was an issue with pandas and OpenRefine classifying the label NA (North Atlantic) with null values, which we were able to catch with an update to the processing script. Additionally there were missing values for both the wind speed and name attributes, which we are choosing to keep as null values. The location parameters in this dataset are latitude and longitude coordinates and the distance from land for each observation of the storm, so we will need to use reverse geocoding to pull the closest cities and countries of each record.  
[Cleaned Cyclone Data](ibtracs-cleaned-csv.csv)  
[Cyclone OpenRefine Project](ibtracs-cleaned-csv.opentrefine.tar.gz)

### Database Design and Data Integration

Our plan is still to connect the three datasets using time and geographic location. However, we need to decide exactly how we want to match the locations across the datasets.

We originally considered using Wikidata to match the shark attack locations, but doing this for locations across the entire world would take a significant amount of time. By narrowing our project to three countries, we hope to make the matching process more manageable.

We also need to consider the differences in how time is recorded. For example, the temperature dataset contains monthly averages, while shark attacks and tropical cyclones have specific dates. We will need to decide how to connect these records in a way that makes sense for our research question.

We have started matching locations using the temperature data. Each of the 13,288 weather stations was matched to its nearest city using city locations from Wikidata, and the city information was added back to the temperature dataset. Since each city has a Wikidata ID, we may be able to use these IDs to connect the shark attack locations to the same cities. Some of the shark attack locations are listed as specific beaches or tiny towns within a specific region, which would make it harder to match to the specific cities in the other datasets. To mitigate this, some of these beaches in a specific city are mapped to that city to allow them to more easily match using location as the key. 

The cyclone data only records locations as latitude and longitude coordinates that are mostly in the ocean. To work with this, we are planning on narrowing down our records to ones that are within a certain distance to land and reverse geocoding the coordinates to get a country. If the record is for a location in the US, South Africa, or Australia, we will keep the record and find the city that the coordinates correspond to.

### Data Analysis and Visualization

Once we finish integrating the datasets, we plan to compare shark attack patterns with temperature changes and tropical cyclone activity. We want to see whether certain weather conditions are associated with increases or decreases in shark attacks over time.

Looking just at the shark attack data, the number of total shark attacks across our three chosen countries increases substantially between the 1990s and the 2000s, from 45 attacks in 1999 to 75 in 2000. And this higher rate continues throughout the next decade. Although not yet compared to the other datasets, this could be partly attributed to general global rising temperatures. This can be confirmed by comparison with the temperature and cyclone levels across specific years, instead of just locations. Trends can be found across different cities, but we are also able to observe global trends across different years. 


### Workflow Automation and Documentation

We plan to create a workflow that connects the different steps of our project, from data acquisition and cleaning to integration and analysis. We already have scripts for preparing the temperature and tropical cyclone datasets, but we still need to organize the full process so it can be run from beginning to end.

We will also need to document our steps and test the workflow on a clean copy of the repository to make sure everything runs properly.

For the temperature data, we added the Wikidata queries, the Python notebook used to match stations to cities, and the OpenRefine history files to GitHub so these steps can be repeated. The shark attack data and cyclone data have also been uploaded to Github as its OpenRefine archive, so the history of cleaning and Wikidata matching is available and repeatable. 


## Changes to Our Project Plan

The biggest change we have made to our project plan is narrowing the geographic scope. Originally, we wanted to use shark attack records from around the world. However, after reviewing the data, we realized that matching each location through Wikidata would take a significant amount of time.

We discussed this as a group and decided that focusing on the countries with the most recorded shark attacks would be a better approach. The three countries we selected are the United States, Australia, and South Africa, which have 2,593, 1,536, and 599 recorded attacks, respectively, across all available years.

This change will allow us to spend less time trying to match locations across the entire world and more time on the actual cleaning and integration process. We also believe that these three countries provide enough information for us to explore our research question, since each has well over the minimum of 100 records required for the project.

Our overall goal has not changed. We still want to understand how shark attacks relate to temperature and tropical cyclone activity. We are simply narrowing our focus to make the project more realistic with the time we have available. We understand that our findings will be limited to these countries rather than representing shark attacks globally.

We have updated our project plan to reflect this decision.


## Challenges and Solutions

**Large datasets:** One of our first challenges was that the temperature and tropical cyclone datasets were too large to conveniently upload to GitHub. We addressed this by filtering both datasets to include data from 1945 onward and reducing unnecessary observations while keeping the variables we needed. We also decided to limit the countries in our scope to allow for more quality analysis without too much quantity. 

**Matching locations:** Another major challenge has been figuring out how to match shark attack locations with the climate and cyclone data. The shark attack dataset contains many specific locations, and matching all of them through Wikidata would take a long time. To address this, we decided to narrow our focus to the three countries with the most recorded attacks: Australia, South Africa, and the United States. For the temperature data, we sped up the matching process by reducing the data to one row per station before matching it to cities. We still need to finalize how we will match the shark attack and cyclone locations, because the latitude and longitude included in the dataset are in the middle of the ocean instead of a coastal city.

**Differences between datasets:** The datasets do not all record information in the same way. The shark attack data includes specific dates and locations, while the climate data contains monthly temperature averages from weather stations. We will need to standardize these differences before integration. This may be done by using the monthly temperature average to be applied to any shark attacks within that month, but will not be as easy to automatically match. 

**Missing information:** Some shark attack records are missing location details or other important information. We will need to decide how to handle these records and determine which ones can reasonably be included in our final dataset. Some of the specific towns and beaches are not findable on Wikidata when reconciling to the city. So we had to reconcile based on country and then state or province, before finally matching some of the unknown locations to the nearest city instead of the actual town or coast. 

## Updated Timeline

11/15 - Complete data cleaning and quality assessments; finalize conceptual database model

11/16 - Complete database creation and data integration; **Interim Status Report submission**

11/23 - Complete data analysis and visualizations; organize scripts for automated workflow

11/30 - Complete automated workflow, collect documentation from team members, and finish initial draft of final report

12/04 - Test workflow on a clean clone and complete final repository checks

12/07 - **Final Project submission**

*These are our updated target dates based on the remaining work and may change depending on our progress.*

## Individual Contributions

### Leela

Leela was responsible for finding the historical shark attack dataset and is working on preparing it for integration with the temperature and cyclone data. She cleaned the data globally to begin matching the country, state/province, and city with Wikidata matches. 

For this milestone, Leela finished cleaning all of the data and narrowed the scope to include just South Africa, the United States, and Australia. She matched all of the rows to the country using Wikidata, and to the exact state or province within the country. She is working on matching each specific location to the nearest city, which takes extensive time due to the specificity of each beach or town that is not always listed on Wikidata. To allow a clearer match for the other datasets, Leela is matching the location to the city encompassing it. That way, it can be linked to the cities that temperature is recorded in. She also added the updated data and OpenRefine file to Github. 

### Kaylee

Kaylee was responsible for finding and preparing NOAA's GHCN-M temperature dataset. She filtered the data to include records from 1945 onward and reduced the file size so it could be stored in GitHub. She also added the processed dataset and the script used to prepare it.

For this milestone, Kaylee filtered the GHCN-M dataset to the United States, Australia, and South Africa using OpenRefine. She used Wikidata and a Python script to match each weather station to its nearest city and added this information back to the temperature dataset. She also added the queries, notebook, and updated data to GitHub.

### Catie

Catie is responsible for data analysis, visualization, and documenting the steps of the project. She is also helping organize the workflow from data acquisition through analysis.

For this milestone, Catie analyzed and cleaned the IBTrACS tropical cyclone set using OpenRefine. She made edits to Jiya's initial preparation script to ensure that there is enough information to accurately assess the quality and information in this dataset. She explored different ways to translate the coordinates in the dataset to cities/countries using reverse geocoding, and plans on discussing these ideas with the group's TA.  

### Jiya

Jiya was responsible for finding and preparing NOAA's IBTrACS tropical cyclone dataset. She filtered the data to include records from 1945 onward and reduced the observations to one per storm per day. She also added the processed dataset and preparation script to GitHub.

For this milestone, Jiya helped update the project plan to reflect our decision to focus on the United States, Australia, and South Africa instead of using data from every country. She also worked on the status report to document our progress, changes to the project plan, and challenges encountered so far.

## Next Steps

Our main priority moving forward is to finish cleaning the datasets and determine how we will match locations across the three sources. Once we have a consistent way to connect the records, we can finish the database and integration process and begin working on our analysis and visualizations.

We also need to complete the automated workflow, document our steps, and make sure the entire project can be reproduced from a clean copy of our GitHub repository.

Although we have changed the scope of our project, we believe this adjustment will help us focus more on the quality of our data and the integration process, which are the most important parts of the project.
