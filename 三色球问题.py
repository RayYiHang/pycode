for red in range(0, 4):
    for yellow in range(0, 4):
        for green in range(2, 7):
            if red + yellow + green == 8:
                print(red, '\t', yellow, '\t', green)
                # \t，为了在不使用表格的情况下，上下对齐，table的意思
