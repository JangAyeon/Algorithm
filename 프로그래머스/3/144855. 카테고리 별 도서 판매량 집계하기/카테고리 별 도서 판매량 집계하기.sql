-- 2022년 1월의 카테고리 별 도서 판매량을 합산
-- 카테고리(CATEGORY), 총 판매량(TOTAL_SALES) 리스트
-- 카테고리명을 기준으로 오름차순
SELECT b.CATEGORY, sum(sales) as TOTAL_SALES 
from BOOK_SALES a 
left join BOOK b using(BOOK_ID)
where a.SALES_DATE like "2022-01%"
group by b.category
order by CATEGORY ASC