pc_nom_1bgn = int(input())
pc_nom_2bgn = int(input())
pc_nom_5bgn = int(input())
total = int(input())

for n1 in range(pc_nom_1bgn + 1):
    for n2 in range(pc_nom_2bgn + 1):
        for n5 in range(pc_nom_5bgn + 1):
            if ((n5 * 5) + (n2 * 2) + (n1 * 1)) == total:

                print(f"{n1} * 1 lv. + {n2} * 2 lv. + {n5} * 5 lv. = {total} lv.")
