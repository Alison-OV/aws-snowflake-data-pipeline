

<img width="7806" height="760" alt="Untitled diagram-2025-12-27-170623" src="https://github.com/user-attachments/assets/4e55b2bd-9a5d-4c65-a6e0-f67bcbe2e5aa" />



### Architecture Overview

This project implements an end-to-end data pipeline following modern data engineering best practices. 
Raw CSV files are stored in an Amazon S3 bucket (simulated locally for development). 
Python scripts handle data extraction, transformation, and loading into Snowflake, 
where the data is optimized for analytical queries and reporting.


> Note: The S3 layer is simulated locally to enable cost-free development. 
> The same pipeline can be deployed to AWS with minimal changes.
