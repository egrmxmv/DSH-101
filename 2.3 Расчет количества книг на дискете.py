# TODO Найдите количество книг, которое можно разместить на дискете
space_disk_in_mbytes = 1.44
BYTES_IN_KBYTES = 1024
KBYTES_IN_MBYTES = 1024
space_disk_in_bytes = (space_disk_in_mbytes * KBYTES_IN_MBYTES) * BYTES_IN_KBYTES
pages_in_book = 100
lines_in_book = 50
symbols_in_line = 25
bytes_for_1_symbol = 4
size_of_one_book = pages_in_book * lines_in_book * symbols_in_line * bytes_for_1_symbol
books_in_disk = int(space_disk_in_bytes // size_of_one_book)

print("Количество книг, помещающихся на дискету:", books_in_disk)
