--  종류 별로 가장 큰 물고기의 ID, 물고기 이름, 길이
--  10cm 이하일 경우에는 LENGTH 가 NULL
--  물고기의 ID에 대해 오름차순 정렬

select ID, FISH_NAME, LENGTH
from FISH_INFO
left join FISH_NAME_INFO using(FISH_TYPE)
where (FISH_TYPE, LENGTH) in (
    select FISH_TYPE, max(LENGTH) as LENGTH
    from FISH_INFO
    group by FISH_TYPE
)
order by ID ASC