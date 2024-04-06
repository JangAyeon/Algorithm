
-- 완료된 중고 거래의 총금액이 70만 원 이상
-- 회원 ID, 닉네임, 총거래금액
-- 총거래금액을 기준으로 오름차순 

SELECT b.USER_ID, b.NICKNAME, sum(a.PRICE) as TOTAL_SALES
from USED_GOODS_BOARD a
left join USED_GOODS_USER b
on a.WRITER_ID = b.USER_ID
where a.status = "DONE"
group by b.USER_ID
having TOTAL_SALES>=700000
order by TOTAL_SALES ASC