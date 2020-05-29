import yoga

#   YGBENCHMARK("Stack with flex", {
#     const YGNodeRef root = YGNodeNew();
#     YGNodeStyleSetWidth(root, 100);
#     YGNodeStyleSetHeight(root, 100);

#     for (uint32_t i = 0; i < 10; i++) {
#       const YGNodeRef child = YGNodeNew();
#       YGNodeSetMeasureFunc(child, _measure);
#       YGNodeStyleSetFlex(child, 1);
#       YGNodeInsertChild(root, child, 0);
#     }

#     YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirectionLTR);
#     YGNodeFreeRecursive(root);
#   });


def test1():
    root = yoga.Node.create()
    print(dir(root))
    root.width = 100
    root.height = 100

    for i in range(10):
        child = yoga.Node.create()
        child.set_flex(1)
        root.insert_child(child, 0)

    root.calculate_layout()

    print(root)

def dump_node(root, indent=0):
    suffix = ''
    if root.child_count > 0:
        suffix = ', children: ['
    else:
        suffix = '}'
    ident_str = ''.join([' ' for i in range(indent*2)])
    print("%s{left: %d, top: %d, width: %d, height: %d%s" % (ident_str,
        root.calculated_left, root.calculated_top,
        root.calculated_width, root.calculated_height,
        suffix))

    for child in root.children:
        dump_node(child, indent+1)
    if root.child_count > 0:
        print(']}')


def test2():
    # https://yogalayout.com/getting-started/standalone/
# const root = Node.create();
# root.setWidth(500);
# root.setHeight(300);
# root.setJustifyContent(yoga.JUSTIFY_CENTER);
    config = yoga.Config.create()
    config.use_web_defaults = True
    root = yoga.Node.create_with_config(config)
    root.width = 500
    root.height = 300
    root.justify_content = yoga.Justify.Center
    # set default value
    # root.flex_direction = yoga.FlexDirection.Row

# const node1 = Node.create();
# node1.setWidth(100);
# node1.setHeight(100);
    node1 = yoga.Node.create_with_config(config)
    node1.width = 100
    node1.height = 100

# const node2 = Node.create();
# node2.setWidth(100);
# node2.setHeight(100);
    node2 = yoga.Node.create_with_config(config)
    node2.width = 100
    node2.height = 100

# root.insertChild(node1, 0);
# root.insertChild(node2, 1);
    root.insert_child(node1, 0)
    root.insert_child(node2, 1)

    root.calculate_layout(500, 300, yoga.Direction.LTR);
# console.log(root.getComputedLayout());
# // {left: 0, top: 0, width: 500, height: 300}
# console.log(node1.getComputedLayout());
# // {left: 150, top: 0, width: 100, height: 100}
# console.log(node2.getComputedLayout());
# // {left: 250, top: 0, width: 100, height: 100}

    return root


def test5():
    root = yoga.Node.create()
    root.width = 320
    root.height = 80
    root.set_margin(yoga.Edge.Top, 40)
    root.set_margin(yoga.Edge.Left, 10)
    root.set_padding(yoga.Edge.All, 10)
    root.set_flex_direction(yoga.FlexDirection.Row)

    child1 = yoga.Node.create()
    child1.width = 80
    child1.set_margin(yoga.Edge.Right, 10)
    root.insert_child(child1, 0)

    child2 = yoga.Node.create()
    child2.width = 80
    child2.height = 20
    child2.flex_grow = 1
    child2.align_self = yoga.Align.Center
    root.insert_child(child2, 1)

    root.calculate_layout()

    return root

def test4():
    root = yoga.Node.create()
    root.width = 320
    root.height = 80
    root.set_margin(yoga.Edge.Top, 40)
    root.set_margin(yoga.Edge.Left, 10)
    root.set_flex_direction(yoga.FlexDirection.Row)

    child1 = yoga.Node.create()
    child1.width = 80
    root.insert_child(child1, 0)

    child2 = yoga.Node.create()
    child2.width = 80
    child2.flex_grow = 1
    root.insert_child(child2, 1)

    root.calculate_layout()

    return root


