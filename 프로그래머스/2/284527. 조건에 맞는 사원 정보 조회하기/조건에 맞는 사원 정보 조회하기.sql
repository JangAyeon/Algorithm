-- 코드를 작성해주세요
## 평가 점수, 사번, 성명, 직책, 이메일
## 상,하반기 점수의 합

select sum(g.SCORE) as SCORE, e.EMP_NO,e.EMP_NAME, e.POSITION, e.EMAIL
from HR_EMPLOYEES e
join HR_GRADE g
on e.EMP_NO = g.EMP_NO
group by e.EMP_NO
order by SCORE DESC
limit 1
