-- DDL for dataKFT.t03_ship
DROP TABLE IF EXISTS dataKFT.t03_ship;
CREATE TABLE dataKFT.t03_ship (
ship_sid BIGINT,
ship_id_sys INT,
ship_brand VARCHAR(30),
ship_model VARCHAR(30),
ship_length decimal(7,2),
ship_length_dim VARCHAR(10),
ship_year INT,
ship_price decimal(12,2),
ship_price_currency VARCHAR(3),
ship_display_name VARCHAR(100),
ship_length_ft decimal(7,2),
ship_length_in decimal(7,2),
ship_length_m decimal(7,2),
ship_price_eur decimal(12,2),
ship_price_huf decimal(12,2),
ship_price_usd decimal(12,2),
record_ts DATETIME
);
