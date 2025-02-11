-- DDL for dataKFT.t01_tender
DROP TABLE IF EXISTS dataKFT.t01_tender;
CREATE TABLE dataKFT.t01_tender (
tender_sid BIGINT,
tender_id_sys VARCHAR(30),
tender_dt VARCHAR(30),
tender_title VARCHAR(100),
tender_category VARCHAR(30),
tender_sid_sys VARCHAR(30),
tender_eid_sys VARCHAR(30),
tender_place VARCHAR(30),
purchaser_sid BIGINT,
awarded_value DECIMAL(12,2),
awarded_currency VARCHAR(3),
awarded_value_eur DECIMAL(9,2),
record_ts DATETIME
);
