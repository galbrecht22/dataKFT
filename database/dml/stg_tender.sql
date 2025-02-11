truncate table dataKFT.stg_tender;
insert into dataKFT.stg_tender
select
  sum(1) over(order by tender_id) as tender_sid
, tender_id as tender_id_sys
, cast(tender_dt as datetime) as tender_dt
, tender_title
, tender_category
, tender_sid as tender_sid_sys
, tender_eid as tender_eid_sys
, tender_place
, purchaser_sid as purchaser_sid_sys
, awarded_value
, awarded_currency
, awarded_value_eur
, inserted_ts
, last_updated_ts
from (
      select
        t.tender_id
,       t.tender_dt
,       t.tender_title
,       t.tender_category
,       t.tender_sid
,       t.tender_eid
,       t.tender_place
,       t.purchaser_sid
,       t.awarded_value
,       t.awarded_currency
,       t.awarded_value_eur
,       rank() over (partition by t.tender_id order by t.inserted_ts desc)                          as rnk
,       min(t.inserted_ts) over(partition by t.tender_id)                                           as inserted_ts
,       IF(min(t.inserted_ts) over (partition by t.tender_id) = t.inserted_ts, null, t.inserted_ts) as last_updated_ts
      from dataKFT.raw_tender t
) x
where rnk = 1
;
