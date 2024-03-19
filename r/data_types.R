

# ############################# string data-type

sold_months <- paste(c(7, 8, 9, 10, 11, 12), collapse = ", ")

query <- sprintf("SELECT * FROM table_name WHERE sold_month IN (%s)", sold_months)


