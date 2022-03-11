CREATE DATABASE primary_education;
USE primary_education;

alter table education rename column ISO3 to Country;

update education set IncomeGroup='Lower middle income (LM)' where Country='VNM';

update education set Region='ECA' where Country='TJK';

create table education (ISO3 varchar(5) primary key, Region varchar(5), IncomeGroup varchar(50), 
Total float, ResRural float, ResUrban float, Poorest float, Richest float, DataSource varchar(50), 
TimePeriod integer);

select * from education; 

#1
select Country, Region, IncomeGroup, rank() over(order by Total desc) as Ranking from education;


#2
SELECT Region, round(AVG(Total), 2), round(avg(Poorest), 2), round(avg(Richest),2) 
FROM education GROUP BY Region; 
#or 
SELECT Region, round(AVG(Total), 2), round(avg(Richest)/avg(Poorest),2) 
FROM education GROUP BY Region; 

#3
SELECT IncomeGroup, round(avg(Total),2), round(avg(ResRural), 2), round(avg(ResUrban), 2)
FROM education GROUP BY IncomeGroup order by avg(Total) desc ; 



 

