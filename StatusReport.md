
# Status Report: Group Lemons

## Overview

The goal of our project is to understand the relationship between shark attacks and weather patterns. Specifically, we want to see if changes in temperature and tropical cyclone activity have any noticeable relationship with the number and severity of shark attacks. To explore this, we are using three datasets: historical shark attack records, NOAA's Global Historical Climatology Network - Monthly (GHCN-M) temperature data, and NOAA's International Best Track Archive for Climate Stewardship (IBTrACS) tropical cyclone data.

So far, we have found and prepared our three datasets and have started working through some of the challenges involved in cleaning and connecting them. One of the biggest decisions we made was to narrow our project from a global analysis to focusing on the United States, Australia, and South Africa. We believe this change will make the project more manageable while still allowing us to explore our original research question.

## Progress on Project Tasks

### Data Collection and Preparation

We have collected all three datasets needed for our project and made adjustments to reduce their sizes and prepare them for integration.

**Shark Attack Data:** Leela was responsible for finding the historical shark attack dataset. The updated CSV contains 7,117 records and includes information such as the date, country, state, location, activity, injuries, and whether the attack was fatal. After looking through the data, we found that the United States had the most recorded attacks with 2,593, followed by Australia with 1,536 and South Africa with 599. These three countries have 4,728 records combined across all available years. When limiting the records to 1945 onward, we have 3,789 records remaining before further cleaning.

**Temperature Data:** Kaylee was responsible for finding and preparing NOAA's GHCN-M dataset. The original dataset was very large, so she filtered it to include records from 1945 onward and removed stations near the North and South Poles where shark attacks are unlikely to occur. This helped reduce the size of the file while keeping the temperature information we need. The processed dataset and the script used to prepare it have been added to our GitHub repository.

**Tropical Cyclone Data:** Jiya was responsible for finding and preparing NOAA's IBTrACS dataset. Since the original file was also very large, she filtered it to include records from 1945 onward and reduced the observations to one per storm per day. This allowed us to keep important information such as storm dates, locations, wind speeds, and intensity while making the file easier to store and work with. The processed dataset and the Python script used to prepare it have also been added to GitHub.

### Data Quality Assessment and Cleaning

One issue we have noticed is that the datasets contain location information in different formats. For example, the shark attack data includes specific beaches, cities, and states, while the temperature and cyclone datasets use geographic coordinates or weather station locations. We will need to make these locations consistent before connecting the datasets.

The shark attack dataset also contains missing information and unnecessary columns. The updated CSV has 185 columns, but 170 of them are completely empty. We will need to remove these unnecessary columns and decide how to handle records with missing information.

[Team members: Add the cleaning steps completed so far and the results of the data quality assessments. Include accuracy, completeness, timeliness, and consistency for each dataset.]

### Database Design and Data Integration

Our plan is still to connect the three datasets using time and geographic location. However, we need to decide exactly how we want to match the locations across the datasets.

We originally considered using Wikidata to match the shark attack locations, but doing this for locations across the entire world would take a significant amount of time. By narrowing our project to three countries, we hope to make the matching process more manageable.

We also need to consider the differences in how time is recorded. For example, the temperature dataset contains monthly averages, while shark attacks and tropical cyclones have specific dates. We will need to decide how to connect these records in a way that makes sense for our research question.

[Team members: Add progress on the conceptual database model, database creation, integration scripts, and any matching or integration already completed.]

### Data Analysis and Visualization

Once we finish integrating the datasets, we plan to compare shark attack patterns with temperature changes and tropical cyclone activity. We want to see whether certain weather conditions are associated with increases or decreases in shark attacks over time.

[Team members: Add any analysis, visualizations, or preliminary findings completed so far.]

### Workflow Automation and Documentation

We plan to create a workflow that connects the different steps of our project, from data acquisition and cleaning to integration and analysis. We already have scripts for preparing the temperature and tropical cyclone datasets, but we still need to organize the full process so it can be run from beginning to end.

We will also need to document our steps and test the workflow on a clean copy of the repository to make sure everything runs properly.

[Team members: Add any completed workflow scripts, documentation, or testing.]

