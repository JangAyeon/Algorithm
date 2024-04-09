-- 2022년 1월의 도서 판매 데이터
-- 저자 별, 카테고리 별 매출액(TOTAL_SALES = 판매량 * 판매가)
-- 저자 ID를 오름차순으로, 저자 ID가 같다면 카테고리를 내림차순

select B.author_id, B.author_name, A.category, sum(price*sales) AS TOTAL_SALES
from BOOK A, AUTHOR B,  BOOK_SALES  C
WHERE C.sales_date LIKE "2022-01-%" 
        AND A.AUTHOR_ID = B.AUTHOR_ID
        AND A.BOOK_ID = C.BOOK_ID
        
GROUP BY B.author_id, A.category
ORDER BY B.author_id, A.category DESC