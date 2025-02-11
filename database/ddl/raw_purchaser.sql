-- DDL for dataKFT.raw_purchaser
DROP TABLE IF EXISTS dataKFT.raw_purchaser;
CREATE TABLE dataKFT.raw_purchaser (
purchaser_id BIGINT,
purchaser_short_name VARCHAR(50),
purchaser_name VARCHAR(100),
address_country VARCHAR(30),
address_zip_code VARCHAR(30),
address_city VARCHAR(30),
address_street_name VARCHAR(30),
address_street_suffix VARCHAR(30),
address_house_no VARCHAR(30),
address_topographic_no VARCHAR(30),
address_nuts_code VARCHAR(30),
inserted_ts DATETIME
);
