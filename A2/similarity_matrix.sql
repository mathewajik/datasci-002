.output 2h.txt
SELECT A.term, SUM(A.count * B.count)
  FROM (SELECT * FROM frequency WHERE docid = '10080_txt_crude') AS A 
    JOIN (SELECT * FROM frequency WHERE docid = '17035_txt_earn') AS B
    ON A.term = B.term
 GROUP BY A.term;
 
 SELECT SUM(A.count * B.count)
  FROM (SELECT * FROM frequency WHERE docid = '10080_txt_crude') AS A 
    JOIN (SELECT * FROM frequency WHERE docid = '17035_txt_earn') AS B
    ON A.term = B.term;
