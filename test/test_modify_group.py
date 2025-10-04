from model.group import Group
from random import randrange
import random

def test_modify_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name"))
    old_groups = db.get_group_list()
    # index = randrange(len(old_groups))
    group = random.choice(old_groups)
    group.name = Group(name="updated group")
    # group.id = old_groups[index].id
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[old_groups.index(group.id)] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_name(app, db):
#     if len(db.get_group_list()) == 0:
#         app.group.create(Group(name="name"))
#     old_groups = db.get_group_list()
#     index = randrange(len(old_groups))
#     group = Group(name="updated group")
#     group.id = old_groups[index].id
#     app.group.modify_group_by_index(index, group)
#     new_groups = db.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     old_groups[index] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_name(app, db):
#     if len(db.get_group_list()) == 0:
#         app.group.create(Group(name="name"))
#     old_groups = app.group.get_group_list()
#     index = randrange(len(old_groups))
#     group = Group(name="updated group")
#     group.id = old_groups[index].id
#     app.group.modify_group_by_index(index, group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     old_groups[index] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(header="header"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="updated header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
