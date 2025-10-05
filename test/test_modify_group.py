from model.group import Group
import random

def test_modify_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    index = old_groups.index(group)
    up_group = (Group(name="updated" + group.name + "name"))
    up_group.id = group.id
    app.group.modify_group_by_id(up_group.id, up_group)
    new_groups = db.get_group_list()
    old_groups[index] = up_group
    assert sorted(old_groups, key=Group.id_or_max) \
           == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) \
               == sorted(app.group.get_group_list(), key=Group.id_or_max)
