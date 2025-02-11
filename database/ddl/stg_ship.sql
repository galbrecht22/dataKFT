-- DDL for dataKFT.stg_ship
DROP TABLE IF EXISTS dataKFT.stg_ship;
CREATE TABLE dataKFT.stg_ship (
ship_sid BIGINT,
ship_id_sys INT,
ship_brand VARCHAR(30),
ship_model VARCHAR(30),
ship_length decimal(7,2),
ship_length_dim VARCHAR(10),
ship_year INT,
ship_price decimal(12,2),
ship_price_currency VARCHAR(3),
inserted_ts DATETIME,
last_updated_ts DATETIME
);
