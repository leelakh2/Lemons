**Project-Plan: Lemons**

**Overview**

The goal of this project is to understand the relationship between shark behavior and weather patterns. Specifically, our team was interested in learning if certain weather patterns or temperature changes cause an increase in shark activity that leads to an increased level and severity of shark attacks. We plan to achieve this by curating datasets about the shark attacks globally since World War II, as well as temperature and storm data globally since World War II. These attributes, time and location, will be how we integrate the datasets together to begin learning more about the correlation between these patterns. We plan to first look at the quality and layout of the datasets and ensure the date and location variables can be matched. Then, we will clean and standardize the data, especially differences in dates and geographic information, before combining the datasets. Once they are integrated, we will compare shark attack patterns with temperature changes and tropical cyclone activity to see if there are any noticeable relationships over time and across locations.

**Team**

Leela was focused on finding the shark attack data, which was more intensive due to the unique nature of the dataset. Afterwards, her work will be centered around cleaning and integrating the data.
Kaylee was focused on finding and preparing the global climate dataset which needed to be adjusted in order to upload. The edited NOAA Global Historical Climatology Network - Monthly (GHCN-M) dataset is filtered to include data from 1945 onwards. It was adjusted to reduce the size of the file in order to upload and be stored in GitHub(both the edited dataset and the script used to create it are in the repository). Her work will also focus on helping to integrate the climate data with the shark attack and storm datasets utilizing both data and location. 
Catie [add stuff]
Jiya was focused on finding and preparing the global tropical cyclone dataset. She found the NOAA IBTrACS dataset, filtered it to include data from 1945 onward, reduced the number of observations so the file could be stored in GitHub, and added both the processed dataset and the script used to create it. Her work will also focus on helping integrate the storm data with the shark attack data using time and location.

**Research Question**

Do changes in weather patterns and storm severity have an effect on shark attacks?

**Datasets**

The first dataset lists shark attacks recorded throughout the world since World War II. Several pieces of information are included when possible, including the date of the attack; whether the attack was provoked or unprovoked; country, state, and location of attack; the name, age, and gender of the victim as well as what activity they were doing and what injury was sustained; whether the attack was fatal; and the species of shark.

The second dataset is NOAA's Global Historical Climatology Network - Monthly (GHCN-M) dataset which contains average temperatures recorded at weather stations around the world. It can be connected to the other two datasets via matching the events(cyclone or shark attack) to the nearest station and month. For the purposes of this project, we are using data from 1945 onwards so the time period matches up nicely with the other datasets. This dataset includes information about the station ID, latitude, longitude, year, and average temperature each month in degrees Celsius. Due to the size of the original file, we made some adjustments in order to shrink the size of the file while still keeping the years and variables needed. Some of the adjustments included removing the stations near the North and South Poles where there aren't likely any shark attacks and removing data prior to 1945. 

Our third dataset is NOAA's International Best Track Archive for Climate Stewardship (IBTrACS), which contains historical tropical cyclone data from around the world. For this project, we are using records from 1945 onwards so the time period better matches the shark attack data. The dataset includes information such as the storm name, date, ocean basin, latitude and longitude, wind speed, and storm intensity. Because the original global file was very large, we created a smaller version with one observation per storm per day while keeping the variables that are most useful for out project. This dataset can be connected to the shark attach data using date and geographic location.

**Timeline**

Our first goal was to have all three datasets chosen and a rough plan on how to connect them all by the time our project outline is due (Monday, Nov 12).
In the next 1-2 weeks we want to make sure that our datasets are cleaned, checked for missing values, and standardized(especially location, dates and units). 
After that, we plan on integrating the datasets by matching up the shark attacks and tropical cyclones with the nearest weather station and month. 
Following that, we will work on analysis, evaluating visuals and starting to think about key takeaways. 
[insert rest of timeline & maybe more precise dates]

**Constraints**

A limitation of this dataset is that the shark attacks can only be determined by one dataset, so the other datasets were filtered based on the similarity of their attributes to the shark attack data. Because shark attacks are not on a predictable schedule, there will be a lot of weather and climate data that will have to be discarded or summarized to match shark attack dates.
Another challenge is that the datasets do not all use the same level of geographic detail. Shark attacks may include specific beaches or cities, while the tropical cyclone and temperature data may use broader locations or coordinates. We will need to standardize these before combining the datasets. Older records may also have more missing or inconsistent information.

**Gaps**

We still need to decide what geographic level to use when connecting the datasets and which temperature variables will be most useful. We also need to determine how close in time and location a weather event should be to a shark attack for it to be considered related.


