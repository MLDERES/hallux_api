select *
from band b join band_member bm on bm.band_id = b.band_id join person p on p.person_id
= bm.member_id
where b.band_id = 1005