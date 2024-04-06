-- 부서별 평균 연봉 (소수 첫째 자리에서 반올림)
-- 부서 ID, 영문 부서명, 평균 연봉을 조회
-- 부서별 평균 연봉을 기준으로 내림차순 정렬

select b.DEPT_ID, b.DEPT_NAME_EN, ROUND(AVG(a.SAL),0) as AVG_SAL
from HR_EMPLOYEES a
left join HR_DEPARTMENT b using(DEPT_ID)
group by b.DEPT_ID
order by AVG_SAL DESC