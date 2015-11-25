select concat(oc.Name,'(',
              (CASE WHEN oc.Occupation = 'Doctor' THEN 'D'
               WHEN oc.Occupation = 'Professor ' THEN 'P'
               WHEN oc.Occupation = 'Singer' THEN 'S'
               WHEN oc.Occupation = 'Actor' THEN 'A'
               ELSE 3 END)
       ,')')
from Occupations oc
order by oc.Name;


select concat('There are total ', count(*), ' ', LCASE(oc.Occupation), 's.')
from Occupations oc
group by oc.Occupation
order by count(*);