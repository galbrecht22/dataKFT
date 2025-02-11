truncate table dataKFT.stg_ship;
insert into dataKFT.stg_ship
select
  sum(1) over(order by ship_id) as ship_sid
, ship_id as ship_id_sys
, ship_brand
, ship_model
, ship_length
, ship_length_dim
, ship_year
, ship_price
, ship_price_currency
, inserted_ts
, last_updated_ts
from (
      select
        s.ship_id
      , s.ship_brand
      , s.ship_model
      , s.ship_length
      , s.ship_length_dim
      , s.ship_year
      , s.ship_price
      , s.ship_price_currency
      , rank() over (partition by s.ship_id order by s.inserted_ts desc)                          as rnk
      , min(s.inserted_ts) over(partition by s.ship_id)                                           as inserted_ts
      , IF(min(s.inserted_ts) over (partition by s.ship_id) = s.inserted_ts, null, s.inserted_ts) as last_updated_ts
      from dataKFT.raw_ship s
) x
where rnk = 1
;
