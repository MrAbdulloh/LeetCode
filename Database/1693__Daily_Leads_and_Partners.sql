SELECT
    date_id,
    make_name,
    COUNT(DISTINCT lead_id) AS unique_leads,
    COUNT(DISTINCT partner_id) AS unique_partners
FROM
    DailySales
GROUP BY
    date_id,
    make_name
ORDER BY
    date_id,
    make_name;

-- Oracle

SELECT
    TO_CHAR(date_id, 'YYYY-MM-DD') AS DATA_ID,
    UPPER(make_name) AS MAKE_NAME,
    COUNT(DISTINCT lead_id) AS UNIQUE_LEADS,
    COUNT(DISTINCT partner_id) AS UNIQUE_PARTNERS
FROM
    DailySales
GROUP BY
    TO_CHAR(date_id, 'YYYY-MM-DD'),
    UPPER(make_name)
ORDER BY
    TO_CHAR(date_id, 'YYYY-MM-DD'),
    UPPER(make_name);