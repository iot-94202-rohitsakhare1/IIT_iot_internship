
mat1 = [
    [11, 12, 13, 14],
    [15, 16, 17, 18],
    [19, 20, 21, 22]
]

mat2 = (
    (22, 21, 20, 19),
    (18, 17, 16, 15),
    (14, 13, 12, 11)
)

def matrix_calc(m1, m2):
    add_mat = []
    sub_mat = []

    for i in range(3):
        add_row = []
        sub_row = []
        for j in range(4):
            add_row.append(m1[i][j] + m2[i][j])
            sub_row.append(m1[i][j] - m2[i][j])
        add_mat.append(add_row)
        sub_mat.append(sub_row)

    return add_mat, sub_mat


addition, subtraction = matrix_calc(mat1, mat2)

print("Addition Matrix:")
for row in addition:
    print(row)

print("\nSubtraction Matrix:")
for row in subtraction:
    print(row)
