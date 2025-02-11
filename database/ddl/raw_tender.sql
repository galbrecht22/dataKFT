-- DDL for dataKFT.raw_tender
DROP TABLE IF EXISTS dataKFT.raw_tender;
CREATE TABLE dataKFT.raw_tender (
tender_id VARCHAR(30),
tender_dt VARCHAR(30),
tender_title VARCHAR(100),
tender_category VARCHAR(30),
tender_sid VARCHAR(30),
tender_eid VARCHAR(30),
tender_place VARCHAR(30),
purchaser_sid BIGINT,
awarded_value DECIMAL(12,2),
awarded_currency VARCHAR(3),
awarded_value_eur DECIMAL(9,2),
inserted_ts DATETIME
);
