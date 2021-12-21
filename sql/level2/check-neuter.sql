-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME,
       IF(SEX_UPON_INTAKE LIKE ('%Neutered%')
          OR SEX_UPON_INTAKE LIKE ('%Spayed%'),
          'O', 'X') AS '중성화'
FROM ANIMAL_INS;

-- 코드를 입력하세요
-- SELECT ANIMAL_ID, NAME,
--        CASE WHEN SEX_UPON_INTAKE LIKE ('%Spayed%') OR
--                  SEX_UPON_INTAKE LIKE ('%Neutered%')
--                  THEN 'O' ELSE 'X' END '중성화'
-- FROM ANIMAL_INS;