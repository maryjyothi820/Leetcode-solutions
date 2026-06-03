3421.Find_students_who_improved.py
SELECT
    a.student_id,
    a.subject,
    a.score AS first_score,
    b.score AS latest_score
FROM Scores a
JOIN Scores b
ON a.student_id = b.student_id
AND a.subject = b.subject
AND a.exam_date = (
    SELECT MIN(exam_date)
    FROM Scores
    WHERE student_id = a.student_id
    AND subject = a.subject
)
AND b.exam_date = (
    SELECT MAX(exam_date)
    FROM Scores
    WHERE student_id = b.student_id
    AND subject = b.subject
)
WHERE b.score > a.score
AND a.exam_date <> b.exam_date
ORDER BY a.student_id, a.subject;