select * from emp;
#emp : 사원번호,이름,업무,관리자번호,입사일자,급여,커미션,부서번호
select * from dept;
#dept : 부서번호,부서명,도시명
select * from salgrade;
#salgrade : 등급,최저급여,최고급여

# 1. EMP TABLE 에서 이름, 급여, 커미션 금액, 총액 (SAL + COMM) 을 구하여 총액이 많은 순서로 출력하라. 
# 단 커미션이 NULL인 사람은 제외한다.
select ename as 이름,
       sal as 급여,
       comm as 커미션,
       (sal + comm) as 총액
 from emp
where comm is not null
order by 총액 desc;

select ename as 이름,
       sal as 급여,
       comm as 커미션,
       (sal + ifnull(comm,0)) as 총액
 from emp
order by 총액 desc;

# 2. EMP와 DEPT TABLE 을 inner JOIN 하여 부서번호, 부서명, 이름, 급여를 출력하라.
select count(*) from emp; #14건
select count(*) from dept; #4

select ename,sal,d.deptno,d.dname
  from emp e, dept d
 where e.deptno = d.deptno;

#Ansi SQL (표준 SQL)

# 3. EMP 테이블에서 사원번호가 7521인 사원과 업무가 같고, 급여가 7934인 사원보다 많은 사원의
# 사원번호, 이름, 담당업무, 입사일자, 급여를 출력하여라.
# where 단일행 subquery
select job from emp where empno = 7521; #salesman
select sal from emp where empno = 7934; #1300

select empno,ename,job,hiredate,sal
  from emp
 where job = (select job from emp where empno = 7521)
   and sal > (select sal from emp where empno = 7934);

# 4. EMP 테이블에서 평균급여보다 적은 급여를 받는 사원의 사원번호, 이름, 담당업무, 급여, 부서번호를 출력하라.
# 단일행 subquery
select avg(sal) from emp;
select empno,ename,job,sal,deptno
  from emp
where sal < (select avg(sal) from emp);

# 5. EMP TABLE 에 있는 EMPNO와 MGR을 이용하여 서로의 관계를 다음과 같이 출력하라.
# SMITH의 매니저는 FORD이다.
# || (oracle) , concat( mysql )
# 5.1 (self join) 같은 emp 테이블 2개를 조인합니다.
select * from emp;
select concat(e.ename,'의 매니저는',m.ename,'이다' ) as 사원과매니저
  from emp e, emp m
 where e.mgr = m.empno;

# 5.2 inline view
select concat(e.ename,'의 매니저는',m.ename,'이다' ) as 사원과매니저
  from emp e, (select * from emp) m
where e.mgr = m.empno;

#6. ALLEN의 직무와 같은 사람의 이름, 부서명, 급여, 직무를 출력하라.
# where 단일행 subquery
select job from emp where ename = 'ALLEN'; #salesman
select ename,d.dname,sal,job
  from emp e, dept d
 where e.deptno = d.deptno
   and job = (select job from emp where ename = 'ALLEN');

#7. EMP 테이블에서 SALES 부서 사원의 이름,업무,부서번호를 출력하는 SELECT문을 작성하시오.
#7.1 Nested Query
select ename,job,deptno
 from emp
where deptno = (select deptno from dept where dname='SALES');
#7.2 Inline View
select e.ename,e.job,d.deptno, d.dname
  from emp e,(select deptno,dname from dept where dname='SALES') d
 where e.deptno = d.deptno;

#8. EMP 테이블에서 이름에 “T”가 있는 사원이 근무하는 부서에서 근무하는 모든 사원에 대해
# 사원 번호,이름,급여를 출력하는 SELECT문을 작성하시오.
#단 사원번호 순으로 출력하여라.
# where in 다중행 subquery
select deptno from emp where ename like '%T%'; #20,30
select empno,ename,sal,deptno
  from emp
where deptno in (select deptno from emp where ename like '%T%')
order by empno;

# 9. 전체 사원의 평균 임금보다 많은 사원의 사원번호, 이름, 부서명, 입사일, 지역, 급여를 출력하라.
# where 단일행 subquery
select avg(sal) from emp;

select empno,ename,d.dname,hiredate,d.loc,sal
  from emp e, dept d
 where e.deptno = d.deptno
  and sal > (select avg(sal) from emp);

# 10. EMP 테이블에서 관리자중에서 부하직원을 2명이상 관리하는 관리자의 이름을 출력하세요.
select mgr,count(*) as emp_cnt from emp group by mgr having emp_cnt >= 2;
select mgr from emp group by mgr having count(*) >= 2;

# 10.1 Nested Query (where 절에 subquery)
select empno,ename
 from emp
where empno in (select mgr from emp group by mgr having count(*) >= 2);

# 10.2 Inline View (from 절에 subquery)
select empno,ename
  from emp,(select mgr from emp group by mgr having count(*) >= 2) b
 where empno in (b.mgr);

