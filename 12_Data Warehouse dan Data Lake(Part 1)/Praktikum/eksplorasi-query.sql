SELECT AVG(mentor_satisfaction_score) AS avg_mentor_satisfaction
FROM dataeksplorasi.survei;

SELECT AVG(cs_satisfaction_score) AS avg_cs_satisfaction
FROM dataeksplorasi.survei;

SELECT AVG(mentor_satisfaction_score) AS avg_mentor_satisfaction_course_a
FROM dataeksplorasi.survei
WHERE course_name = 'Course A';

SELECT MIN(learning_satisfaction_score) AS min_learning_satisfaction_course_c
FROM dataeksplorasi.survei
WHERE course_name = 'Course C';

SELECT MAX(cs_satisfaction_score) AS max_cs_satisfaction_course_b
FROM dataeksplorasi.survei
WHERE course_name = 'Course B';

SELECT course_name, AVG(mentor_satisfaction_score) AS avg_mentor_satisfaction
FROM dataeksplorasi.survei
GROUP BY course_name
ORDER BY avg_mentor_satisfaction DESC
LIMIT 1;

SELECT course_name, AVG(learning_satisfaction_score) AS avg_learning_satisfaction
FROM dataeksplorasi.survei
GROUP BY course_name
ORDER BY avg_learning_satisfaction DESC
LIMIT 1;