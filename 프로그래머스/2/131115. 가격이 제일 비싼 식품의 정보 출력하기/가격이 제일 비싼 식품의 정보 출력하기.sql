-- 가격이 제일 비싼 식품의 식품 ID, 식품 이름, 식품 코드, 식품분류, 식품 가격을 조회
SELECT PRODUCT_ID, PRODUCT_NAME,PRODUCT_CD,  CATEGORY, PRICE
from FOOD_PRODUCT
where PRICE in (select max(PRICE) 
from FOOD_PRODUCT)