## Changes to Our Project Plan

The biggest change we have made to our project plan is narrowing the geographic scope. Originally, we wanted to use shark attack records from around the world. However, after reviewing the data, we realized that matching each location through Wikidata would take a significant amount of time.

We discussed this as a group and decided that focusing on the countries with the most recorded shark attacks would be a better approach. The three countries we selected are the United States, Australia, and South Africa, which have 2,593, 1,536, and 599 recorded attacks, respectively, across all available years.

This change will allow us to spend less time trying to match locations across the entire world and more time on the actual cleaning and integration process. We also believe that these three countries provide enough information for us to explore our research question, since each has well over the minimum of 100 records required for the project.

Our overall goal has not changed. We still want to understand how shark attacks relate to temperature and tropical cyclone activity. We are simply narrowing our focus to make the project more realistic with the time we have available. We understand that our findings will be limited to these countries rather than representing shark attacks globally.

We have updated our project plan to reflect this decision.

[Team members: Add any changes made in response to feedback received on the original project plan.]

## Challenges and Solutions

**Large datasets:** One of our first challenges was that the temperature and tropical cyclone datasets were too large to conveniently upload to GitHub. We addressed this by filtering both datasets to include data from 1945 onward and reducing unnecessary observations while keeping the variables we needed.

**Matching locations:** Another major challenge has been figuring out how to match shark attack locations with the climate and cyclone data. The shark attack dataset contains many specific locations, and matching all of them through Wikidata would take a long time. To address this, we decided to narrow our focus to the three countries with the most recorded attacks. We still need to finalize how we will match locations within those countries.

**Differences between datasets:** The datasets do not all record information in the same way. The shark attack data includes specific dates and locations, while the climate data contains monthly temperature averages from weather stations. We will need to standardize these differences before integration.

**Missing information:** Some shark attack records are missing location details or other important information. We will need to decide how to handle these records and determine which ones can reasonably be included in our final dataset.

## Updated Timeline

11/16 - Complete data cleaning and quality assessments; finalize conceptual database model

11/19 - Complete database creation and data integration; **Interim Status Report submission**

11/23 - Complete data analysis and visualizations; organize scripts for automated workflow

11/30 - Complete automated workflow, collect documentation from team members, and finish initial draft of final report

12/04 - Test workflow on a clean clone and complete final repository checks

12/07 - **Final Project submission**

*These are our updated target dates based on the remaining work and may change depending on our progress.*

## Individual Contributions

### Leela

Leela was responsible for finding the historical shark attack dataset and is working on preparing it for integration with the temperature and cyclone data.

[Leela: Add specific work completed for this milestone, including data cleaning and integration.]

### Kaylee

Kaylee was responsible for finding and preparing NOAA's GHCN-M temperature dataset. She filtered the data to include records from 1945 onward and reduced the file size so it could be stored in GitHub. She also added the processed dataset and the script used to prepare it.

[Kaylee: Add any additional work completed for this milestone.]

### Catie

Catie is responsible for data analysis, visualization, and documenting the steps of the project. She is also helping organize the workflow from data acquisition through analysis.

[Catie: Add specific work completed for this milestone.]

### Jiya

Jiya was responsible for finding and preparing NOAA's IBTrACS tropical cyclone dataset. She filtered the data to include records from 1945 onward and reduced the observations to one per storm per day. She also added the processed dataset and preparation script to GitHub.

For this milestone, Jiya helped update the project plan to reflect our decision to focus on the United States, Australia, and South Africa instead of using data from every country. She also worked on the status report to document our progress, changes to the project plan, and challenges encountered so far.

## Next Steps

Our main priority moving forward is to finish cleaning the datasets and determine how we will match locations across the three sources. Once we have a consistent way to connect the records, we can finish the database and integration process and begin working on our analysis and visualizations.

We also need to complete the automated workflow, document our steps, and make sure the entire project can be reproduced from a clean copy of our GitHub repository.

Although we have changed the scope of our project, we believe this adjustment will help us focus more on the quality of our data and the integration process, which are the most important parts of the project.
