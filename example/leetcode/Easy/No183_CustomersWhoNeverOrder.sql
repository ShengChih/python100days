/**
Example 1:

Input: 
Customers table:
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Orders table:
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Output: 
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
*/

select c.name Customers
from Customers c
left join Orders o on o.customerId = c.id
where o.id is null
group by c.id

select c.name Customers
from Customers c
where c.id not in (
    select o.customerId
    from Orders o
)