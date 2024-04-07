-- 식품분류가 '과자', '국', '김치', '식용유'인 경우만
-- 식품분류별로 가격이 제일 비싼 식품의 분류
-- 식품 가격을 기준으로 내림차순 정렬

SELECT CATEGORY,PRICE,PRODUCT_NAME
FROM  FOOD_PRODUCT
WHERE (CATEGORY , PRICE ) IN
   (SELECT CATEGORY , max(PRICE) AS PRICE
    FROM FOOD_PRODUCT
    WHERE CATEGORY = '과자' or  CATEGORY = '국' or   CATEGORY = '김치'or CATEGORY = '식용유'  
    GROUP BY CATEGORY)
    ORDER BY PRICE DESC;