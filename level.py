import json
import os

config = {
    "allow-cheat": True,
    "ruby": 5,
    "sapphire": 5,
    "topaz": 50,
    "emerald": 400,
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
    "villager": {  # 在这里自定义商人
        "villager-f3": {
            "sell": "blue-key",
            "count": 1,
            "money": 500,
            "max": 2,
            "say": "我有2把蓝钥匙，500金钱一把，你要不？"
        }
    },
    "messenger": {  # 在这里自定义传话人
        "messenger-f1": {
            "say": [
                "传话人：啊，你居然掉下来了，天哪，这个坑里已经几百年没掉下人来了！",
                "你：那我该怎么回去呢？",
                "传话人：我也不知道你该怎么回去，我已经卡在这里好多天了。",
                "你：那你知道些什么呢？",
                "传话人：我只知道这个地底下居住着一位魔王，他法力无边，非常勇敢。",
                "你：那我是不是应该要打败他才能回家？",
                "传话人：应该是的，我只知道这个地下总共有51层，每10层都有一个首领。你要小心啊！",
                "你：但是我现在身上什么都没有，请问我该怎么获得装备？",
                "传话人：好的，我现在得知了一个消息，我知道的铁剑在7楼，铁盾在8楼，没事，我现在和你一起上去，如果前面有消息的话，我会来和你说的。",
                "你：好的，那就太感谢你了！",
                "传话人：前面就是上去的楼梯了，走上前去就可以上楼了！"
            ]
        },
        "messenger-f2": {
            "say": [
                "村民：非常感谢你拯救了我！我被这个该死的守卫关在这里好久了。",
                "你：那你知道怎么打败魔王吗？",
                "村民：我只知道这座塔里，魔王养了一只很凶猛的恶龙，不过没事，我会帮你挖一条隧道的，以便你成功绕过恶龙！",
                "你：好的，那就谢谢你了！"
            ]
        }
    },
    "non-special": {
        "iron-sword": {
            "add": "attack",
            "count": 10,
            "texture": ".\\image\\non-special\\iron_sword.png"
        },
        "iron-shield": {
            "add": "defence",
            "count": 10,
            "texture": ".\\image\\non-special\\iron_shield.png"
        }
    },
    "monster": {  # 在这里自定义怪物
        "yellow-slime": {
            "name": "黄史莱姆",
            "health": 20,
            "attack": 7,
            "defence": 7,
            "money": 5,
            "texture": ".\\image\\monsters\\yellow_slime.png",
            "say": []
        },
        "green-slime": {
            "name": "绿史莱姆",
            "health": 30,
            "attack": 10,
            "defence": 10,
            "money": 8,
            "texture": ".\\image\\monsters\\green_slime.png",
            "say": []
        },
        "red-slime": {
            "name": "红史莱姆",
            "health": 50,
            "attack": 15,
            "defence": 15,
            "money": 10,
            "texture": ".\\image\\monsters\\red_slime.png",
            "say": []
        },
        "blue-slime": {
            "name": "蓝史莱姆",
            "health": 80,
            "attack": 20,
            "defence": 20,
            "money": 15,
            "texture": ".\\image\\monsters\\blue_slime.png",
            "say": []
        },
        "high-guard": {
            "name": "高级卫兵",
            "health": 800,
            "attack": 400,
            "defence": 450,
            "money": 900,
            "texture": ".\\image\\monsters\\high_guard.png",
            "say": []
        },
        "small-bat": {
            "name": "小蝙蝠",
            "health": 100,
            "attack": 40,
            "defence": 30,
            "money": 25,
            "texture": ".\\image\\monsters\\small_bat.png",
            "say": []
        }
    },
    "floor": [  # 在这里自定义楼层
        [
            ["lava", "lava", "lava", "lava", "wall", "upstairs", "wall", "lava", "lava", "lava", "lava"],
            ["lava", "lava", "lava", "lava", "wall", "floor", "wall", "lava", "lava", "lava", "lava"],
            ["lava", "lava", "lava", "lava", "wall", "floor", "wall", "lava", "lava", "lava", "lava"],
            ["lava", "lava", "lava", "lava", "wall", "floor", "wall", "lava", "lava", "lava", "lava"],
            ["lava", "lava", "lava", "lava", "wall", "floor", "wall", "lava", "lava", "lava", "lava"],
            ["lava", "lava", "lava", "wall", "wall", "floor", "wall", "wall", "lava", "lava", "lava"],
            ["lava", "lava", "lava", "wall", "floor", "floor", "floor", "wall", "lava", "lava", "lava"],
            ["lava", "lava", "lava", "wall", "messenger-f1", "floor", "floor", "wall", "lava", "lava", "lava"],
            ["lava", "lava", "lava", "wall", "floor", "floor", "floor", "wall", "lava", "lava", "lava"],
            ["lava", "lava", "lava", "wall", "wall", "floor", "wall", "wall", "lava", "lava", "lava"],
            ["lava", "lava", "lava", "lava", "wall", "player", "wall", "lava", "lava", "lava", "lava"],
        ],
        [
            ["downstairs", "player", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
            ["wall", "wall", "wall", "high-guard", "floor", "high-guard", "wall", "wall", "wall", "wall", "floor"],
            ["sapphire", "floor", "floor", "wall", "magic-door", "wall", "floor", "floor", "ruby", "wall", "floor"],
            ["floor", "blue-key", "floor", "floor", "floor", "floor", "floor", "yellow-key", "floor", "wall", "floor"],
            ["sapphire", "floor", "emerald", "floor", "floor", "floor", "emerald", "floor", "ruby", "wall", "floor"],
            ["floor", "blue-key", "floor", "floor", "floor", "floor", "floor", "yellow-key", "floor", "wall", "floor"],
            ["sapphire", "floor", "emerald", "floor", "floor", "floor", "emerald", "floor", "ruby", "wall", "green-slime"],
            ["floor", "blue-key", "floor", "floor", "floor", "floor", "floor", "yellow-key", "floor", "wall", "yellow-slime"],
            ["sapphire", "floor", "emerald", "floor", "floor", "floor", "emerald", "floor", "ruby", "wall", "blue-slime"],
            ["floor", "blue-key", "floor", "red-key", "messenger-f2", "red-key", "floor", "yellow-key", "floor", "wall", "red-slime"],
            ["sapphire", "floor", "floor", "floor", "green-key", "floor", "floor", "floor", "ruby", "wall", "upstairs"],
        ],
        [
            ["floor", "floor", "wall", "yellow-key", "ruby", "yellow-key", "wall", "villager-f3", "floor", "wall", "upstairs"],
            ["floor", "floor", "wall", "emerald", "blue-key", "emerald", "wall", "floor", "yellow-slime", "wall", "floor"],
            ["floor", "floor", "wall", "yellow-key", "ruby", "yellow-key", "wall", "yellow-slime", "floor", "wall", "floor"],
            ["wall", "wall", "wall", "wall", "floor", "wall", "wall", "wall", "yellow-door", "wall", "floor"],
            ["floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
            ["floor", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor", "floor"],
            ["yellow-door", "wall", "floor", "wall", "wall", "wall", "wall", "yellow-door", "wall", "yellow-door", "wall"],
            ["small-bat", "wall", "floor", "wall", "sapphire", "small-bat", "floor", "floor", "wall", "small-bat", "floor"],
            ["small-bat", "wall", "floor", "wall", "wall", "floor", "floor", "small-bat", "wall", "topaz", "small-bat"],
            ["ruby", "wall", "player", "downstairs", "wall", "floor", "small-bat", "floor", "wall", "small-bat", "emerald"],
        ],
        [
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "upstairs", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "player", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "downstairs", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
        ],
        [
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "upstairs", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "player", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "downstairs", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
        ],
        [
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "upstairs", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "player", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "downstairs", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
        ],
        [
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "upstairs", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "player", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "downstairs", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
        ],
        [
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "upstairs", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "player", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "downstairs", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
        ],
        [
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "upstairs", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "player", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "downstairs", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
        ],
        [
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "upstairs", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "magic-wing", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "player", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "downstairs", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
            ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
        ],
    ],

    "help_page": [  # 在这里自定义帮助文档。
        "难度部分：\n"
        "    作弊模式：生命：9999999、攻击：9999999、防御：9999999、金钱：9999999\n"
        "    简单模式：生命：10000、攻击：50、防御：50、金钱：200\n"
        "    普通模式：生命：6000、攻击：30、防御：30、金钱：150\n"
        "    困难模式：生命：4000、攻击：20、防御：20、金钱：100\n"
        "道具部分：\n"
        "    红宝石：+5 attack\n"
        "    蓝宝石：+5 defence\n"
        "    黄宝石：+20 money\n"
        "    绿宝石：+200 health\n"
        "    红钥匙：打开红色的门\n"
        "    蓝钥匙：打开蓝色的门\n"
        "    黄钥匙：打开黄色的门\n"
        "    绿钥匙：打开绿色的门\n"
        "怪物部分：\n"
        "    绿色史莱姆：生命：30、攻击：10、防御：10、金钱：8\n"
        "    蓝色史莱姆：生命：80、攻击：20、防御：20、金钱：15\n"
        "    黄色史莱姆：生命：20、攻击：7、防御：7、金钱：5\n"
        "    红色史莱姆：生命：50、攻击：15、防御：15、金钱：10",
        "道具部分：\n"
        "    冰冻魔法：可以走岩浆如履平地。\n"
        "    幸运金币：获得之后，击杀怪物可以获得双倍金币。\n"
        "    镐子：获取后可以挖掉自己周围的墙壁。但是假地板需要触发才能挖。点击使用。\n"
        "    圣水：获取后每一楼层回复的生命值不同。例如1楼恢复1000，50楼恢复50000。点击使用。\n"
        "    炸弹：获取后可以炸掉自己周围打不过的怪物，但无法获得金钱，点击使用。\n"
        "    魔法钥匙：获取后可以打开这一层楼中所有的门，无视红门还是黄门啥的。\n"
        "    地震卷轴：获取后可以炸掉这一层楼中所有的墙壁，包括假墙壁和假地板。\n"
        "墙壁部分：\n"
        "    红门：需要红钥匙可以打开。\n"
        "    蓝门：需要蓝钥匙可以打开。\n"
        "    黄门：需要黄钥匙可以打开。\n"
        "    绿门：需要绿钥匙可以打开。\n"
        "    魔法门：紫色，需要特定事件可以打开。\n"
        "    岩浆：需要冰冻魔法方可安全通行。\n"
        "商人部分具体价格按照具体来定。",
        "按键部分：\n"
        "    q键：退出至标题。\n"
        "    Enter键：下一个对话。\n"
        "    上键：向上移动。\n"
        "    下键：向下移动。\n"
        "    左键：向左移动。\n"
        "    右键：向右移动。\n"
        "    y键：确认交易。\n"
        "    n键：取消交易。\n"
        "    v键：随时打开怪物手册。",
        "    在你进入魔塔之时，我觉得我有必要和你说说游戏规则与游戏背景。\n"
        "    你是一个优秀的旅行者，在一天旅途中，你一不小心掉落进了一个深坑。\n"
        "    你一路往下掉，但是掉落的速度却非常慢，直到你掉落进这个深坑的最底层。你在途中看见了每一种怪物。\n"
        "    每一种怪物的属性你都摸得一清二楚，现在你需要逃出去的话，你需要一路攀升至51层，打败最终的大魔王。\n"
        "    游戏规则是：你只需要一步一步往上走，往上走，走到第51层打败魔王即可胜利！\n"
        "    但是第51层可不是那么容易就能到达的，你可能需要很多的攻击力和防御力才能打败大魔王。\n"
        "    你必须多动脑子，为每一层都规划好，这样才能够通关噢！【如果卡关了，那么大概率是你自己的问题。】"
    ]
}


def load_json():
    global config
    with open(".\\config.json", "r", encoding="GBK") as f:
        config = json.loads(f.read())


def spawn_json():
    if not os.path.exists(".\\config.json"):
        conf = json.dumps(config, indent=4, ensure_ascii=False)
        with open(".\\config.json", "w") as f:
            f.write(conf)
