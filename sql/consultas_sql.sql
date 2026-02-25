SELECT 
    Produto,
    Categoria,
    SUM(Quantidade * Preço) AS Total_Vendas
FROM vendas
GROUP BY Produto, Categoria
ORDER BY Total_Vendas DESC;


SELECT 
    Produto,
    SUM(Quantidade * Preço) AS Total_Vendas
FROM vendas
WHERE EXTRACT(MONTH FROM Data) = 6
GROUP BY Produto
ORDER BY Total_Vendas ASC;