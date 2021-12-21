-- 코드를 입력하세요
SELECT count(distinct NAME) count
FROM ANIMAL_INS
WHERE NAME IS NOT NULL;