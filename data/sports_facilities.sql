-- Drop table

-- DROP TABLE public.sports_facilities;

CREATE TABLE public.sports_facilities
(
    id            serial4 NOT NULL,
    ida_code      int4 NULL,
    facility_name varchar NULL,
    province      varchar NULL,
    town          varchar NULL,
    street_name   varchar NULL,
    postal_code   int4 NULL,
    sport_area    varchar NULL
);

COPY public.sports_facilities(ida_code, facility_name, province, town, street_name, postal_code, sport_area)
    FROM '/tmp/sports_facilities_census.csv' -- Path to CSV file, adjust it to your file system
    DELIMITER ','
    ENCODING 'iso-8859-1'
    CSV HEADER
;
