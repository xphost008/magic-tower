import json
import os

config = {
    "ruby": 5,
    "sapphire": 5,
    "topaz": 20,
    "emerald": 200,
    "villager": {  # 在这里自定义商人
        "villager-red-key": {
            "sell": "red-key",
            "count": 1,
            "money": 200,
            "say": "卖红钥匙咯！200金钱1把，你要不要？",
        }
    },
    "difficulty": {
        "easy": {
            "health": 10000,
            "attack": 50,
            "defence": 50,
            "money": 200
        },
        "normal": {
            "health": 6000,
            "attack": 30,
            "defence": 30,
            "money": 150
        },
        "hard": {
            "health": 4000,
            "attack": 20,
            "defence": 20,
            "money": 100
        },
    },

    "messenger": {  # 在这里自定义传话人
        "messenger-tips": {
            "say": [
                "千万不要捡起上面有笑脸的金币，因为那会让你杀怪的时候掉落比以往少的金钱。",
                "一定要捡起冰冻魔法，它长得像一个蜘蛛网，无需点击即可使用。可以走过岩浆噢！"
            ]
        }
    },

    "monster": {  # 在这里自定义怪物
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
    },

    "floor": [  # 在这里自定义楼层
        [
            ["upstairs", "wall", "fake-wall", "fake-floor", "red-door", "blue-door", "green-door", "yellow-door",
             "red-slime", "yellow-slime", "green-slime"],
            ["blue-key", "red-key", "pickaxe", "lucky-coin", "holy-water", "ice-magic", "emerald", "ruby", "sapphire",
             "topaz", "blue-slime"],
            ["yellow-key", "green-key", "quake-scroll", "magic-key", "tnt", "floor", "floor", "floor", "floor",
             "floor", "floor"],
            ["floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
            ["floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
            ["floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "villager-red-key",
             "floor"],
            ["floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "messenger-tips",
             "floor"],
            ["floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
            ["floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
            ["floor", "floor", "floor", "floor", "floor", "floor", "player", "floor", "floor", "floor", "lava"],
            ["floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "lava", "downstairs"],
        ],
    ],

    "help_page": [  # 在这里自定义帮助文档。
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
        "    幸运金币：获得之后，击杀怪物可以获得双倍金币。\n" +
        "    镐子：获取后可以挖掉自己周围的墙壁。但是假地板需要触发后才能挖。点击使用。\n" +
        "    圣水：获取后每一楼层回复的生命值不同。例如1楼恢复1000，50楼恢复50000。点击使用。\n" +
        "    炸弹：获取后可以炸掉自己周围打不过的怪物，但无法获得金钱，点击使用。\n" +
        "    魔法钥匙：获取后可以打开这一层楼中所有的门，无视红门还是黄门啥的。\n" +
        "    地震卷轴：获取后可以炸掉这一层楼中所有的墙壁，包括假墙壁和假地板。\n" +
        "墙壁部分：\n" +
        "    红门：需要红钥匙可以打开\n" +
        "    蓝门：需要蓝钥匙可以打开\n"
        "    黄门：需要黄钥匙可以打开\n"
        "    绿门：需要绿钥匙可以打开\n"
        "    岩浆：需要冰冻魔法方可安全通行\n"
        "商人部分具体价格按照具体来定。"
    ]
}


def load_json():
    global config
    with open(".\\config.json", "r") as f:
        config = json.loads(f.read())


def spawn_json():
    if not os.path.exists(".\\config.json"):
        conf = json.dumps(config, sort_keys=True, indent=4)
        with open(".\\config.json", "w") as f:
            f.write(conf)
