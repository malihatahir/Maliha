This dataset examines open parking and camera violations in New York City. 

The folder structure is as follows:

project01/
+-- Dockerfile
+-- requirements.txt
+-- src/
+-- +-- main.py
+-- +-- elastic_helper.py
+-- +-- config.py
+-- assets/
+-- +-- kibanadashboard.png
+-- +-- count.png
+-- README

To build the docker image type the following in the terminal:

docker build -t bigdata1:1.0 project01/

After this change directory to project01 by using the following command:
cd project01/

In order to run the dockcer container use the following command:

docker run -d \
  -v ${PWD}:/app \
  -e APP_TOKEN=your app token \
  -e ES_HOST=your elastic endpoint \
  -e ES_USERNAME=your username \
  -e ES_PASSWORD=your password \
  bigdata1:1.0 --page_size=1 --num_pages=1 (--page_size and --num_pages can be changed based on user preference of how many rows they want to get)

  I pulled all the fields except for violation_status and summons_image becasue I didn't think they were necessary for my analysis. 

  I created four visulaizations using Kibana.
  1) Line chart showing average penalty amount for top 25 states.
  2) Horizontal Bar graph showing average reduction amount for the five boroughs. New York had the highest.
  3) Tag cloud showing the most popular violations. 
  4) A guage to count the rows in DB. There are 1,000,801 rows.

   

  