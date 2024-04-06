-- 각 시간대별로 입양이 몇 건이나 발생
-- 시간대 순으로 정렬
--  09:00부터 19:59까지
SELECT HOUR(DATETIME) as HOUR, count(ANIMAL_ID) as COUNT
from ANIMAL_OUTS
group by HOUR
having HOUR between 9 and 19
order by HOUR