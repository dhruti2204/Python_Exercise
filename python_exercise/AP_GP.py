
def correct_ap(ap):
    common_diff = ap[1] - ap[0]
    for i in range(2, len(ap)):
        if ap[i] - ap[i - 1] != common_diff:
            if ap[i] - ap[i - 1] != common_diff:
                ap[i] = ap[i - 1] + common_diff
            continue
    return ap

def correct_gp(gp):
    common_ratio = int(gp[1] / gp[0])
    for i in range(2, len(gp)):
        if gp[i] / gp[i - 1] != common_ratio:
            gp[i] = gp[i - 1]  * common_ratio
            continue
    return gp


ap = [2, 5, 8, 11, 15, 17]
gp = [3, 6, 9, 12, 16, 18]

corrected_ap = correct_ap(ap)
corrected_gp = correct_gp(gp)

print("Correct A.P. =", corrected_ap)
print("Correct G.P. =", corrected_gp)
