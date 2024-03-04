# MSDS697-final-project
Final project in the class (MSDS697 -  Distributed Data Systems)

### Python environment
```bash
pip install airflow[google] pymongo pyspark matplotlib seaborn joblib
```

### Airflow setup
```bash
# Set up the environmental variable
# You would put those exports under .bash_profile or .zshrc
export AIRFLOW_HOME={path/to/github/repo}/airflow
export AIRFLOW_CONFIG={path/to/github/repo}/config/airflow.cfg

export AIRFLOW_CONN_GOOGLE_CLOUD_DEFAULT='{
    "conn_type": "google_cloud_platform",
    "extra": {"key_path": "{path/to/project}/credentials.json",
    "scope": "https://www.googleapis.com/auth/cloud-platform",
    "project": "airflow",
    "num_retries": 5}}'

# run in a terminal
### initialize airflow db
airflow db migrate
# or
# airflow db init

### create user
### id: admin, password: admin
airflow users create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin

### start webserver
### endpoint defined in config/airflow.cfg
### default: http://localhost:8080
airflow webserver

# run in another terminal
### run scheduler
airflow scheduler
```

You also need to set-up the parameters that are passed through in dags/example.py
```python
params={
        'gcs_bucket_name' : 'msds697-jobs', # bucket name where your input data is located
        'gcs_input_dir_path' : 'jobs', # path to the file from your bucket
        'output_dir_path' : '/tmp', # directory path for your artifacts (location for outputs)
        'mongodb_host' : 'localhost',
        'mongodb_port' : '27017',
        'mongodb_database' : 'msds697',
        'mongodb_collection' : 'jobs'
    }
```

### Pipeline tasks
![example](images/run_example.png)

### Artifacts

#### [data analysis] plots
- average_salary.png
![alt text](images/average_salary.png) 

- ds_job_postings_in_ffang.png
![alt text](images/ds_job_postings_in_ffang.png)

- proportion_of_relevant_postings.png
![alt text](images/proportion_of_relevant_postings.png) 

- images/top_companies_by_salary.png
![alt text](images/top_companies_by_salary.png)

- types_of_job_postings.png
![alt text](images/types_of_job_postings.png)

#### [model] test score of salary prediction models
- In `rf_model_evaluation.txt` and `slr_model_evaluation.txt`
```
Root Mean Squared Error (RMSE) on test data = 2210.18
```
