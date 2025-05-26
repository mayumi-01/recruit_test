DELETE FROM
    ItemSalesMonthlySummary
WHERE
    SaleMonth = DATE_FORMAT(CURRENT_DATE, '%Y-%m')
