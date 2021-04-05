-- 코드를 입력하세요
SELECT *
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC

-- 코드를 입력하세요
SELECT NAME, DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC

-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = "Sick"

-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != "Aged"

-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID

-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME ASC, DATETIME DESC

-- 코드를 입력하세요
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1

-- 코드를 입력하세요
SELECT DATETIME AS 시간
FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 1

-- 코드를 입력하세요
SELECT COUNT(*) AS count
FROM ANIMAL_INS

-- 코드를 입력하세요
SELECT COUNT(DISTINCT NAME) AS count
FROM ANIMAL_INS

-- 코드를 입력하세요
SELECT ANIMAL_TYPE, COUNT(*) AS count
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Cat' OR ANIMAL_TYPE = 'Dog'
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE

-- 코드를 입력하세요
SELECT NAME, COUNT(*) AS count
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY NAME
HAVING count != 1
ORDER BY NAME

-- 코드를 입력하세요
SELECT HOUR,COUNT(HOUR)
FROM(
    SELECT DATE_FORMAT(DATETIME,'%H') AS HOUR
    FROM ANIMAL_OUTS    
)A
GROUP BY HOUR
HAVING HOUR>=9 AND HOUR<20
ORDER BY HOUR ASC

-- 코드를 입력하세요
SELECT hour(datetime) HOUR, count(*) as COUNT
from animal_outs
group by hour
having hour >= 9 and hour <= 19
order by hour

--------------------------------------------------------------------------------------
-- 코드를 입력하세요
WITH RECURSIVE `HOUR_BASE` AS (
    SELECT 0 AS `HOUR`
    UNION ALL
    SELECT `HOUR`+1 FROM `HOUR_BASE` WHERE `HOUR` < 23
)
SELECT HOUR_BASE.`HOUR`, COUNT(ANIMAL_INFO.`HOUR`)
FROM (
    SELECT HOUR(DATETIME) AS `HOUR`
    FROM `ANIMAL_OUTS`
) AS `ANIMAL_INFO`
NATURAL RIGHT OUTER JOIN `HOUR_BASE`
GROUP BY `HOUR`
ORDER BY `HOUR`

-- 코드를 입력하세요
SELECT
  HOURS.HOUR, 
  IFNULL(AO.CNT, 0) AS COUNT
FROM
  JSON_TABLE(
      "[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]",
      '$[*]' COLUMNS (HOUR INT PATH '$')
  ) HOURS
 LEFT JOIN (
    SELECT 
      HOUR(DATETIME) as HOUR, 
      COUNT(*) as CNT
    FROM ANIMAL_OUTS 
    GROUP BY HOUR(DATETIME)
) AS AO ON AO.HOUR = HOURS.HOUR

-- 코드를 입력하세요
set @a := -1;
SELECT A.HOUR,IFNULL(B.COUNT,0) FROM
(SELECT @a:=@a+1 as HOUR FROM ANIMAL_OUTS) A LEFT JOIN
(SELECT HOUR(DATETIME) as HOUR,COUNT(*) as COUNT FROM ANIMAL_OUTS GROUP BY HOUR(DATETIME) ) B
ON A.HOUR = B.HOUR WHERE A.HOUR<=23

-- 코드를 입력하세요
SELECT DATETIME, count(*)-1
from (SELECT to_number(TO_CHAR ( LEVEL ))-1 as DATETIME FROM DUAL CONNECT BY LEVEL <= 24
      union all
      select to_number(TO_CHAR (DATETIME,'HH24')) from ANIMAL_OUTS) 
group by DATETIME
order by DATETIME

-- 코드를 입력하세요
WITH RECURSIVE HOUR AS(
    SELECT 0 AS h
    UNION ALL
    SELECT h+1 FROM HOUR WHERE h<23
)
SELECT h AS HOUR, COALESCE(COUNT(ANIMAL_ID),0) AS COUNT
FROM HOUR LEFT JOIN ANIMAL_OUTS ON HOUR.h = DATE_FORMAT(DATETIME, '%k')
GROUP BY HOUR.h
--------------------------------------------------------------------------------------

-- 코드를 입력하세요
2. 입양 시각 구하기(2)
위 테이블 데이터를 토대로, 입양 시간대별로 입양이 몇 건이나 발생했는지 조회해야 합니다.

(1) 과 다른 점이라면, 모든 시간대(0시~23시)를 조회해야 합니다.
갑자기 난이도가 상승한 레벨 4의 문제로, 쿼리문에서 로컬 변수를 활용하는 문제입니다.
-- 코드를 입력하세요
set @hour := -1;

select (@hour := @hour + 1) as HOUR, (
    select count(*) 
    from animal_outs
    where hour(datetime) = @hour
) as COUNT
from ANIMAL_OUTS
where @hour < 23

