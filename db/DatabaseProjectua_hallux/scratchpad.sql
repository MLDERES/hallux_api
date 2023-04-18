select *
from band b join band_member bm on bm.band_id = b.band_id join person p on p.person_id
= bm.member_id
where b.band_id = 1005

SELECT band.[Band_Status_Code] AS [band_Band_Status_Code], band.[Band_Name] AS [band_Band_Name], band.[Band_id] AS [band_Band_id], 
band.formation_date AS band_formation_date, band.primary_contact_id AS band_primary_contact_id, band_member_1.[Band_id] AS [band_member_1_Band_id], 
band_member_1.[Member_Id] AS [band_member_1_Member_Id], person_1.street_address AS person_1_street_address, person_1.[Person_Id] AS [person_1_Person_Id], person_1.first_name AS person_1_first_name, 
person_1.last_name AS person_1_last_name, person_1.phone_number AS person_1_phone_number, person_1.email AS person_1_email, person_1.zip_code_ext AS person_1_zip_code_ext, person_1.zip_code AS person_1_zip_code, band_member_1.join_date AS band_member_1_join_date
FROM band LEFT OUTER JOIN band_member AS band_member_1 ON band.[Band_id] = band_member_1.[Band_id] LEFT OUTER JOIN person AS person_1 ON person_1.[Person_Id] = band_member_1.[Member_Id]
WHERE band.[Band_id] = 1037