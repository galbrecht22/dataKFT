truncate table dataKFT.stg_purchaser;
insert into dataKFT.stg_purchaser
select
  sum(1) over(order by purchaser_id) as purchaser_sid
, purchaser_id as purchaser_id_sys
, purchaser_short_name
, purchaser_name
, address_country
, address_zip_code
, address_city
, address_street_name
, address_street_suffix
, address_house_no
, address_topographic_no
, address_nuts_code
, inserted_ts
, last_updated_ts
from (
      select
        p.purchaser_id
,       p.purchaser_short_name
,       p.purchaser_name
,       p.address_country
,       p.address_zip_code
,       p.address_city
,       p.address_street_name
,       p.address_street_suffix
,       p.address_house_no
,       p.address_topographic_no
,       p.address_nuts_code
,       rank() over (partition by p.purchaser_id order by p.inserted_ts desc)                          as rnk
,       min(p.inserted_ts) over(partition by p.purchaser_id)                                           as inserted_ts
,       IF(min(p.inserted_ts) over (partition by p.purchaser_id) = p.inserted_ts, null, p.inserted_ts) as last_updated_ts
      from dataKFT.raw_purchaser p
) x
where rnk = 1
;
