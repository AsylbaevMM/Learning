for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            print(f'While X = {x}, Y = {y}, Z = {z}, result = {not(x or y or z) == (not x and not y and not z)}')