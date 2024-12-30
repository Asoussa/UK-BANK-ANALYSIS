create database uk_bank;
use uk_bank;

select * from uk_bank_modified
limit 10;

select * from uk_bank_modified
limit 10;
 
 describe uk_bank_modified;
 
 select distinct(state) from uk_bank_modified;
 
 set sql_safe_updates=0;
 
 
update uk_bank_modified
set City=trim(upper(city));
set sql_safe_updates=1;


UPDATE uk_bank_modified
SET `New Expansion` = REPLACE(`New Expansion`, 'Old', 'Oldd');

select * from uk_bank_modified;


UPDATE uk_bank_modified
SET `Store ID`= COALESCE(`Store ID`, 'no Store ID');

SELECT City, COUNT(*) AS count
FROM uk_bank_modified
GROUP BY City
ORDER BY count DESC;


SELECT 
    COUNT(*) AS total_null_values 
FROM uk_bank_modified
WHERE City IS NULL OR State IS NULL OR Revenue IS NULL OR 'Store ID' IS NULL;


select * from uk_bank_modified;


UPDATE uk_bank_modified  `Sales Region` 
SET  `Sales Region`=REPLACE(`Sales Region`,' ','_');


SELECT City,State,Revenue FROM uk_bank_modified
WHERE Revenue >60000
ORDER BY Revenue DESC;

SELECT City,State, min(`Marketing Spend`) AS MS FROM uk_bank_modified
group by City,State
ORDER BY min(`Marketing Spend`) ;

SELECT State,SUM(PROFIT) AS TOTAL_PROFIT
FROM uk_bank_modified
GROUP BY State
ORDER BY TOTAL_PROFIT DESC;



 SELECT 
    state,
    AVG(`Marketing Spend`) AS avg_marketing_spend,
    AVG(Revenue) AS avg_revenue
FROM uk_bank_modified
group by State;

