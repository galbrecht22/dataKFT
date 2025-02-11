-- DDL for dataKFT.raw_ship
DROP TABLE IF EXISTS dataKFT.raw_ship;
CREATE TABLE dataKFT.raw_ship (
ship_id INT,
ship_brand VARCHAR(30),
ship_model VARCHAR(30),
ship_length decimal(7,2),
ship_length_dim VARCHAR(10),
ship_year INT,
ship_price decimal(12,2),
ship_price_currency VARCHAR(3),
inserted_ts DATETIME
);
