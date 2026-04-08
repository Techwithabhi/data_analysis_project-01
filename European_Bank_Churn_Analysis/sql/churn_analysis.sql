CREATE DATABASE project;

USE project;

CREATE TABLE final_data (
    CustomerID INT,
    CreditScore INT,
    Geography VARCHAR(50),
    Gender INT,
    Age INT,
    Tenure INT,
    Balance FLOAT,
    NumOfProducts INT,
    HasCrCard INT,
    IsActiveMember INT,
    EstimatedSalary FLOAT,
    Exited INT,
    AgeGroup VARCHAR(20),
    CreditBand VARCHAR(20),
    BalanceGroup VARCHAR(20),
    TenureGroup VARCHAR(20)
);

-- Load CSV into table
-- (Done using MySQL import wizard / LOAD DATA INFILE)


-- Overview the dataset
SELECT * FROM final_data;


-- Size of the dataset
SELECT COUNT(*) AS total_customers
FROM final_data;


-- Overall Churn Rate
SELECT 
    ROUND(AVG(Exited) * 100, 2) AS churn_rate
FROM final_data;


-- Churn by Geography
SELECT 
    Geography,
    ROUND(AVG(Exited) * 100, 2) AS churn_rate
FROM final_data
GROUP BY Geography
ORDER BY churn_rate DESC;


-- Churn by Age Group
SELECT 
    AgeGroup,
    ROUND(AVG(Exited) * 100, 2) AS churn_rate
FROM final_data
GROUP BY AgeGroup
ORDER BY churn_rate DESC;


-- Engagement Impact
SELECT 
    IsActiveMember,
    ROUND(AVG(Exited) * 100, 2) AS churn_rate
FROM final_data
GROUP BY IsActiveMember;


-- High-Value Customers
SELECT 
    ROUND(AVG(Exited) * 100, 2) AS high_value_churn
FROM final_data
WHERE Balance > 100000;


