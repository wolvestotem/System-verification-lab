-- Q1

SELECT student_name,stu_id FROM Student_registration WHERE course LIKE '%04'

SELECT DISTINCT student_name FROM Student_registration WHERE course LIKE 'EE5%'

SELECT student_name FROM Student_registration GROUP BY student_name HAVING COUNT(status='C' OR NULL) >2

SELECT student_name,course,units FROM Student_registration a, Courses b WHERE a.course=b.course

-- Q2

SELECT name FROM Employee a, Bonus b WHERE a.empID=b.empID