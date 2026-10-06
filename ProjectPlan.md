**Project-Plan: Lemons**

**Overview**
The goal of this project is to understand the relationship between shark behavior and weather patterns. Specifically, our team was interested 
in learning if certain weather patterns or temperature changes cause an increase in shark activity that leads to an increased level and 
severity of shark attacks. We plan to achieve this by curating datasets about the shark attacks globally since World War II, as well as 
temperature and storm data globally since World War II. These attributes, time and location, will be how we integrate the datasets 
together to begin learning more about the correlation between these patterns. We plan to first look at the quality and layout of the datasets and ensure the date and location variables can be matched. Then, we will clean and standardize the data, especially differences in dates and geographic information, before combining the datasets. Once they are integrated, we will compare shark attack patterns with temperature changes and tropical cyclone activity to see if there are any noticeable relationships over time and across locations.

**Team**
Leela was focused on finding the shark attack data, which was more intensive due to the unique nature of the dataset. Afterwards, her work was
centered around [...]
Kaylee [add stuff]
Catie [add stuff]
Jiya was focused on finding and preparing the global tropical cyclone dataset. She found the NOAA IBTrACS dataset, filtered it to include data from 1945 onward, reduced the number of observations so the file could be stored in GitHub, and added both the processed dataset and the script used to create it. Her work will also focus on helping integrate the storm data with the shark attack data using time and location.

**Research Question**
Do changes in weather patterns and storm severity have an effect on shark attacks?

**Datasets**
The first dataset lists shark attacks recorded throughout the world since World War II. Several pieces of information are included when 
possible, including the date of the attack; whether the attack was provoked or unprovoked; country, state, and location of attack; the name, 
age, and gender of the victim as well as what activity they were doing and what injury was sustained; whether the attack was fatal; and the 
species of shark.
[Add dataset 2 info]
Our third dataset is NOAA's International Best Track Archive for Climate Stewardship (IBTrACS), which contains historical tropical cyclone data from around the world. For this project, we are using records from 1945 onwards so the time period better matches the shark attack data. The dataset includes information such as the storm name, date, ocean basin, latitude and longitude, wind speed, and storm intensity. Because the original global file was very large, we created a smaller version with one observation per storm per day while keeping the variables that are most useful for out project. This dataset can be connected to the shark attach data using date and geographic location.

**Timeline**
[insert timeline]

**Constraints**
A limitation of this dataset is that the shark attacks can only be determined by one dataset, so the other datasets were filtered based on 
the similarity of their attributes to the shark attack data. Because shark attacks are not on a predictable schedule, there will be a lot 
of weather and climate data that will have to be discarded or summarized to match shark attack dates.
Another challenge is that the datasets do not all use the same level of geographic detail. Shark attacks may include specific beaches or cities, while the tropical cyclone and temperature data may use broader locations or coordinates. We will need to standardize these before combining the datasets. Older records may also have more missing or inconsistent information.

**Gaps**
We still need to decide what geographic level to use when connecting the datasets and which temperature variables will be most useful. We also need to determine how close in time and location a weather event should be to a shark attack for it to be considered related.


