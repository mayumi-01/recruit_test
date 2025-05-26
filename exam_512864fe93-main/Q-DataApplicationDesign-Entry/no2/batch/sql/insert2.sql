INSERT INTO
    ItemSalesMonthlySummary
SELECT 
    ItemSales.ItemID,
    DATE_FORMAT(SaleAt, '%Y-%m') AS SaleMonth,
    COUNT(*) * Price AS AmountOfSales
FROM ItemSales INNER JOIN ItemMaster ON ItemSales.ItemID = ItemMaster.ItemID
WHERE SaleAt >= DATE_FORMAT(DATE_SUB(CURRENT_DATE, INTERVAL 1 MONTH), '%Y-%m-01')
  AND SaleAt <  DATE_FORMAT(CURRENT_DATE, '%Y-%m-01')
GROUP BY
    ItemSales.ItemID, SaleMonth, Price
