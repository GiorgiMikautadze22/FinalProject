arrow = "    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****"

double_size = ""
double_arrow = ""

for char in arrow:
    if char != "\n":
        double_size += char * 2
    else:
        double_size += char

lines = double_size.split("\n")

for line in lines:
    double_arrow += line
    double_arrow += " " * 10
    double_arrow += line
    double_arrow += "\n"

print(double_arrow)