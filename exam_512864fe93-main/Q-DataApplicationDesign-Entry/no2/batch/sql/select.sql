SELECT
    *
FROM
    ItemSalesMonthlySummary
WHERE
    SaleMonth = DATE_FORMAT(DATE_SUB(CURRENT_DATE, INTERVAL 1 MONTH), '%Y-%m')
