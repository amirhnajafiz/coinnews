from dir_check import dir_init, in_doc_search
from file_maker import generate_file
from part_time import Set


def initialize():
    dir_init()
    temp = Set()
    in_doc_search(temp.get_dir_string())
    return temp


def make_files(total_number, time_setter):
    for i in range(total_number):
        generate_file("./Documents"+time_setter.get_dir_string())
    print(f"{time_setter.get_time_string()}\nNew file added")


number = input(">> ")
setter = initialize()
make_files(int(number), setter)