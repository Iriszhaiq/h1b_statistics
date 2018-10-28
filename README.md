# [Insight Data Science Coding Challenge ](https://github.com/InsightDataScience/h1b_statistics)

## Table of Contents:
* [Problem](#Problem)
* [Approach](#Approach)
* [Run instructions](#Run_instruction)

##Problem
A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). But while there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years. 

The main task is to create a mechanism to analyze past years data, specificially calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.
##Approach
In order to get the sorted list of occupation and states based on the certified application number, I listed my approach as below:


1. Get the one input filepath and two output filepath through `sys.argv` parsed in from command line wrote in the `run.sh` script. 
2. Read the csv file into two parts: the first line to a list of labels and the remaining lines as a list of records list.  
3. Used keyword match to get the relavant index of the occupations, the states, and the visa status and save records according to the index number in *"soc_list"*, *"state_list"*, and *"status_list"* respectively. 
	- Occupations keyword: **"SOC_NAME"**
	- States keyword: **"STATUS"**
	- Visa status keyword: **{"WORKLOC1_STATE"}** or **{"STATE" and "WORK"}**
3. Filtered the records lists *"soc_list"* and *"state_list"* according to *"CERTIFIED"* in **"status_list"**. Saved those filtered records as keys and count as values in two dictionary **"occupations"** and **"states"** respectively. [Each time encounted a "CERTIFIED" records, count+=1]
4. Sum the values of the dictionary values in either dictionary and saved to **'total_certified'** as the total count of applications that have been certified in that state.
5. Create and open two txt files __`top_10_occupations.txt`__ and __`top_10_states.txt`__
6. Use for loop to iterate the first 10 **key**, **value** and **percentage(value/total_certified)** from sorted dictionaries *"occupations"* and *"states"* line by line and parsed them into string using ";" to seperate them. 
	- The sorted mechanism is based on dictionary's **value** (in reverse order) and **key** if value in a tie.


##Run Instructions

Run `run.sh` under root directory and the output would be stored under the `./output` folder.

- Unit test: By running the script `run_tests.sh` within the `insight_testsuite` folder to test your directory structure and output format
- To get output files for specific csv file, edited on the `run.sh` on main directory. Changed the `./input/h1b_input.csv` to the directory of your targeted file. You can also changed the output directory and filename by changing the following argument ` ./output/top_10_occupations.txt`, `./output/top_10_states.txt`. 






