select count(st.ID)-count(distinct(st.CITY))
from STATION st
