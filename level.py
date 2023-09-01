"""
11 x 11的空间自由发挥！

所有普通道具
[wall]：墙壁【已完成】
[fake-wall]：假墙壁，走过去自动变成地板。
[floor]：可以行走的地板【已完成】
[fake-floor]：假地板，走过去自动变成墙壁。
[emerald]：绿宝石 + 200 live【已完成】
[ruby]：红宝石 + 5 attack【已完成】
[sapphire]：蓝宝石 + 5 defense【已完成】
[topaz]：黄宝石 + 10 money【已完成】
[yellow-key]：黄钥匙【已完成】
[blue-key]：蓝钥匙【已完成】
[red-key]：红钥匙【已完成】
[green-key]：绿钥匙【已完成】
[yellow-door]：黄门【已完成】
[blue-door]：蓝门【已完成】
[red-door]：红门【已完成】
[green-door]：绿门【已完成】
[lava]：岩浆
[upstairs]：上楼楼梯
[downstairs]：下楼楼梯

所有特殊道具
在此版本中，没有怪物手册，按v键自动查看。
也没有记事本，右下角自动观看。
也没有飞行器，按w键自动往上一层，按s键自动往下一层【前提是上层已经被走过了】
[pickaxe]镐子，可以挖开一格墙壁。
[scroll]地震卷轴：破坏一层楼所有的墙壁
[frost-magic]冰冻魔法：这里改成了直接破除一层楼所有的岩浆，且仅能用一次。
[magic-key]魔法钥匙：自动打开一层楼所有的门。【无论红门蓝门还是黄门】
[holy-water]圣水：在每层楼使用会恢复不同的生命值，在1层用会恢复1000，50层恢复50000。
[fly]51层飞行器：使用后可以在任意楼层直接飞往51层隐藏房间。


[custom-<name>]：自定义，在代码中自定义。

所有怪物
[green-slime]：绿色史莱姆。【已完成】
[red-slime]：红色史莱姆。【已完成】
[blue-slime]：蓝色史莱姆。【已完成】
[yellow-slime]：黄色史莱姆。【已完成】

生命值属性相克：
如果己方攻击力低于敌方防御力，则不予攻击。
如果己方防御力低于对方攻击力，则必然克血。

克除生命值的公式是：
克除 = (敌血 ÷ (己攻 - 敌防) - 1) * (敌攻 - 己防)

"""

monster = {
    "yellow-slime": {
        "life": 20,
        "attack": 7,
        "defense": 7,
        "money": 5
    },
    "green-slime": {
        "life": 30,
        "attack": 10,
        "defense": 10,
        "money": 8,
    },
    "red-slime": {
        "life": 50,
        "attack": 15,
        "defense": 15,
        "money": 10,
    },
    "blue-slime": {
        "life": 80,
        "attack": 20,
        "defense": 20,
        "money": 15
    }
}

floor = [
    [
        ["upstairs", "wall", "floor", "wall", "green-door", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["floor", "wall", "floor", "wall", "floor", "floor", "floor", "green-slime", "floor", "topaz", "floor"],
        ["yellow-key", "wall", "floor", "sapphire", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["blue-key", "wall", "floor", "wall", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["red-key", "wall", "floor", "red-door", "floor", "floor", "floor", "floor", "floor", "wall", "floor"],
        ["green-key", "wall", "floor", "wall", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["emerald", "wall", "floor", "blue-door", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["floor", "wall", "floor", "wall", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["floor", "floor", "floor", "green-door", "floor", "floor", "floor", "ruby", "floor", "floor", "floor"],
        ["yellow-slime", "wall", "floor", "wall", "floor", "floor", "player", "floor", "floor", "floor", "floor"],
        ["blue-slime", "green-slime", "red-slime", "yellow-door", "green-key", "floor", "floor", "floor", "floor", "floor", "floor"],
    ],
    [
        ["downstairs", "player", "yellow-key", "yellow-key", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "floor"],
        ["floor", "floor", "green-key", "green-key", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["floor", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
        ["floor", "floor", "floor", "blue-key", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "floor"],
        ["floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["floor", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
        ["floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "floor"],
        ["upstairs", "ruby", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
    ],
    [
        ["downstairs", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["blue-door", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "floor"],
        ["floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["floor", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "yellow-door"],
        ["floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["green-door", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "floor"],
        ["floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["floor", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "yellow-door"],
        ["floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["green-door", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "floor"],
        ["topaz", "floor", "floor", "player", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
    ]
]