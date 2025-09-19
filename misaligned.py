def color_index_to_pair_number(major_color_index, minor_color_index):
    return major_color_index * 5 + minor_color_index + 1

def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i in range(len(major_colors)):
        for j in range(len(minor_colors)):
            print(f"{color_index_to_pair_number(i, j)} | {major_colors[i]} | {minor_colors[j]}")
    
    return len(major_colors) * len(minor_colors)


def test_print_color_map():
    print("\nPrint color map test\n")
    result = print_color_map()
    assert result == 25
    assert color_index_to_pair_number(0, 0) == 1
    assert color_index_to_pair_number(0, 1) == 2
    assert color_index_to_pair_number(1, 0) == 6
    assert color_index_to_pair_number(4, 4) == 25


if __name__ == "__main__":
    test_print_color_map()
