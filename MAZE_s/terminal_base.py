def main():
    import table_c
    import os
    import time

    tem = int(input("if you want use default shape enter 1 and for customise enter 2: "))

    if tem == 1:
        a = table_c.Table(x=11, y=11)
        a.add_st_end(start=(1, 5), end=(9, 5))
        a.add_border()
        a.add_wall((2, 1), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (4, 5), (4, 6), (4, 7), (1, 6), (2, 6), (2, 8),
                   (6, 1), (6, 2), (5, 2), (4, 2), (9, 6), (8, 7), (8, 8), (8, 6), (8, 5), (8, 4), (8, 3), (7, 8),
                   (7, 4), (8, 2), (6, 4), (6, 8), (6, 6), (6, 5), (2, 7), (4, 8))
        print("first shape: ")
        a.print_beautiful_shape()
        input("for continue enter: ")
        os.system("cls")
        w = a.processing()
        if w:
            a.add_road()
        else:
            print("There is no way to that point!")
        print("steps: 0:empty  1:wall  2:full  3:start  4:end  (*:road)")
        a.print_shape()
        print("\nfinal shape: \n")
        a.print_beautiful_shape()
        input("finish")

    elif tem == 2:
        st = time.perf_counter()
        a = table_c.Table(x=10, y=20)
        a.add_border()
        a.add_st_end(start=(1, 1), end=(8, 18))
        a.print_beautiful_shape()
        w = a.processing()
        a.add_road()
        en = time.perf_counter()
        a.print_beautiful_shape()
        input(f"{en-st}")


if __name__ == "__main__":
    main()
