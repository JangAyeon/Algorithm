-- 코드를 입력하세요
SELECT Floor(PRICE/10000)*10000 as PRICE_GROUP, count(*) as PRODUCTS
from PRODUCT
group by PRICE_GROUP
order by PRICE_GROUP ASC