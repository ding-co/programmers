-- 코드를 입력하세요
SELECT t2.ANIMAL_ID, t2.NAME
FROM ANIMAL_INS t1 RIGHT OUTER JOIN ANIMAL_OUTS t2 on t1.ANIMAL_ID = t2.ANIMAL_ID
WHERE t1.ANIMAL_ID IS NULL;