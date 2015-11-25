select t.N, (CASE WHEN t.P IS NULL THEN 'Root'
             WHEN (select count(*) from BST tn where tn.P=t.N)>0 THEN "Inner"
             ELSE "Leaf" END
            )
from BST t;
