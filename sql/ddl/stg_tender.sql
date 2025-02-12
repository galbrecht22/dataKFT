-- DDL for dataKFT.stg_tender
DROP TABLE IF EXISTS dataKFT.stg_tender;
CREATE TABLE dataKFT.stg_tender (
tender_sid BIGINT,
tender_id_sys VARCHAR(30),
tender_dt DATETIME,
tender_title VARCHAR(100),
tender_category VARCHAR(30),
tender_sid_sys VARCHAR(30),
tender_eid_sys VARCHAR(30),
tender_place VARCHAR(30),
purchaser_sid_sys BIGINT,
awarded_value DECIMAL(12,2),
awarded_currency VARCHAR(3),
awarded_value_eur DECIMAL(9,2),
inserted_ts DATETIME,
last_updated_ts DATETIME
);
