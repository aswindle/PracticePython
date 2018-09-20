def draw_row(cols, fill):
    row = "|"
    for i in range(0, cols):
        row += " " + fill + " |"
    print(row)
    
def draw_border(cols):
    border = " "
    for i in range(0, cols):
        border += "--- "
    print(border)
    
rows = int(input("How many rows? "))
cols = int(input("How many columns? "))
fill = input("Fill character? ")
draw_border(cols)
for i in range(0, rows):
    draw_row(cols, fill)
    draw_border(cols)