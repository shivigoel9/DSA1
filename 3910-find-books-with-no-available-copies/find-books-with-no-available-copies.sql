select l.book_id, l.title, l.author, l.genre, l.publication_year, count(*) as current_borrowers 
from library_books l
join borrowing_records b on l.book_id = b.book_id
where b.return_date IS NULL
group by l.book_id, l.title, l.author, l.genre, l.publication_year, l.total_copies
having count(*) = l.total_copies
order by current_borrowers DESC, l.title ASC;