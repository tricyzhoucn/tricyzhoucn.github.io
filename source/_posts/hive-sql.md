---
title: hive-sql
date: 2022-12-05 15:01:21
tags: sql
---

> Hive sql 汇总

<!-- more -->

#### 连续7天登陆

```sql
select user_id, count(1) as cn 
from (
    select user_id, login_date, row_number() over (partition by user_id order by login_date) as rn 
    from (
        select user_id, login_date 
        from db.t 
        group by user_id, login_date
    )
) group by user_id, date_sub(login_date, rn)
where cn>=7
```

#### 时间处理

```sql
date_sub(from_unixtime(unix_timestamp(cast(imp_date as string), 'yyyyMMdd')),1)
```

#### 相邻间隔

```sql
select t1.id, 
t1.ctime, 
t2.id, 
t2.ctime,
timediff(t2.ctime,t1.ctime) as diff -- abs(datediff())
from t t1 inner join t t2 
on t1.id + 1 = t2.id
```

