/**
Example 1:

Input: 
Person table:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Output: 
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
Explanation: john@example.com is repeated two times. We keep the row with the smallest Id = 1.
*/

delete p1 from Person p1, Person p2
where p1.email = p2.email and p1.id > p2.id ;

DELETE FROM Person WHERE Id NOT IN 
(
    select *
    from (
        SELECT MIN(Id) FROM Person GROUP BY Email
    ) p
)