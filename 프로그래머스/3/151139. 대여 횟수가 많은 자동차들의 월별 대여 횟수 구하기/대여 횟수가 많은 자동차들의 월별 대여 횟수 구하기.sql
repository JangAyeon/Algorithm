-- 코드를 입력하세요
-- 대여 시작일 기준 : 2022년 8월부터 2022년 10월까지 총 대여 횟수가 5회 이상인 자동차들에 대해서

select Month(START_DATE) as MONTH, CAR_ID, count(*) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE (START_DATE BETWEEN '2022-08-01' AND '2022-10-31') and 
CAR_ID in (
    SELECT CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where START_DATE between '2022-08-01' and '2022-10-31'
    group by CAR_ID
    having count(CAR_ID)>=5
) 
group by MONTH, CAR_ID
order by MONTH ASC, CAR_ID DESC



