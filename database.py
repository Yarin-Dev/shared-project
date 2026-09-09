import Screen
import csv

from csv import writer


def insert_into_db(board, solider_position, grass_rect_list):
    new_row = [board, solider_position, grass_rect_list]
    with open('data.csv', 'a', newline='') as f:
        writer_obj = writer(f)
        writer_obj.writerow(new_row)
