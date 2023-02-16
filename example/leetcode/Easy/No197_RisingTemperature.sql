/**
Input: 
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
Output: 
+----+
| id |
+----+
| 2  |
| 4  |
+----+
Explanation: 
In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
In 2015-01-04, the temperature was higher than the previous day (20 -> 30).
*/

select w1.id
from Weather w1
join Weather w2 on datediff(w1.recordDate, w2.recordDate) = 1 and w1.temperature > w2.temperature

select w1.id
from Weather w1
join Weather w2 on subdate(w1.recordDate, interval 1 day) = w2.recordDate and w1.temperature > w2.temperature

select w1.id
from Weather w1
join Weather w2 on adddate(w2.recordDate, interval 1 day) = w1.recordDate and w1.temperature > w2.temperature

SELECT w1.id
FROM Weather AS w1 , Weather AS w2
WHERE w1.Temperature > w2.Temperature AND DATEDIFF(w1.recordDate , w2.recordDate) = 1