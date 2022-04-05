"""Print out all the melons in our inventory."""

from melons import melon_info

def print_melons(melon_info):
    for melon_name in melon_info:
        print(f"\n{melon_name.upper()}")
        for key, value in melon_info[melon_name].items():
            print(f"{key}: {value}")

print_melons(melon_info)        