select empno,ename
  from emp,(select mgr,count(*) as emp_cnt from emp group by mgr) b
 where empno in (b.mgr)
   and b.emp_cnt >= 2;

# 11.EMP 테이블에서 CHICAGO에서 근무하는 사원과 같은 업무를 하는 사원의 이름,업무를 출력하는 SELECT문을 작성하시오.
select * from emp where deptno = 30;
select * from dept;
select * from emp where job in ('SALESMAN','MANAGER','CLERK');

# 11.1.1 Nested Query ( where 절에 in 구문에  subquery 대입 )
select ename,job
  from emp
 where job in (select job from emp where deptno = (select deptno from dept where loc='CHICAGO'));

# 11.2 Inline View
select distinct ename,e.job, d.loc
  from emp e,(select a.deptno,a.loc,b.job from dept a,emp b where a.deptno = b.deptno and loc='CHICAGO') d
  where e.job = d.job;

# 12.EMP 테이블에서 업무가 JONES와 같거나 월급이 FORD이상인 사원의 이름,업무,부서번호,급여를 출력하는 SELECT문을 작성하시오.
# 단 업무별, 월급이 많은 순으로 출력하여라.
# where 단일행 subquery
select job from emp where ename = 'JONES'; #manager
select sal from emp where ename = 'FORD'; #3000

select ename,job,deptno,sal
  from emp
 where job = (select job from emp where ename = 'JONES')
   or sal >= (select sal from emp where ename = 'FORD')
 order by job, sal desc;

# 13. EMP 테이블에서 업무별로 최소 급여를 받는 사원의 사원번호, 이름, 업무, 입사일자, 급여, 부서번호를 출력하여라.
select job, min(sal) from emp group by job;
select empno,min(sal) from emp group by job having min(sal);
select empno from emp group by job having min(sal);
select * from emp where job = 'SALESMAN';

# inline view
select empno,ename,e.job,hiredate,sal,deptno
  from emp e, (select job, min(sal) as min_sal from emp group by job) b
 where e.job = b.job
   and e.sal = b.min_sal;

# select empno,ename,job,hiredate,sal,deptno
#   from emp
#  where empno in (select empno from emp group by job having min(sal));

# 14. emp와 dept 테이블에서 업무가 manager인 사원의 이름, 업무, 부서명, 근무지를 출력하여라.
# Inline View 를 사용하자
select ename,job,d.dname,d.loc
  from (select * from emp where job='MANAGER') e, dept d
 where e.deptno = d.deptno;

# 15. EMP 테이블에서 30번 부서원 중 최저급여를 받는 사원을 제외한 나머지 사원들의 모든 정보를 출력하는 SELECT문을 작성하시오.
select * from emp where deptno = 30 order by sal asc;
select deptno, min(sal) from emp group by deptno;
# Multi Column Subquery
select *
  from emp
where not ((deptno,sal) in (select deptno, min(sal) from emp group by deptno))
  and deptno = 30;

# 16. EMP 테이블에서 말단 사원의 사원번호,이름,업무,부서번호를 출력하는 SELECT문을 작성하시오.(말단사원: 다른 사원을 관리하지 않는 사원)
# - ORACLE : NVL(VALUE1, VALUE2)
# - MSSQL  : ISNULL(VALUE1, VALUE2)
# - MYSQL  : IFNULL(VALUE1, VALUE2)
select ename,mgr from emp;
select distinct mgr from emp;
SELECT DISTINCT(IFNULL(mgr,0)) FROM emp;

select empno,job,deptno
  from emp
where empno not in (SELECT DISTINCT(IFNULL(mgr,0)) FROM emp);

#결과가 출력되지 않는다 in 구문은 null 값을 비교하지 못하기 때문이다.
select empno,job,deptno
  from emp
where empno not in (select distinct mgr from emp);

# 17. EMP 테이블에서 사원번호, 이름, 업무, 급여, 급여의 등급을 출력하되 3등급 이상인 사원의 정보만을 출력하세요.
# (emp와 salgrade 테이블을 이용);
select * from salgrade;
select empno,job,sal,s.grade
from emp e, salgrade s
where (e.sal >= s.LOSAL) and (e.sal <= s.HISAL)
  and s.GRADE >= 3;

# 18. 부서번호, 부서에 속한 직원수, 부서명, 도시명을 출력하세요.
# 직원수가 5명이상인 부서만 출력하세요. ( inline view )
select deptno,count(*) emp_cnt
  from emp
group by deptno
 having emp_cnt >= 5;

select e.emp_cnt, d.dname, d.loc
  from (select deptno,count(*) emp_cnt
        from emp
        group by deptno
        having emp_cnt >= 5) e, dept d
where e.deptno = d.deptno;


# 20. EMP 테이블에서 적어도 한 명 이상으로부터 보고를 받을 수 있는 사원의 업무,이름,사원번호,부서번호를 출력하시오.
# (즉 관리자를 출력하세요)
select empno,job,deptno
  from emp
where empno in (SELECT DISTINCT(IFNULL(mgr,0)) FROM emp);

