# Weather Data Pipeline  

## Project Overview  

This project is an end-to-end weather monitoring and analytics pipeline built with Python and Power BI.  
The pipeline automatically collects live weather data for Athens from a public weather website,  
stores the data in a CSV file, sends rainfall email alerts, and visualizes the collected time-series data  
in an interactive Power BI dashboard.  
The project was designed to simulate a lightweight real-world data workflow:  
## Web Scraping → Automated Data Collection → CSV Storage → Email Alerts → Power BI Analytics  

## Technologies Used  

Python  
BeautifulSoup  
Requests  
CSV Storage  
Windows Task Scheduler  
SMTP Email Alerts  
Power BI  
Git & GitHub 

## Project Structure  
- [data/](data/) — Collected weather dataset in CSV format
- [src/](src/) — Python pipeline script
- [requirements.txt](requirements.txt) — Python dependencies 

## Data Collection Pipeline  

The Python pipeline performs the following steps:  

Sends an HTTP request to the weather website  
Parses the HTML using BeautifulSoup  
Extracts:  
Temperature  
Humidity  
Daily rainfall  
Timestamp  
Stores the results into a CSV file  
Detects rainfall events  
Sends automated email alerts when rainfall starts  

The pipeline was scheduled using Windows Task Scheduler and collected weather data automatically at regular intervals.  
 
## Data Collected  

The dataset contains:  

City  
Temperature (°C)  
Humidity (%)  
Rainfall (mm)  
Timestamp  

The data was collected for one full week with hourly measurements during daytime and evening hours.  



## Email Alert System  

The project includes an automated rainfall detection system.  
Logic used:  
if previous_rain == 0 and rain_value > 0:  
When rainfall starts:  
An email alert is automatically sent  
Rain events are logged into the dataset  

SMTP email credentials were removed from the public repository for security reasons.  

## Power BI Dashboard  

The Power BI dashboard was built using the collected CSV dataset.  

The dashboard includes:  

KPI Cards  
Average Temperature  
Maximum Temperature  
Minimum Temperature  
Average Humidity  
Total Rainfall  

Time-Series Analysis
  
- Temperature Trend Over Time  
A continuous time-series visualization showing temperature fluctuations throughout the week.  

- Average Temperature by Hour  
Shows the average daily temperature pattern based on hourly aggregation.  
Main observation:  
Temperatures increase toward midday and afternoon  
Temperatures decrease during evening hours
 
- Humidity Trend Over Time  
Area chart used to visualize humidity variability over time.  

Correlation Analysis

-Temperature vs Humidity Relationship  
Scatter plot used to analyze the relationship between temperature and humidity.  
Main observation:  
Higher temperatures generally correspond to lower humidity levels  
The trend line shows a negative correlation tendency  

## How to Run  
1. Install dependencies  
pip install -r requirements.txt  
2. Run the pipeline manually  
python src/scraper_step1.py  
3. Configure automation  
Use Windows Task Scheduler to run the script periodically.

## Notes
The dataset was collected from 'Meteo' publicly available weather data.  
Email credentials were removed for security purposes.  
The project focuses on building a lightweight end-to-end analytics workflow using real collected data.  

## Author
Georgios Konstantopoulos


