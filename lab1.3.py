def drawgraph():
    print("График функции y = x/2")
    print(" Y")
    
    for i in range(9, 0, -1):
        line = ""
        for x in range(1, 19):
            if abs(x/2 - i) < 0.3:
                line += "•"
            else:
                line += " "
        print(f"{i:2d} {line}")
    
    print(" 0 " + "─" * 18 + " X")
    print("   " + "020406081012141618")

drawgraph()