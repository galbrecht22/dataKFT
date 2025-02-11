truncate table dataKFT.t02_purchaser;
insert into dataKFT.t02_purchaser
select
  p.purchaser_sid
, p.purchaser_id_sys
, p.purchaser_short_name
, p.purchaser_name
, p.address_country
, p.address_zip_code
, p.address_city
, p.address_street_name
, p.address_street_suffix
, p.address_house_no
, p.address_topographic_no
, p.address_nuts_code
, current_timestamp() as record_ts
from dataKFT.stg_purchaser p
-- order by p.purchaser_sid
;
