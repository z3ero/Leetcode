# 1. 组合两个表
```[mysql]
select p.firstname, p.lastname, a.city, a.state from person p left join address a on p.personid=a.personid
```
# 2. 第二高的薪水
# 思路: 按照不同的薪资降序排序，然后使用LIMIT子句获得第二高的薪资
```[mysql]
SELECT
    Salary AS SecondHighestSalary
FROM
    Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1
```
# 当表中只有一项纪录时，会出现异常，使用IFNULL解决异常
# IFNULL() 如果不是第一个参数不为 NULL, 返回第一个参数；否则返回第二个参数
```[mysql]
select
    ifnull(
    (select distinct salary from employee order by salary desc limit 1 offset 1),NULL)
    as SecondHighestSalary
```
