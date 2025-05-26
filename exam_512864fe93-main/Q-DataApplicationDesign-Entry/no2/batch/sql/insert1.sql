INSERT INTO
    ItemSalesMonthlySummary
SELECT 
    ItemSales.ItemID,
    DATE_FORMAT(SaleAt, '%Y-%m') AS SaleMonth,
    COUNT(*) * Price AS AmountOfSales
FROM ItemSales INNER JOIN ItemMaster ON ItemSales.ItemID = ItemMaster.ItemID
WHERE SaleAt >= DATE_SUB(CURRENT_DATE, INTERVAL 1 MONTH)
  AND SaleAt <  CURRENT_DATE
GROUP BY
    ItemSales.ItemID, SaleMonth, Price
