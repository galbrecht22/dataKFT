truncate table dataKFT.t03_ship;
insert into dataKFT.t03_ship
select
  ship_sid
, ship_id_sys
, ship_brand
, ship_model
, ship_length
, ship_length_dim
, ship_year
, ship_price
, ship_price_currency
, concat(s.ship_brand, ' ', s.ship_model, ' (', s.ship_year, ')') as ship_display_name
, s.ship_length    * u_ft.conversion_rate  as ship_length_ft
, s.ship_length    * u_in.conversion_rate  as ship_length_in
, s.ship_length    *  u_m.conversion_rate  as ship_length_m
, s.ship_price     *  fx_eur.exchange_rate as ship_price_eur
, s.ship_price     *  fx_huf.exchange_rate as ship_price_huf
, s.ship_price     *  fx_usd.exchange_rate as ship_price_usd
, current_timestamp() as record_ts
from dataKFT.stg_ship s
left join dataKFT.uom_conv u_ft  on s.ship_length_dim = u_ft.from_uom and u_ft.to_uom = 'ft'
left join dataKFT.uom_conv u_in  on s.ship_length_dim = u_in.from_uom and u_in.to_uom = 'in'
left join dataKFT.uom_conv u_m   on s.ship_length_dim =  u_m.from_uom and  u_m.to_uom = 'm'
left join dataKFT.fx_rate fx_eur on s.ship_price_currency = fx_eur.currency_from and fx_eur.currency_to = 'EUR'
left join dataKFT.fx_rate fx_huf on s.ship_price_currency = fx_huf.currency_from and fx_huf.currency_to = 'HUF'
left join dataKFT.fx_rate fx_usd on s.ship_price_currency = fx_usd.currency_from and fx_usd.currency_to = 'USD'
-- order by s.ship_id
;