SET 옆에 변수명과 초기값을 설정할 수 있습니다.
@가 붙은 변수는 프로시저가 종료되어도 유지된다고 생각하면 됩니다.
이를 통해 값을 누적하여 0부터 23까지 표현할 수 있습니다.
@hour은 초기값을 -1로 설정합니다. PL/-SQL 문법에서 :=은 비교 연산자 =과 혼동을 피하기 위한의 대입 연산입니다.
SELECT (@hour := @hour +1) 은 @hour의 값에 1씩 증가시키면서 SELECT 문 전체를 실행하게 됩니다.
이 때 처음에 @hour 값이 -1 인데, 이 식에 의해 +1 이 되어 0이 저장됩니다.
HOUR 값이 0부터 시작할 수 있습니다.
WHERE @hour < 23일 때까지, @hour 값이 계속 + 1씩 증가합니다.

-- 코드를 입력하세요
SELECT animal_id
from animal_ins
where name is null
order by animal_id


-- 코드를 입력하세요
SELECT animal_id
from animal_ins
where name is not null
order by animal_id

# ifnull
-- 코드를 입력하세요
SELECT ANIMAL_TYPE, ifnull(name, "No name"), SEX_UPON_INTAKE
from ANIMAL_INS

# join
-- 코드를 입력하세요
SELECT animal_id, name
from animal_outs
where animal_id not in (
    select animal_id
    from animal_ins
)

-- 코드를 입력하세요
SELECT ao.animal_id, ao.name
from animal_outs as ao
    left join animal_ins as ai
    on ao.animal_id = ai.animal_id
where ai.animal_id is null
order by ao.animal_id

-- 코드를 입력하세요
SELECT ai.animal_id, ai.name
from animal_ins as ai
    left join animal_outs as ao
    on ai.animal_id = ao.animal_id
where ai.datetime > ao.datetime
order by ai.datetime

-- 코드를 입력하세요
SELECT ai.name, ai.datetime
from animal_ins as ai
    left join animal_outs as ao
    on ai.animal_id = ao.animal_id
where ao.animal_id is null
order by datetime asc
limit 3

-- 코드를 입력하세요
select ao.animal_id, ao.animal_type, ao.name
from animal_outs as ao
    left join animal_ins as ai
    on ao.animal_id = ai.animal_id
where (ai.sex_upon_intake = "Intact Male" or ai.sex_upon_intake = "Intact Female")
    and (ao.sex_upon_outcome = "Neutered Male" or ao.sex_upon_outcome = "Spayed female")
order by ao.animal_id

-- 코드를 입력하세요
select animal_id, name, sex_upon_intake
from animal_ins
where name in ("Lucy", "Ella", "Pickle", "Rogan", "Sabrina", "Mitty")

-- 코드를 입력하세요
SELECT animal_id, name
from animal_ins
where name like '%el%' and animal_type = 'dog'
order by name

-- 코드를 입력하세요
SELECT animal_id, name, if(sex_upon_intake like "%Neutered%" or sex_upon_intake like "%Spayed%", "O", "X") as 중성화
from animal_ins

-- 코드를 입력하세요
select ai.animal_id, ai.name
from animal_ins as ai
    left join animal_outs as ao
    on ai.animal_id = ao.animal_id
where ao.datetime is not null
order by datediff(ao.datetime, ai.datetime) desc
limit 2

-- 코드를 입력하세요
select ai.animal_id, ai.name
from animal_ins as ai
    inner join animal_outs as ao
    on ai.animal_id = ao.animal_id
order by datediff(ao.datetime, ai.datetime) desc
limit 2


-- 코드를 입력하세요
2
SELECT animal_id, name, date_format(datetime, "%Y-%m-%d") as 날짜
3
from animal_ins
4
order by animal_id


















--------------------------------------------------------------------------------------
[mysql] 쿼리에서 조건문 사용
if 문, case 문, ifnull문
 
IF 문
형식 : if ( 조건문, 참일때 값, 거짓일때 값)

EX)  select member_id, if ( isnull(birthday), '-', birthday ) from member
설명 - 멤버 테이블에서 아이디(member_id) 와 생일을 뽑는데 null 일경우는 - 를 출력, 
      아니면 생일을 출력

Case 문
형식 :  case (조건 또는 값)
          when 값1 then 표시값
          when 값2 then 표시값
        else 표시값
        end

EX)   select case a when '1' then a when '2' then b else c end from table_name
설명 - a 값이 '1'이면 a, '2' 이면 b, 둘다 아닐경우 c 를 출력

ifnull문 ( mysql 에서 사용 )
 형식 : ifnull ( 값1, 값2)

EX ) select ifnull ( price, 0 ) from books
설명 - price 값이 Null 이면 0을, Null 이 아니면 price 값을 출력

isnull문 ( MS-SQL 에서 사용 )
 형식 : ifnull ( 값1, 값2)

EX ) select isnull ( price, 0 ) from books
설명 - price 값이 Null 이면 0을, Null 이 아니면 price 값을 출력

NVL문 ( Oracle 에서 사용 )
 형식 : NVL ( 값1, 값2) 

EX ) select nvl ( price, 0 ) from books
설명 - price 값이 Null 이면 0을, Null 이 아니면 price 값을 출력
--------------------------------------------------------------------------------------