-- 코드를 입력하세요
SELECT t1.NAME, t1.DATETIME
FROM ANIMAL_INS t1 LEFT OUTER JOIN ANIMAL_OUTS t2 ON t1.ANIMAL_ID = t2.ANIMAL_ID
WHERE t2.ANIMAL_ID IS NULL
ORDER BY t1.DATETIME ASC
LIMIT 3;