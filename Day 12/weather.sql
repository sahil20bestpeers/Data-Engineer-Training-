CREATE TABLE weather_forecast2
(
    City String,
    ForecastDateTime DateTime,
    Temperature Float32,
    WeatherDescription String,
    Humidity UInt8,
    WindSpeed Float32,
    IngestionTimestamp DateTime64(6)
)
ENGINE = MergeTree()
ORDER BY (City, ForecastDateTime);



select * from weather_forecast2  



CREATE TABLE icecream_sales
(
    City String,
    SaleDateTime DateTime,
    IceCreamType String,
    UnitsSold UInt32,
    SaleAmount Float32
)
ENGINE = MergeTree()
ORDER BY (City, SaleDateTime);



ALTER TABLE icecream_sales
ADD COLUMN Rent Float32 DEFAULT 0;

INSERT INTO icecream_sales (City, SaleDateTime, IceCreamType, UnitsSold, SaleAmount, Rent) VALUES
('Bhopal', '2025-09-01 12:00:00', 'Vanilla', 20, 100.0, 15.0),
('Bhopal', '2025-09-01 15:00:00', 'Chocolate', 15, 75.0, 14.5),
('Bhopal', '2025-09-01 18:00:00', 'Strawberry', 10, 50.0, 15.2),
('Bhopal', '2025-09-02 12:00:00', 'Vanilla', 22, 110.0, 15.0),
('Bhopal', '2025-09-02 15:00:00', 'Chocolate', 18, 90.0, 14.7),
('Bhopal', '2025-09-02 18:00:00', 'Strawberry', 12, 60.0, 15.1),
('Bhopal', '2025-09-03 12:00:00', 'Vanilla', 25, 125.0, 15.3),
('Bhopal', '2025-09-03 15:00:00', 'Chocolate', 20, 100.0, 14.9),
('Bhopal', '2025-09-03 18:00:00', 'Strawberry', 15, 75.0, 15.0),
('Bhopal', '2025-09-04 12:00:00', 'Vanilla', 30, 150.0, 15.4),
('Bhopal', '2025-09-04 15:00:00', 'Chocolate', 22, 110.0, 15.0),
('Bhopal', '2025-09-04 18:00:00', 'Strawberry', 18, 90.0, 14.8),
('Delhi', '2025-09-01 12:00:00', 'Vanilla', 35, 175.0, 20.0),
('Delhi', '2025-09-01 15:00:00', 'Chocolate', 28, 140.0, 19.5),
('Delhi', '2025-09-01 18:00:00', 'Strawberry', 20, 100.0, 20.2),
('Delhi', '2025-09-02 12:00:00', 'Vanilla', 38, 190.0, 20.1),
('Delhi', '2025-09-02 15:00:00', 'Chocolate', 30, 150.0, 20.3),
('Delhi', '2025-09-02 18:00:00', 'Strawberry', 22, 110.0, 19.8),
('Delhi', '2025-09-03 12:00:00', 'Vanilla', 40, 200.0, 20.5),
('Delhi', '2025-09-03 15:00:00', 'Chocolate', 32, 160.0, 20.0),
('Delhi', '2025-09-03 18:00:00', 'Strawberry', 25, 125.0, 19.9),
('Delhi', '2025-09-04 12:00:00', 'Vanilla', 45, 225.0, 20.4),
('Delhi', '2025-09-04 15:00:00', 'Chocolate', 35, 175.0, 20.2),
('Delhi', '2025-09-04 18:00:00', 'Strawberry', 30, 150.0, 20.1),
('Mumbai', '2025-09-01 12:00:00', 'Vanilla', 28, 140.0, 18.0),
('Mumbai', '2025-09-01 15:00:00', 'Chocolate', 20, 100.0, 18.2),
('Mumbai', '2025-09-01 18:00:00', 'Strawberry', 15, 75.0, 18.5),
('Mumbai', '2025-09-02 12:00:00', 'Vanilla', 30, 150.0, 18.3),
('Mumbai', '2025-09-02 15:00:00', 'Chocolate', 22, 110.0, 18.1),
('Mumbai', '2025-09-02 18:00:00', 'Strawberry', 18, 90.0, 18.0),
('Mumbai', '2025-09-03 12:00:00', 'Vanilla', 32, 160.0, 18.4),
('Mumbai', '2025-09-03 15:00:00', 'Chocolate', 25, 125.0, 18.2),
('Mumbai', '2025-09-03 18:00:00', 'Strawberry', 20, 100.0, 18.3),
('Mumbai', '2025-09-04 12:00:00', 'Vanilla', 35, 175.0, 18.5),
('Mumbai', '2025-09-04 15:00:00', 'Chocolate', 28, 140.0, 18.4),
('Mumbai', '2025-09-04 18:00:00', 'Strawberry', 22, 110.0, 18.3),
('Chennai', '2025-09-01 12:00:00', 'Vanilla', 18, 90.0, 17.0),
('Chennai', '2025-09-01 15:00:00', 'Chocolate', 15, 75.0, 17.2),
('Chennai', '2025-09-01 18:00:00', 'Strawberry', 12, 60.0, 17.3),
('Chennai', '2025-09-02 12:00:00', 'Vanilla', 20, 100.0, 17.5),
('Chennai', '2025-09-02 15:00:00', 'Chocolate', 18, 90.0, 17.1),
('Chennai', '2025-09-02 18:00:00', 'Strawberry', 15, 75.0, 17.4),
('Chennai', '2025-09-03 12:00:00', 'Vanilla', 22, 110.0, 17.5),
('Chennai', '2025-09-03 15:00:00', 'Chocolate', 20, 100.0, 17.6),
('Chennai', '2025-09-03 18:00:00', 'Strawberry', 18, 90.0, 17.7);