def test3():
    root = yoga.Node.create()
    root.width = 320
    root.height = 80
    root.set_margin(yoga.Edge.Top, 40)
    root.set_margin(yoga.Edge.Left, 10)
    root.set_flex_direction(yoga.FlexDirection.Row)

    root.calculate_layout()

    return root

def test6():
    root = yoga.Node.create()
    root.width = 320
    root.height = 575
    root.align_items = yoga.Align.Center
    root.justify_content = yoga.Justify.FlexEnd
    root.set_margin(yoga.Edge.Top, 40)
    root.set_margin(yoga.Edge.Left, 10)
    root.set_padding(yoga.Edge.All, 10)
    root.flex_direction = yoga.FlexDirection.Row

    child1 = yoga.Node.create()
    child1.width = 80
    child1.set_margin(yoga.Edge.Right, 10)
    root.insert_child(child1, 0)

    child2 = yoga.Node.create()
    child2.width = 80
    child2.height = 20
    child2.flex_grow = 1
    child2.align_self = yoga.Align.Center
    root.insert_child(child2, 1)

    root.calculate_layout()

    return root

def test7():
#       <View style={{
#         flex: 1,
#         width: 500,
#         height: 500,
#         alignItems: 'flex-start',
#         padding: 20,
#       }}>
    root = yoga.Node.create()
    root.width = 500
    root.height = 500
    root.align_items = yoga.Align.FlexStart
    root.set_padding(yoga.Edge.All, 20)
    root.set_flex(1)
    root.flex_wrap = yoga.Wrap.Wrap
    root.flex_direction = yoga.FlexDirection.Row
    root.align_content = yoga.Align.Stretch

#         <View style={{
#           flex: 1,
#           width: 100,
#           height: 100,
#         }} />
    child1 = yoga.Node.create()
    child1.width = 100
    child1.height = 100
    # child1.set_flex(1)
    root.insert_child(child1, 0)

#         <View style={{
#           flex: 1,
#           width: 100,
#           height: 100,
#           marginHorizontal: 20,
#           flexGrow: 1,
#         }} />
    child2 = yoga.Node.create()
    child2.width = 100
    child2.height = 100
    # child2.set_flex(1)
    child2.flex_grow = 1
    child2.set_margin(yoga.Edge.Horizontal, 20)
    root.insert_child(child2, 1)

#         <View style={{
#           flex: 1,
#           width: 100,
#           height: 100,
#         }} />
    for i in range(15):
        child3 = yoga.Node.create()
        child3.width = 100
        child3.height = 100
        # child3.set_flex(1)
        root.insert_child(child3, 2+i)

    root.calculate_layout()

    return root


def test8():
    # https://yogalayout.com/getting-started/standalone/
# const root = Node.create();
# root.setWidth(500);
# root.setHeight(300);
# root.setJustifyContent(yoga.JUSTIFY_CENTER);
    root = yoga.Node.create()
    root.width = 500
    root.height = 300
    root.justify_content = yoga.Justify.Center
    # set default value
    root.flex_direction = yoga.FlexDirection.Row

# const node1 = Node.create();
# node1.setWidth(100);
# node1.setHeight(100);
    node1 = yoga.Node.create()
    node1.width = 100
    node1.height = 100

# const node2 = Node.create();
# node2.setWidth(100);
# node2.setHeight(100);
    node2 = yoga.Node.create()
    node2.width = 100
    node2.height = 100

# root.insertChild(node1, 0);
# root.insertChild(node2, 1);
    root.insert_child(node1, 0)
    root.insert_child(node2, 1)

    root.calculate_layout(500, 300, yoga.Direction.LTR);
# console.log(root.getComputedLayout());
# // {left: 0, top: 0, width: 500, height: 300}
# console.log(node1.getComputedLayout());
# // {left: 150, top: 0, width: 100, height: 100}
# console.log(node2.getComputedLayout());
# // {left: 250, top: 0, width: 100, height: 100}

    return root


n = test2()
dump_node(n)
