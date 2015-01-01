.output 1a.txt
select count(*) from frequency where docid = '10398_txt_earn';
.output 1b.txt
select count(*) from frequency where docid = '10398_txt_earn' and count = 1;
.output 1c.txt
select count(*)
from (
    select term from frequency where docid = '10398_txt_earn' and count = 1
    union
    select term from frequency where docid = '925_txt_trade' and count = 1
);
.output 1d.txt
select count(distinct docid) from frequency where term = 'parliament' and count > 0;
.output 1e.txt
select count(docid) from (select docid AS docid, sum(count) AS docs from frequency group by docid) where docs > 300;
.output two_words.txt
select count(*) from
(select distinct docid from frequency where term = 'transactions') a,
(select distinct docid from frequency where term = 'world') b
where a.docid = b.docid;

