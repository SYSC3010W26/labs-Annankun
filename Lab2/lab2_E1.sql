
CREATE TABLE temps(
    tdate DATE,
    ttime TEXT,
    zone TEXT,
    temperature REAL
);

INSERT INTO temps VALUES ('26-Sep', '4:45 PM', 'kitchen', 20.6);
INSERT INTO temps VALUES ('26-Sep', '4:45 PM', 'greenhouse', 26.3);
INSERT INTO temps VALUES ('26-Sep', '4:45 PM', 'garage', 18.6);
INSERT INTO temps VALUES ('27-Sep', '8:03 AM', 'kitchen', 19.5);
INSERT INTO temps VALUES ('27-Sep', '8:03 AM', 'greenhouse', 15.1);
INSERT INTO temps VALUES ('27-Sep', '8:03 AM', 'garage', 18.1);
INSERT INTO temps VALUES ('27-Sep', '2:35 PM', 'kitchen', 21.2);
INSERT INTO temps VALUES ('27-Sep', '2:35 PM', 'greenhouse', 27.1);
INSERT INTO temps VALUES ('27-Sep', '2:35 PM', 'garage', 19.1);

SELECT * FROM temps;