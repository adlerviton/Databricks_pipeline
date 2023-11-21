# Databricks Pipeline

[![CI](https://github.com/adlerviton/Databricks_pipeline/actions/workflows/python.yml/badge.svg)](https://github.com/adlerviton/Databricks_pipeline/actions/workflows/python.yml)

Week 11: Data Pipeline with Databricks

## Pipeline Flow:

#### Ingest Raw Data
- Using the Ingest songs data script, it takes in data from one of the databricks sample data sources and uses spark to create a table called raw_songs_table in the DBFS

#### Prepare Data
- Uses the Prepare songs data script to create another SQL table called prepared_song_data in the DBFS which has a limited number of columns from the raw data. Here we can see the the table being filled with data from the raw table successfully.
  ![image](https://github.com/adlerviton/Databricks_pipeline/blob/main/Images_mini_11/Prep_and_Insert.png)

#### Analyze the Data
- Uses the Analyze songs data script to run 2 different SQL queries:
- First creates a ranking of how many songs each artist has released in a single year, ordering them from highest to lowest:
  ![image](https://github.com/adlerviton/Databricks_pipeline/blob/main/Images_mini_11/Query1.png)

- Second show all of the songs produced with a time signature of 4 and tempo between 100 and 140 bpm:
  ![image](https://github.com/adlerviton/Databricks_pipeline/blob/main/Images_mini_11/Query2.png)

  ## Job:

  Here is the workflow set up to automate the pipeline in databricks:
  ![image](https://github.com/adlerviton/Databricks_pipeline/blob/main/Images_mini_11/Job.png)

  And the success of the job running is shown below:
    ![image](https://github.com/adlerviton/Databricks_pipeline/blob/main/Images_mini_11/Job_success.png)
  
