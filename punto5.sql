SELECT a.EmployeeID, a.FirstName, a.LastName, b.OrderID, d.PrcuctName, e.CategoryName
FROM Employees a
JOIN Orders b ON a.EmployeeID = b.EmployeeID
JOIN OrderDetails c ON b.OrderID = c.OrderID
JOIN Products d ON c.ProductID = d.ProductID
JOIN Categories e ON d.CategoryID = e.CategoryID
WHERE e.CategoryName = 'Beverages';