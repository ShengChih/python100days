/**
The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.

Write a SQL query to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03". Round Cancellation Rate to two decimal points.

Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input: 
Trips table:
+----+-----------+-----------+---------+---------------------+------------+
| id | client_id | driver_id | city_id | status              | request_at |
+----+-----------+-----------+---------+---------------------+------------+
| 1  | 1         | 10        | 1       | completed           | 2013-10-01 |
| 2  | 2         | 11        | 1       | cancelled_by_driver | 2013-10-01 |
| 3  | 3         | 12        | 6       | completed           | 2013-10-01 |
| 4  | 4         | 13        | 6       | cancelled_by_client | 2013-10-01 |
| 5  | 1         | 10        | 1       | completed           | 2013-10-02 |
| 6  | 2         | 11        | 6       | completed           | 2013-10-02 |
| 7  | 3         | 12        | 6       | completed           | 2013-10-02 |
| 8  | 2         | 12        | 12      | completed           | 2013-10-03 |
| 9  | 3         | 10        | 12      | completed           | 2013-10-03 |
| 10 | 4         | 13        | 12      | cancelled_by_driver | 2013-10-03 |
+----+-----------+-----------+---------+---------------------+------------+
Users table:
+----------+--------+--------+
| users_id | banned | role   |
+----------+--------+--------+
| 1        | No     | client |
| 2        | Yes    | client |
| 3        | No     | client |
| 4        | No     | client |
| 10       | No     | driver |
| 11       | No     | driver |
| 12       | No     | driver |
| 13       | No     | driver |
+----------+--------+--------+
Output: 
+------------+-------------------+
| Day        | Cancellation Rate |
+------------+-------------------+
| 2013-10-01 | 0.33              |
| 2013-10-02 | 0.00              |
| 2013-10-03 | 0.50              |
+------------+-------------------+
Explanation: 
On 2013-10-01:
  - There were 4 requests in total, 2 of which were canceled.
  - However, the request with Id=2 was made by a banned client (User_Id=2), so it is ignored in the calculation.
  - Hence there are 3 unbanned requests in total, 1 of which was canceled.
  - The Cancellation Rate is (1 / 3) = 0.33
On 2013-10-02:
  - There were 3 requests in total, 0 of which were canceled.
  - The request with Id=6 was made by a banned client, so it is ignored.
  - Hence there are 2 unbanned requests in total, 0 of which were canceled.
  - The Cancellation Rate is (0 / 2) = 0.00
On 2013-10-03:
  - There were 3 requests in total, 1 of which was canceled.
  - The request with Id=8 was made by a banned client, so it is ignored.
  - Hence there are 2 unbanned request in total, 1 of which were canceled.
  - The Cancellation Rate is (1 / 2) = 0.50
*/

select
    t.request_at Day,
    round(sum(if(t.status like 'cancelled%', 1, 0)) / count(t.id), 2) "Cancellation Rate"
from Trips t
where t.request_at between '2013-10-01' and '2013-10-03'and t.client_id not in (
    select u.users_id
    from Users u
    where u.banned = 'Yes'
) and t.driver_id not in (
    select u.users_id
    from Users u
    where u.banned = 'Yes'
)
group by t.request_at

select
    t.request_at Day,
    round(sum(t.status != 'completed') / count(t.id), 2) "Cancellation Rate"
from Trips t
left join Users u1 on u1.users_id = t.client_id and u1.banned = 'Yes'
left join Users u2 on u2.users_id = t.driver_id and u2.banned = 'Yes'
where t.request_at between '2013-10-01' and '2013-10-03'and u1.users_id is null and u2.users_id is null
group by t.request_at

select
    t.request_at Day,
    round(sum(t.status != 'completed') / count(t.id), 2) "Cancellation Rate"
from Trips t
join Users u1 on u1.users_id = t.client_id and u1.banned = 'No'
join Users u2 on u2.users_id = t.driver_id and u2.banned = 'No'
where t.request_at between '2013-10-01' and '2013-10-03'
group by t.request_at

/*** Mysql 8+ 加入 CTE，增進 subquery 易讀性及效能 ?，可批量操作可使用原 table index / 暫存表不行使用索引 */
/** CTE 適合 recursive 的資料結構，也有語法的限制 */
with a as (select client_id, driver_id, request_at from Trips where status in ("cancelled_by_driver",           "cancelled_by_client")
    and client_id in (select users_id from Users where banned = "No")
    and driver_id in (select users_id from Users where banned = "No")),
    
b as (select count(client_id) as total_users, request_at from Trips where
      client_id in (select users_id from Users where banned = "No")
      and driver_id in (select users_id from Users where banned = "No")
     group by request_at)
     
select b.request_at as "Day", round((select count(a.client_id) from a where a.request_at = b.request_at)/b.total_users, 2) as "Cancellation Rate"
from b
where b.request_at between "2013-10-01" and "2013-10-03"
group by b.request_at