vertices = ['V1', 'V2', 'V3', 'V4']

colors = ['C1', 'C2', 'C3', 'C4', 'C5']

adjvertices = {}
adjvertices['V1'] = ['V2', 'V3']
adjvertices['V2'] = ['V1', 'V3', 'V4']
adjvertices['V3'] = ['V1', 'V2', 'V4']
adjvertices['V4'] = ['V2', 'V3']

output_colors = {}

def can_be_colored(ver, color):
    for v in adjvertices.get(ver): 
        col_adjver = output_colors.get(v)
        if col_adjver == color:
            return False

    return True

def mcolor(ver):
    for c in colors:
        if can_be_colored(ver, c):
            return c

def demo():
    for ver in vertices:
        output_colors[ver] = mcolor(ver)

    print (output_colors)


demo()

