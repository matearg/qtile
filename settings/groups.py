from libqtile.config import Group

# groups = [Group(i) for i in "12345"]

groups = []

group_names = ["1", "2", "3", "4", "5",]

# group_labels = ["", "", "", "", "",] # widgets
# group_labels = ["", "", "", "", "",] # widgetsvariant
group_labels = ["I", "II", "II", "IV", "V",] # widgetsvariant2
# group_labels = ["1", "2", "3", "4", "5",] # widgetsvariant3, widgetsvariant4

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        )
    )
