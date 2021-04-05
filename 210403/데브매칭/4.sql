-- 코드를 입력하세요
select id, name, host_id
from places
where host_id in (
    select host_id
    from (
        select host_id, count(*) as c
        from places
        group by host_id
    ) as p
    where c >= 2
)
order by id

-- 코드를 입력하세요
select id, name, host_id
from places
where host_id in (
    select host_id
    from places
    group by host_id
    having count(*) >= 2
)
order by id