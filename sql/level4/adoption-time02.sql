-- 코드를 입력하세요
SET @v_time = -1;

SELECT (@v_time := @v_time + 1) AS HOUR,
       (SELECT count(*) FROM ANIMAL_OUTS WHERE @v_time = HOUR(DATETIME)) AS COUNT
FROM ANIMAL_OUTS
WHERE @v_time < 23;