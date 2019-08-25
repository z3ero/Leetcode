# 1. 组合两个表
```[mysql]
select p.firstname, p.lastname, a.city, a.state from person p left join address a on p.personid=a.personid
```
# 2. 第二高的薪水
# 思路: 按照不同的薪资降序排序，然后使用LIMIT子句获得第二高的薪资
```[mysql]
SELECT DISTINCT
    Salary AS SecondHighestSalary
FROM
    Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1
```