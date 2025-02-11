truncate table dataKFT.t01_tender;
insert into dataKFT.t01_tender
select
  t.tender_sid
, t.tender_id_sys
, t.tender_dt
, t.tender_title
, t.tender_category
, t.tender_sid_sys
, t.tender_eid_sys
, t.tender_place
, p.purchaser_sid
, t.awarded_value
, t.awarded_currency
, t.awarded_value_eur
, current_timestamp() as record_ts
from dataKFT.stg_tender t
left join dataKFT.stg_purchaser p on t.purchaser_sid_sys = p.purchaser_id_sys
-- order by t.tender_sid
;
