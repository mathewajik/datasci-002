.output 2i.txt

CREATE VIEW frequency_V AS 
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count;

SELECT A.docid, SUM(A.count * B.count * C.count)
  FROM (SELECT * FROM frequency_V WHERE term = 'washington') AS A 
    JOIN (SELECT * FROM frequency_V WHERE TERM = 'taxes') AS B
    ON A.docid = B.docid    
    JOIN (SELECT * FROM frequency_V WHERE TERM = 'treasury') AS C
    ON B.docid = C.docid
 GROUP BY A.docid
 ORDER BY 2 desc;
 
 SELECT A.docid, SUM(A.count * B.count)
  FROM (SELECT * FROM frequency_V WHERE term = 'washington') AS A 
    JOIN (SELECT * FROM frequency_V WHERE TERM = 'taxes') AS B
    ON A.docid = B.docid        
 GROUP BY A.docid
 ORDER BY 2 desc;
 
 SELECT A.docid, A.count , B.count , C.count
  FROM (SELECT * FROM frequency_V WHERE term = 'washington') AS A 
    JOIN (SELECT * FROM frequency_V WHERE TERM = 'taxes') AS B
    ON A.docid = B.docid
    JOIN (SELECT * FROM frequency_V WHERE TERM = 'treasury') AS C
    ON B.docid = C.docid
 ORDER BY 1 desc;
 
 SELECT B.docid, SUM(A.count * B.count)
  FROM (SELECT * FROM frequency_V WHERE docid = 'q') AS A 
    JOIN frequency_V B ON A.term = B.term
    GROUP BY B.docid
    ORDER BY 2 ASC;
    
-- That's it!  Use the query like  document, and then compute the similarity of the query with every document, and find the max score.
