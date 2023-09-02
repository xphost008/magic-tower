"""
11 x 11的空间自由发挥！

所有普通道具
[wall]：墙壁【已完成】
[fake-wall]：假墙壁，走过去自动变成地板。【已完成】
[floor]：可以行走的地板【已完成】
[fake-floor]：假地板，走过去自动变成墙壁。【已完成】
[emerald]：绿宝石 + 200 health【已完成】
[ruby]：红宝石 + 5 attack【已完成】
[sapphire]：蓝宝石 + 5 defence【已完成】
[topaz]：黄宝石 + 10 money【已完成】
[yellow-key]：黄钥匙【已完成】
[blue-key]：蓝钥匙【已完成】
[red-key]：红钥匙【已完成】
[green-key]：绿钥匙【已完成】
[yellow-door]：黄门【已完成】
[blue-door]：蓝门【已完成】
[red-door]：红门【已完成】
[green-door]：绿门【已完成】
[lava]：岩浆【已完成】
[upstairs]：上楼楼梯【已完成】
[downstairs]：下楼楼梯【已完成】

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
[lucky-coin]幸运金币：杀死怪物后双倍掉落金钱【已完成】
[ice-magic]冰冻魔法：走过去岩浆自动消失

[villager-<name>]：自定义售卖商人，在villager中自定义。
其中，商人类里有字符串模板可以替换使用。但是只有${sell_count}可以替换成目前售卖次数。如果想指定无数次，可以使用9999999代替。
且目前sell中只提供：【attack】

所有怪物
[green-slime]：绿色史莱姆。【已完成】
[red-slime]：红色史莱姆。【已完成】
[blue-slime]：蓝色史莱姆。【已完成】
[yellow-slime]：黄色史莱姆。【已完成】

所有怪物血量、攻防金钱都在monster代码块中自定义。

生命值属性相克：
如果己方攻击力低于敌方防御力，则不予攻击。
如果己方防御力低于对方攻击力，则必然克血。

克除生命值的公式是：
克除 = (敌血 ÷ (己攻 - 敌防) - 1) * (敌攻 - 己防)

"""

villager = {
    "floor3": {
        "sell": "red-key",
        "count": 1,
        "money": 200,
        "sell-count": 2,
        "say": "我有${sell-count}把红钥匙，200金币1把，你要不要？",
    }
}

monster = {
    "yellow-slime": {
        "health": 20,
        "attack": 7,
        "defence": 7,
        "money": 5
    },
    "green-slime": {
        "health": 30,
        "attack": 10,
        "defence": 10,
        "money": 8,
    },
    "red-slime": {
        "health": 50,
        "attack": 15,
        "defence": 15,
        "money": 10,
    },
    "blue-slime": {
        "health": 80,
        "attack": 20,
        "defence": 20,
        "money": 15
    }
}

floor = [
    [
        ["upstairs", "wall", "floor", "wall", "green-door", "fake-wall", "floor", "fake-floor", "floor", "floor", "ice-magic"],
        ["floor", "wall", "floor", "wall", "floor", "floor", "floor", "green-slime", "floor", "topaz", "floor"],
        ["yellow-key", "wall", "floor", "sapphire", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["blue-key", "wall", "floor", "wall", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["red-key", "wall", "floor", "red-door", "floor", "floor", "floor", "floor", "floor", "wall", "floor"],
        ["green-key", "wall", "floor", "wall", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["emerald", "wall", "floor", "blue-door", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["floor", "wall", "floor", "wall", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["floor", "floor", "floor", "green-door", "floor", "floor", "floor", "ruby", "floor", "floor", "floor"],
        ["yellow-slime", "wall", "floor", "wall", "floor", "floor", "player", "floor", "floor", "floor", "floor"],
        ["blue-slime", "green-slime", "red-slime", "yellow-door", "green-key", "floor", "floor", "floor", "floor",
         "floor", "floor"],
    ],
    [
        ["downstairs", "player", "yellow-key", "yellow-key", "floor", "floor", "floor", "floor", "floor", "floor",
         "floor"],
        ["floor", "floor", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "floor"],
        ["floor", "floor", "green-key", "green-key", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["lava", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
        ["floor", "floor", "floor", "blue-key", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["floor", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "lucky-coin"],
        ["floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["floor", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
        ["floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["floor", "floor", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "floor"],
        ["upstairs", "ruby", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
    ],
    [
        ["downstairs", "player", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["blue-door", "floor", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "villager-floor3"],
        ["floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["floor", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "yellow-door"],
        ["floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["green-door", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "floor"],
        ["floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["floor", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "yellow-door"],
        ["floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
        ["green-door", "floor", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "floor"],
        ["topaz", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
    ]
]

help_page = [
    "难度部分：\n" +
    "    作弊模式：生命：9999999、攻击：9999999、防御：9999999、金钱：9999999\n" +
    "    简单模式：生命：10000、攻击：50、防御：50、金钱：200\n" +
    "    普通模式：生命：6000、攻击：30、防御：30、金钱：150\n" +
    "    困难模式：生命：4000、攻击：20、防御：20、金钱：100\n" +
    "道具部分：\n" +
    "    红宝石：+5 attack\n" +
    "    蓝宝石：+5 defence\n" +
    "    黄宝石：+20 money\n" +
    "    绿宝石：+200 health\n" +
    "    红钥匙：打开红色的门\n" +
    "    蓝钥匙：打开蓝色的门\n" +
    "    黄钥匙：打开黄色的门\n" +
    "    绿钥匙：打开绿色的门\n" +
    "怪物部分：\n" +
    "    绿色史莱姆：生命：30、攻击：10、防御：10、金钱：8\n" +
    "    蓝色史莱姆：生命：80、攻击：20、防御：20、金钱：15\n" +
    "    黄色史莱姆：生命：20、攻击：7、防御：7、金钱：5\n" +
    "    红色史莱姆：生命：50、攻击：15、防御：15、金钱：10",
    "道具部分：\n" +
    "    冰冻魔法：可以走岩浆如履平地。\n"
    "    幸运金币：获得之后，击杀怪物可以获得双倍金币。" +
    "墙壁部分：\n" +
    "    红门：需要红钥匙可以打开\n" +
    "    蓝门：需要蓝钥匙可以打开\n"
    "    黄门：需要黄钥匙可以打开\n"
    "    绿门：需要绿钥匙可以打开\n"
    "    岩浆：需要冰冻魔法方可安全通行\n"
    "商人部分具体按照具体来定。"
]
