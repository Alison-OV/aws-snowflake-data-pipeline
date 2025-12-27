> Note: The S3 layer is simulated locally to enable cost-free development. 
> The same pipeline can be deployed to AWS with minimal changes.

flowchart LR
    subgraph Data_Source
        A[Sales CSV Files]
    end

    subgraph Data_Lake
        B[S3 Bucket<br/>Raw Zone]
    end

    subgraph ETL_Pipeline
        C[Extract<br/>Python]
        D[Transform<br/>Data Cleaning & Enrichment]
        E[Load<br/>Snowflake Connector]
    end

    subgraph Data_Warehouse
        F[Snowflake<br/>SALES Table]
    end

    subgraph Analytics
        G[BI / SQL Analytics]
    end

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
