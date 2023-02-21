def print_operation_table(operation, rows_count = 6, cols_count = 6):
    for i in range(1, rows_count + 1):
        for j in range(1, cols_count + 1):
            print(operation(i,j),end = "\t")
        print()

print_operation_table(lambda x,y: x * y)



