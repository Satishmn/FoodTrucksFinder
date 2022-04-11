# FoodTrucksFinder

# about
This is a web app displays the list of food trucks available from the csv data available from the url https://data.sfgov.org/api/views/rqzj-sfat/rows.csv
and also gives the options to select trucks/food cart types and zip codes and the data tables are dynamically get updated.

The visualizations also get updated with the selctions/filters.
also tried to show a seperate list for Tacos to demonatrate the capability to display trucks by a food item.

# Techinical details and approach
--Requirements used Lnguage : Python Libraries : plotly,streamlit,pandas,openpyxl,pillow libraries Repository : Github Workspace used to collabrate my python application is : Streamlit Cloud

Understood the dataset and explored the columns for understanding how best I can use selective columns to improve web application response time.

1) Get all the requirements and libraries setup. In this scenario I used python as the coding language and used plotly,streamlit,pandas,openpyxl,pillow libraries
2) Import all the libraries and set up a header for my webpage,here it is 'Foodtruck'
3) Using pandas loaded dataframe with data from csv provided in the URL.
4) After understanding the data the next most important scenario is to clean data and have data validations
5) Here all the NaNs were dropped and zipcode validation were implemented to restrict the zipcode to 5 digit.
6) Sidebars were implemented for FacilityType and ZipCode in order to allow the customer to select what type of food truck are they looking for truck or pushcart,and for which zipcode are they looking in.
7) Based on the customers selection of zipcode and type of cart the data visuals on the website refresh in order to display filtered data.

# visualizations
We can see the number of results for selected criteria.
1) Data Visual1 :DATAFRAME: We can see the data displayed in a dataframe for entire food items available in that particular zipcode and facility type.
2) Data Visual2 :DATA TABLE: Below we can see a data table displayed with what are the tacos available and for which applicants they are available in the selected criteria.
 We can set the taco variable to any dynamic value so incase the requirement changes to retrieve the number of food trucks available in a particular zipcode with tacos to any other type of food like noodles,it will retuen that. For current code as per requirement it is returning only taco food items.
3) Data Visual3 :PIE CHART: The next data visual is a pie chart showing the percentage of facility type like trucks,pushcarts ratio for that particular selection criteria
4) Data Visual4 :BAR GRAPH: Bar graph dislaying the food items available for the selection criteria
5) Data Visual5 : List of food items vailable in the selection criteria.
6) Data Visual6 : Retunr a JSON file set of results for selection criteria.

# test run
The application can be direcltly tested using streamlit run /app.py

# Docker image, build and run
Dockerfile is created to build the image for the web app

docker build -t food-truck-web-app .
docker run -p 8501:8501 food-truck-web-app streamlit run /src/app.py