select * from icecream_sales






select * from  weather_forecast2

SELECT 
    w.City,
    w.ForecastDateTime,
    w.Temperature,
    w.Humidity,
    w.WeatherDescription,                           
    s.IceCreamType,
    s.UnitsSold,
    s.SaleAmount
FROM weather_forecast2 AS w
JOIN icecream_sales AS s
ON w.City = s.City AND toDate(w.ForecastDateTime) = toDate(s.SaleDateTime) 

                
SELECT 
    w.City,
    corr(w.Temperature, s.SaleAmount) AS correlation
FROM weather_forecast2 AS w
JOIN icecream_sales AS s
ON w.City = s.City
GROUP BY w.City
ORDER BY correlation  DESC;


SELECT 
    w.WeatherDescription,
    avg(s.SaleAmount) AS avg_sales
FROM weather_forecast2 AS w
JOIN icecream_sales AS s   
ON w.City = s.City 
GROUP BY w.WeatherDescription
ORDER BY avg_sales DESC;



SELECT 
    round(w.Humidity, -10) AS HumidityBucket,
    avg(s.SaleAmount) AS avg_sales
FROM weather_forecast2  AS w
JOIN icecream_sales AS s
ON w.City = s.City 
GROUP BY HumidityBucket
ORDER BY HumidityBucket;        


select * from weather_forecast2



--Best Country for Main Location: select most sales and min rent city?
WITH sales_per_city AS (
    SELECT
        s1.City,
        sum(s2.SaleAmount) AS total_sales,
        min(s2.Rent) AS min_rent
    FROM weather_forecast2 AS s1
    JOIN icecream_sales AS s2
        ON s1.City = s2.City
    GROUP BY s1.City
)

SELECT
    City,
    total_sales,
    min_rent
FROM sales_per_city
ORDER BY total_sales DESC, min_rent ASC
LIMIT 1;


SELECT
    City,
    toStartOfMonth(SaleDateTime) AS Month,
    sum(SaleAmount) AS total_revenue,
    any(Rent) AS monthly_rent  -- assuming rent same within month for city
FROM icecream_sales
GROUP BY City, Month


SELECT
    City,
    Month,
    total_revenue,
    monthly_rent
FROM (
    SELECT
        City,
        toStartOfMonth(SaleDateTime) AS Month,  
        sum(SaleAmount) AS total_revenue,
        any(Rent) AS monthly_rent
    FROM icecream_sales
    GROUP BY City, Month
)
WHERE total_revenue >= 3 * monthly_rent
ORDER BY City, Month;


--ROI Analysis: Use each country’s average ice‐cream price; where unavailable, approximate using the
--Big Mac Index to infer purchasing‐power‐adjusted pricing. Factor in fuel usage of 1 liter per 10 km
--and assume no costs beyond diesel for cross‐country transport.





