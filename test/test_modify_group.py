from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name"))
    app.group.modify_first_group(Group(name="updated group"))



def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="header"))
    app.group.modify_first_group(Group(header="updated header"))
