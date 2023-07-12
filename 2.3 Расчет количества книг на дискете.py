# TODO Найдите количество книг, которое можно разместить на дискете
space_disk_in_Mbytes = 1.44
Bytes_in_Kbytes = 1024
Kbytes_in_Mbytes = 1024
space_disk_in_Bytes = (space_disk_in_Mbytes * Kbytes_in_Mbytes) * Bytes_in_Kbytes
pages_in_book = 100
lines_in_book = 50
symbols_in_line = 25
Bytes_for_1_symbol = 4
Books_in_disk = int(space_disk_in_Bytes // (pages_in_book * lines_in_book * symbols_in_line * Bytes_for_1_symbol))

print("Количество книг, помещающихся на дискету:", Books_in_disk)
