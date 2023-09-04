# !/usr/bin/python3.10
# -*- coding: utf-8 -*-
# Copyright (C) 2023 Rechalow, Inc. All Rights Reserved
#
# @Time    : 2023/8/29
# @Author  : Rechalow
# @Email   : 273020451@qq.com
# @File    : main.py
# @Software: MagicTower
import sys

import pygame
from pygame.locals import *
import level

# 初始化pygame
pygame.init()
pygame.mixer.init()

favicon = pygame.image.load(".\\favicon.ico")  # 程序图标
pygame.display.set_icon(favicon)  # 设置程序图标

screen = pygame.display.set_mode((1024, 768))  # 设定窗口宽高为1024 x 768
pygame.display.set_caption("Magic Tower Remake 2 Fantastic Work!!")  # 设定窗口标题为此

player_health = 0  # 玩家生命
player_attack = 0  # 玩家攻击
player_defence = 0  # 玩家防御
player_money = 0  # 玩家金钱

failed_image = pygame.image.load(".\\image\\boom.png")  # 死亡动画

player_face_image = pygame.image.load(".\\image\\player_face.png")  # 玩家正脸
player_left_image = pygame.image.load(".\\image\\player_left.png")  # 玩家左脸
player_right_image = pygame.image.load(".\\image\\player_right.png")  # 玩家右脸
player_back_image = pygame.image.load(".\\image\\player_back.png")  # 玩家背面

wall_image = pygame.image.load(".\\image\\wall.png")  # 墙壁
floor_image = pygame.image.load(".\\image\\floor.png")  # 地板
upstairs = pygame.image.load(".\\image\\upstairs.png")  # 上楼
downstairs = pygame.image.load(".\\image\\downstairs.png")  # 下楼
lava_image = pygame.image.load(".\\image\\lava.png")  # 岩浆

emerald_image = pygame.image.load(".\\image\\emerald.png")  # 绿宝石
sapphire_image = pygame.image.load(".\\image\\sapphire.png")  # 蓝宝石
topaz_image = pygame.image.load(".\\image\\topaz.png")  # 黄宝石
ruby_image = pygame.image.load(".\\image\\ruby.png")  # 红宝石

green_key_image = pygame.image.load(".\\image\\green_key.png")  # 绿钥匙
blue_key_image = pygame.image.load(".\\image\\blue_key.png")  # 蓝钥匙
yellow_key_image = pygame.image.load(".\\image\\yellow_key.png")  # 黄钥匙
red_key_image = pygame.image.load(".\\image\\red_key.png")  # 红钥匙

ice_magic_image = pygame.image.load(".\\image\\ice_magic.png")  # 冰冻魔法
lucky_coin_image = pygame.image.load(".\\image\\lucky_coin.png")  # 幸运金币
holy_water_image = pygame.image.load(".\\image\\holy_water.png")  # 圣水
pickaxe_image = pygame.image.load(".\\image\\pickaxe.png")  # 镐子
tnt_image = pygame.image.load(".\\image\\tnt.png")  # 炸弹
magic_key_image = pygame.image.load(".\\image\\magic_key.png")  # 魔法钥匙
quake_scroll_image = pygame.image.load(".\\image\\quake_scroll.png")  # 地震卷轴

# green_slime_image = pygame.image.load(".\\image\\green_slime.png")  # 绿色史莱姆
# blue_slime_image = pygame.image.load(".\\image\\blue_slime.png")  # 蓝色史莱姆
# red_slime_image = pygame.image.load(".\\image\\red_slime.png")  # 红色史莱姆
# yellow_slime_image = pygame.image.load(".\\image\\yellow_slime.png")  # 黄色史莱姆

green_door_image = pygame.image.load(".\\image\\green_door.png")  # 绿门
blue_door_image = pygame.image.load(".\\image\\blue_door.png")  # 蓝门
red_door_image = pygame.image.load(".\\image\\red_door.png")  # 红门
yellow_door_image = pygame.image.load(".\\image\\yellow_door.png")  # 黄门

font_attribute = pygame.font.Font(".\\font\\msyh.ttc", 20)  # 属性栏字体
font_start_menu = pygame.font.Font(".\\font\\simfang.ttf", 96)  # 界面大标题
font_start_button = pygame.font.Font(".\\font\\simfang.ttf", 36)  # 按钮标题
font_message = pygame.font.Font(".\\font\\msyh.ttc", 16)  # 信息框字体
font_level = pygame.font.Font(".\\font\\msyh.ttc", 42)  # 楼层字体
font_help = pygame.font.Font(".\\font\\msyh.ttc", 24)  # 帮助字体

villager_image = pygame.image.load(".\\image\\villager.png")  # 商人
messenger_image = pygame.image.load(".\\image\\messenger.png")  # 传话人
error_image = pygame.image.load(".\\image\\error.png")  # 错误贴图

ding_music = pygame.mixer.Sound(".\\music\\ogg\\ding.ogg")
kill_music = pygame.mixer.Sound(".\\music\\ogg\\kill.ogg")
open_music = pygame.mixer.Sound(".\\music\\ogg\\open.ogg")
pick_music = pygame.mixer.Sound(".\\music\\ogg\\pick.ogg")
extinguish_music = pygame.mixer.Sound(".\\music\\ogg\\fizz.ogg")
yes_music = pygame.mixer.Sound(".\\music\\ogg\\yes.ogg")
no_music = pygame.mixer.Sound(".\\music\\ogg\\no.ogg")

yellow_key = 0  # 黄钥匙个数
blue_key = 0  # 蓝钥匙个数
red_key = 0  # 红钥匙个数
green_key = 0  # 绿钥匙个数

can_turn = True  # 玩家此时是否可以行走
is_fail = False  # 是否失败

ice_magic = False  # 是否拥有冰冻魔法
lucky_coin = False  # 是否拥有幸运金币
pickaxe = False  # 是否拥有稿子
holy_water = False  # 是否拥有圣水
magic_key = False  # 是否拥有稿子
tnt = False  # 是否拥有圣水
quake_scroll = False  # 是否拥有稿子

current_level = 0  # 当前楼层
face = 1  # 玩家朝向【1：前、2：后、3：左、4：右】

villager_sell = ""
villager_count = 0
villager_money = 0

x = 0  # 当前走过的横坐标真实值
y = 0  # 当前走过的纵坐标真实值
dx = 0  # 当前走过的横坐标比例值
dy = 0  # 当前走过的纵坐标比例值

help_page = 0  # 帮助索引页面。


def match_face():
    """
    匹配玩家的朝向，从而判定此时是否是墙壁
    也可以用于判断未能通过区域。例如没钥匙的时候撞门。
    """
    global x, y, dx, dy
    match face:
        case 1:
            y -= 64
            dy -= 1
        case 2:
            y += 64
            dy += 1
        case 3:
            x += 64
            dx += 1
        case 4:
            x -= 64
            dx -= 1


def return_pre_face():
    global x, y, dx, dy
    match face:
        case 1:
            return x, y + 64, dx, dy + 1
        case 2:
            return x, y - 64, dx, dy - 1
        case 3:
            return x - 64, y, dx - 1, dy
        case 4:
            return x + 64, y, dx + 1, dy


def draw_player():
    match face:
        case 1:
            screen.blit(player_face_image, (x, y))
        case 2:
            screen.blit(player_back_image, (x, y))
        case 3:
            screen.blit(player_left_image, (x, y))
        case 4:
            screen.blit(player_right_image, (x, y))


def reduce_hp(own_attack: int, own_defence: int, enemy_attack: int, enemy_defence: int, enemy_hp: int):
    """
    :param own_attack: 己方攻击
    :param own_defence: 己方防御
    :param enemy_attack: 敌方攻击
    :param enemy_defence: 敌方防御
    :param enemy_hp: 敌方血量
    :return: 己方克除血量
    """
    if enemy_attack <= own_defence:
        return 0
    red = (round(enemy_hp / (own_attack - enemy_defence))) * (enemy_attack - own_defence)
    if red < 0:
        red = 0
    return red


def update_level():
    """
    更新楼层
    """
    global screen
    global font_level
    surface = pygame.Surface((256, 52))
    surface.fill((192, 192, 192))
    screen.blit(surface, (768, 0))
    text = font_level.render("第" + str(current_level + 1) + "层", True, (0, 0, 0))
    screen.blit(text, (768, 0))


def update_prop():
    global screen
    surface = pygame.Surface((256, 256))
    surface.fill((192, 192, 192))
    screen.blit(surface, (768, 256))
    no_prop = pygame.Surface((64, 64))
    no_prop.fill((192, 192, 192))
    if ice_magic:
        screen.blit(ice_magic_image, (768, 256))
    else:
        screen.blit(no_prop, (768, 256))
    if lucky_coin:
        screen.blit(lucky_coin_image, (832, 256))
    else:
        screen.blit(no_prop, (832, 256))
    if holy_water:
        screen.blit(holy_water_image, (896, 256))
    else:
        screen.blit(no_prop, (896, 256))
    if pickaxe:
        screen.blit(pickaxe_image, (960, 256))
    else:
        screen.blit(no_prop, (960, 256))
    if magic_key:
        screen.blit(magic_key_image, (768, 320))
    else:
        screen.blit(no_prop, (768, 320))
    if tnt:
        screen.blit(tnt_image, (832, 320))
    else:
        screen.blit(no_prop, (832, 320))
    if quake_scroll:
        screen.blit(quake_scroll_image, (896, 320))
    else:
        screen.blit(no_prop, (896, 320))
    pygame.draw.rect(screen, (0, 0, 0), ((768, 256), (256, 256)), width=3)


def help_message(text: str):
    """
    :param text: 帮助文本
    :return:
    """
    global screen
    surface = pygame.Surface((960, 604))
    surface.set_colorkey((0, 0, 0, 255))
    screen.blit(surface, (32, 32))
    pygame.draw.rect(screen, (200, 200, 200), ((32, 32), (960, 604)), width=10)
    count = 0
    char_width = [font_help.render(char, True, (0, 0, 0)).get_width() for char in text]
    lines = []
    current_text = ""
    for i, chars in enumerate(text):
        current_text += chars
        count += char_width[i]
        if chars == "\n":
            current_text = current_text[0:len(current_text) - 1]
            lines.append(current_text)
            current_text = ""
            count = 0
            continue
        if count > 908:
            lines.append(current_text)
            current_text = ""
            count = 0
    lines.append(current_text)
    for i in range(0, len(lines)):
        text = font_help.render(lines[i], True, (1, 1, 1))
        text.set_colorkey((0, 0, 0, 255))
        screen.blit(text, (46, 42 + 28 * i))


def message(text: str, is_lock: bool):
    """
    :param text: 信息框文本【自动换行】。
    :param is_lock: 是否锁住屏幕
    :return: 无
    """
    global can_turn
    global screen
    global player_money, player_attack, player_health, player_defence
    global red_key, yellow_key, blue_key, green_key
    surface = pygame.Surface((256, 256))
    surface.fill((192, 192, 192))
    screen.blit(surface, (768, 512))
    pygame.draw.rect(screen, (0, 0, 0), ((768, 512), (256, 256)), width=10)
    count = 0
    char_width = [font_message.render(char, True, (0, 0, 0)).get_width() for char in text]
    lines = []
    current_text = ""
    for i, chars in enumerate(text):
        current_text += chars
        count += char_width[i]
        if chars == "\n":
            current_text = current_text[0:len(current_text) - 1]
            lines.append(current_text)
            current_text = ""
            count = 0
            continue
        if count > 220:
            lines.append(current_text)
            current_text = ""
            count = 0
    lines.append(current_text)
    for i in range(0, len(lines)):
        text = font_message.render(lines[i], True, (0, 0, 0))
        screen.blit(text, (778, 522 + 16 * i))
    if is_lock:
        can_turn = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if villager_sell == "":
                            screen.blit(surface, (768, 512))
                            pygame.draw.rect(screen, (0, 0, 0), ((768, 512), (256, 256)), width=10)
                            return
                    if event.key == pygame.K_y:
                        if villager_sell != "":
                            if player_money >= villager_money:
                                player_money -= villager_money
                                if villager_sell == "attack":
                                    player_attack += villager_count
                                elif villager_sell == "health":
                                    player_health += villager_count
                                elif villager_sell == "defence":
                                    player_defence += villager_count
                                elif villager_sell == "red-key":
                                    red_key += villager_count
                                elif villager_sell == "yellow-key":
                                    yellow_key += villager_count
                                elif villager_sell == "blue-key":
                                    blue_key += villager_count
                                elif villager_sell == "green-key":
                                    green_key += villager_count
                                message("交易愉快！", False)
                                yes_music.play()
                                update()
                            else:
                                message("金钱不够……", False)
                                no_music.play()
                            return
                    if event.key == pygame.K_n:
                        if villager_sell != "":
                            message("你取消了交易。", False)
                            no_music.play()
                            update()
                            return
            draw_player()
            pygame.display.flip()
            pygame.display.update()


def update_attribute():
    """
    更新属性数据
    """
    global screen
    surface = pygame.Surface((256, 104))
    surface.fill((192, 192, 192))
    screen.blit(surface, (768, 52))
    text_health = font_attribute.render("生命：" + str(player_health), True, (0, 0, 0))
    text_attack = font_attribute.render("攻击：" + str(player_attack), True, (0, 0, 0))
    text_defence = font_attribute.render("防御：" + str(player_defence), True, (0, 0, 0))
    text_money = font_attribute.render("金钱：" + str(player_money), True, (0, 0, 0))
    screen.blit(text_health, (772, 52))
    screen.blit(text_attack, (772, 76))
    screen.blit(text_defence, (772, 100))
    screen.blit(text_money, (772, 124))


def update_key():
    """
    更新钥匙数据
    """
    global screen
    surface = pygame.Surface((256, 104))
    surface.fill((192, 192, 192))
    screen.blit(surface, (768, 152))
    text_yellow = font_attribute.render("黄钥匙：" + str(yellow_key), True, (255, 255, 0))
    text_blue = font_attribute.render("蓝钥匙：" + str(blue_key), True, (0, 0, 255))
    text_red = font_attribute.render("红钥匙：" + str(red_key), True, (255, 0, 0))
    text_green = font_attribute.render("绿钥匙：" + str(green_key), True, (0, 255, 0))
    screen.blit(text_yellow, (772, 152))
    screen.blit(text_blue, (772, 176))
    screen.blit(text_red, (772, 200))
    screen.blit(text_green, (772, 224))


def update():
    update_level()
    update_prop()
    update_attribute()
    update_key()


def player_move():
    """
    玩家移动，通过全局变量控制，无需参数
    """
    global player_health, player_attack, player_defence, player_money
    global red_key, blue_key, green_key, yellow_key
    global is_fail, can_turn, current_level
    global x, y, dx, dy
    global ice_magic, lucky_coin, holy_water, pickaxe, quake_scroll, magic_key, tnt
    global villager_sell, villager_money, villager_count
    if is_fail:
        return
    x = max(32, min(672, x))
    y = max(32, min(672, y))
    dx = max(1, min(11, dx))
    dy = max(1, min(11, dy))
    lvl = level.config["floor"][current_level]
    if lvl[dy - 1][dx - 1] == "wall":
        match_face()
        return
    for key in level.config["monster"].keys():
        if lvl[dy - 1][dx - 1] == key:
            if player_attack < int(level.config["monster"][key]["defence"]):
                message("无法击打" + key, False)
                match_face()
                return
            player_health -= reduce_hp(player_attack, player_defence, int(level.config["monster"][key]["attack"]),
                                       int(level.config["monster"][key]["defence"]), int(level.config["monster"][key]["health"]))
            if lucky_coin:
                player_money += int(level.config["monster"][key]["money"]) * 2
                message("你战胜了" + key + "，金钱+" + str(level.config["monster"][key]["money"] * 2), False)
            else:
                player_money += int(level.config["monster"][key]["money"])
                message("你战胜了" + key + "，金钱+" + str(level.config["monster"][key]["money"]), False)
            kill_music.play()
    # if lvl[dy - 1][dx - 1] == "slime":
    #     if player_attack < 10:
    #         return x, y, dx, dy
    #     player_health -= reduce_hp(player_attack, player_defence, 10, 10, 30)
    #     player_money += 5
    #     message("你战胜了史莱姆，金钱 + 5")
    #     can_turn = True
    for key in level.config["villager"].keys():
        if lvl[dy - 1][dx - 1] == key:
            match_face()
            villager_sell = str(level.config["villager"][key]["sell"])
            villager_count = int(level.config["villager"][key]["count"])
            villager_money = int(level.config["villager"][key]["money"])
            message(level.config["villager"][key]["say"] + "\n按Y确定，按N取消", True)
            can_turn = True
            villager_sell = ""
            villager_count = 0
            villager_money = 0
            return
    for key in level.config["messenger"].keys():
        if lvl[dy - 1][dx - 1] == key:
            lvl[dy - 1][dx - 1] = "floor"
            match_face()
            for say in level.config["messenger"][key]["say"]:
                message(say, True)
            can_turn = True
            tx, ty, tdx, tdy = return_pre_face()
            screen.blit(floor_image, (tx, ty))
            return
    match lvl[dy - 1][dx - 1]:
        case "topaz":
            player_money += int(level.config["topaz"])
            message("你吃掉了黄宝石，金钱+" + str(level.config["topaz"]), False)
            pick_music.play()
        case "sapphire":
            player_defence += int(level.config["sapphire"])
            message("你吃掉了蓝宝石，防御+" + str(level.config["sapphire"]), False)
            pick_music.play()
        case "ruby":
            player_attack += int(level.config["ruby"])
            message("你吃掉了红宝石，攻击+" + str(level.config["ruby"]), False)
            pick_music.play()
        case "emerald":
            player_health += int(level.config["emerald"])
            message("你吃掉了绿宝石，生命+" + str(level.config["emerald"]), False)
            pick_music.play()
        case "yellow-key":
            yellow_key += 1
            message("你得到了黄钥匙", False)
            pick_music.play()
        case "green-key":
            green_key += 1
            message("你得到了绿钥匙", False)
            pick_music.play()
        case "blue-key":
            blue_key += 1
            message("你得到了蓝钥匙", False)
            pick_music.play()
        case "red-key":
            red_key += 1
            message("你得到了红钥匙", False)
            pick_music.play()
        case "yellow-door":
            if yellow_key < 1:
                message("黄钥匙不够", False)
                match_face()
                return
            else:
                message("你打开了黄门", False)
                yellow_key -= 1
                open_music.play()
        case "blue-door":
            if blue_key < 1:
                message("蓝钥匙不够", False)
                match_face()
                return
            else:
                message("你打开了蓝门", False)
                blue_key -= 1
                open_music.play()
        case "red-door":
            if red_key < 1:
                message("红钥匙不够", False)
                match_face()
                return
            else:
                message("你打开了红门", False)
                red_key -= 1
                open_music.play()
        case "green-door":
            if green_key < 1:
                message("绿钥匙不够", False)
                match_face()
                return
            else:
                message("你打开了绿门", False)
                green_key -= 1
                open_music.play()
        case "upstairs":
            match_face()
            lvl[dy - 1][dx - 1] = "player"
            level.config["floor"][current_level] = lvl
            current_level += 1
            if current_level >= len(level.config["floor"]) - 1:
                current_level = len(level.config["floor"]) - 1
            initFloor()
            message("上到：" + str(current_level + 1) + "层", False)
            return
        case "downstairs":
            match_face()
            lvl[dy - 1][dx - 1] = "player"
            level.config["floor"][current_level] = lvl
            current_level -= 1
            if current_level <= 0:
                current_level = 0
            initFloor()
            message("下到：" + str(current_level + 1) + "层", False)
            return
        case "ice-magic":
            message("获得”冰冻魔法“", False)
            ice_magic = True
            pick_music.play()
        case "lucky-coin":
            message("获得”幸运金币“，金钱 * 2", False)
            lucky_coin = True
            pick_music.play()
        case "holy-water":
            message("获得”圣水“，不同楼层使用会有恢复不同血量。", False)
            holy_water = True
            pick_music.play()
        case "pickaxe":
            message("获得”镐子“，可以挖开自己身边的墙壁，假地板需触发。", False)
            pickaxe = True
            pick_music.play()
        case "quake-scroll":
            message("获得”地震卷轴“，可以炸掉这一整层的墙壁，包括假地板。", False)
            quake_scroll = True
            pick_music.play()
        case "tnt":
            message("获得”炸弹“，可以炸死自己周围的怪物。", False)
            tnt = True
            pick_music.play()
        case "magic-key":
            message("获得”魔法钥匙“，可以打开这一层楼的所有门，无视黄门还是红门。", False)
            magic_key = True
            pick_music.play()
        case "lava":
            if not ice_magic:
                message("你不能穿过这里。", False)
                match_face()
                return
            else:
                message("你熄灭了岩浆。", False)
                extinguish_music.play()
        case "fake-wall":
            message("你遇到了假墙壁", False)
            lvl[dy - 1][dx - 1] = "floor"
        case "fake-floor":
            message("你遇到了假地板", False)
            lvl[dy - 1][dx - 1] = "wall"
            screen.blit(wall_image, (x, y))
            match_face()
            return

    lvl[dy - 1][dx - 1] = "player"
    # match face:
    #     case 1:
    #         lvl[dy][dx - 1] = "floor"
    #         print(str(dy) + "  " + str(dx))
    #     case 2:
    #         lvl[dy - 2][dx - 1] = "floor"
    #     case 3:
    #         lvl[dy - 1][dx - 2] = "floor"
    #     case 4:
    #         lvl[dy - 1][dx] = "floor"
    update()
    if player_health <= 0:
        is_fail = True
        return
    level.config["floor"][current_level] = lvl


def draw_button(txt: str, b: tuple[int, int, int, int], lvl: tuple[int, int], c: tuple[int, int, int]):
    """
    :param txt: 按钮文字
    :param b: 【1：按钮宽度，2：按钮高度，3：按钮距左，4：按钮距上】
    :param lvl: 【1：文字距左，2：文字距上】
    :param c: 颜色
    :return: 无
    """
    surface = pygame.Surface((b[0], b[1]))
    surface.set_colorkey((0, 0, 0, 255))
    screen.blit(surface, (b[2], b[3]))
    text = font_start_button.render(txt, True, (c[0], c[1], c[2]))
    text.set_colorkey((0, 0, 0, 255))
    screen.blit(text, (lvl[0], lvl[1]))
    pygame.draw.rect(screen, (c[0], c[1], c[2]), ((b[2], b[3]), (b[0], b[1])), width=10)


def game_help():
    global screen
    global help_page
    for ima in range(0, 16):
        for ge in range(0, 12):
            screen.blit(floor_image, (ima * 64, ge * 64))
    help_message(level.config["help_page"][help_page])
    if help_page != 0:
        draw_button("上一页", (200, 100, 32, 650), (77, 680), (200, 200, 200))
    draw_button("返回", (200, 100, 412, 650), (472, 680), (200, 200, 200))
    if help_page != len(level.config["help_page"]) - 1:
        draw_button("下一页", (200, 100, 792, 650), (837, 680), (200, 200, 200))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                mouse = pygame.mouse.get_pos()
                mouse_left = mouse[0]
                mouse_top = mouse[1]
                if help_page != 0:
                    if 650 <= mouse_top <= 750 and 32 <= mouse_left <= 232:
                        draw_button("上一页", (200, 100, 32, 650), (77, 680), (140, 255, 140))
                    else:
                        draw_button("上一页", (200, 100, 32, 650), (77, 680), (200, 200, 200))
                if 650 <= mouse_top <= 750 and 412 <= mouse_left <= 612:
                    draw_button("返回", (200, 100, 412, 650), (472, 680), (140, 255, 140))
                else:
                    draw_button("返回", (200, 100, 412, 650), (472, 680), (200, 200, 200))
                if help_page != len(level.config["help_page"]) - 1:
                    if 650 <= mouse_top <= 750 and 792 <= mouse_left <= 992:
                        draw_button("下一页", (200, 100, 792, 650), (837, 680), (140, 255, 140))
                    else:
                        draw_button("下一页", (200, 100, 792, 650), (837, 680), (200, 200, 200))
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                mouse_left = mouse[0]
                mouse_top = mouse[1]
                if help_page != 0:
                    if 650 <= mouse_top <= 750 and 32 <= mouse_left <= 232:
                        help_page -= 1
                        game_help()
                if help_page != len(level.config["help_page"]) - 1:
                    if 650 <= mouse_top <= 750 and 792 <= mouse_left <= 992:
                        help_page += 1
                        game_help()
                if 650 <= mouse_top <= 750 and 412 <= mouse_left <= 612:
                    game_launch()
        pygame.display.flip()
        pygame.display.update()


def game_launch():
    global screen
    for ima in range(0, 16):
        for ge in range(0, 12):
            screen.blit(floor_image, (ima * 64, ge * 64))
    text_start_menu = font_start_menu.render("欢迎来到魔塔世界", True, (190, 10, 60))
    text_start_menu.set_colorkey((0, 0, 0, 255))
    screen.blit(text_start_menu, (108, 128))
    draw_button("开始游戏", (200, 100, 400, 300), (430, 330), (200, 200, 200))
    draw_button("帮助", (200, 100, 400, 430), (460, 460), (200, 200, 200))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                mouse = pygame.mouse.get_pos()
                mouse_left = mouse[0]
                mouse_top = mouse[1]
                if 300 <= mouse_top <= 400 <= mouse_left <= 600:
                    draw_button("开始游戏", (200, 100, 400, 300), (430, 330), (140, 255, 140))
                else:
                    draw_button("开始游戏", (200, 100, 400, 300), (430, 330), (200, 200, 200))
                if 530 >= mouse_top >= 430 and 600 >= mouse_left >= 400:
                    draw_button("帮助", (200, 100, 400, 430), (460, 460), (140, 255, 140))
                else:
                    draw_button("帮助", (200, 100, 400, 430), (460, 460), (200, 200, 200))
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                mouse_left = mouse[0]
                mouse_top = mouse[1]
                if 300 <= mouse_top <= 400 <= mouse_left <= 600:
                    choose_level()
                if 530 >= mouse_top >= 430 and 600 >= mouse_left >= 400:
                    game_help()
        pygame.display.flip()
        pygame.display.update()


def choose_level():
    global player_health, player_attack, player_defence, player_money
    global screen
    for ima in range(0, 16):
        for ge in range(0, 12):
            screen.blit(floor_image, (ima * 64, ge * 64))
    draw_button("作弊", (200, 100, 400, 100), (460, 130), (200, 200, 200))
    draw_button("简单", (200, 100, 400, 230), (460, 260), (200, 200, 200))
    draw_button("普通", (200, 100, 400, 360), (460, 390), (200, 200, 200))
    draw_button("困难", (200, 100, 400, 490), (460, 520), (200, 200, 200))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                mouse = pygame.mouse.get_pos()
                mouse_left = mouse[0]
                mouse_top = mouse[1]
                if 400 <= mouse_left <= 600 and 100 <= mouse_top <= 200:
                    draw_button("作弊", (200, 100, 400, 100), (460, 130), (140, 255, 140))
                else:
                    draw_button("作弊", (200, 100, 400, 100), (460, 130), (200, 200, 200))
                if 400 <= mouse_left <= 600 and 230 <= mouse_top <= 330:
                    draw_button("简单", (200, 100, 400, 230), (460, 260), (140, 255, 140))
                else:
                    draw_button("简单", (200, 100, 400, 230), (460, 260), (200, 200, 200))
                if 400 <= mouse_left <= 600 and 360 <= mouse_top <= 460:
                    draw_button("普通", (200, 100, 400, 360), (460, 390), (140, 255, 140))
                else:
                    draw_button("普通", (200, 100, 400, 360), (460, 390), (200, 200, 200))
                if 400 <= mouse_left <= 600 and 490 <= mouse_top <= 590:
                    draw_button("困难", (200, 100, 400, 490), (460, 520), (140, 255, 140))
                else:
                    draw_button("困难", (200, 100, 400, 490), (460, 520), (200, 200, 200))
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                mouse_left = mouse[0]
                mouse_top = mouse[1]
                if 400 <= mouse_left <= 600 and 100 <= mouse_top <= 200:
                    player_health = 9999999
                    player_attack = 9999999
                    player_defence = 9999999
                    player_money = 9999999
                    initFloor()
                    start()
                if 400 <= mouse_left <= 600 and 230 <= mouse_top <= 330:
                    player_health = int(level.config["difficulty"]["easy"]["health"])
                    player_attack = int(level.config["difficulty"]["easy"]["attack"])
                    player_defence = int(level.config["difficulty"]["easy"]["defence"])
                    player_money = int(level.config["difficulty"]["easy"]["money"])
                    initFloor()
                    start()
                if 400 <= mouse_left <= 600 and 360 <= mouse_top <= 460:
                    player_health = int(level.config["difficulty"]["normal"]["health"])
                    player_attack = int(level.config["difficulty"]["normal"]["attack"])
                    player_defence = int(level.config["difficulty"]["normal"]["defence"])
                    player_money = int(level.config["difficulty"]["normal"]["money"])
                    initFloor()
                    start()
                if 400 <= mouse_left <= 600 and 490 <= mouse_top <= 590:
                    player_health = int(level.config["difficulty"]["hard"]["health"])
                    player_attack = int(level.config["difficulty"]["hard"]["attack"])
                    player_defence = int(level.config["difficulty"]["hard"]["defence"])
                    player_money = int(level.config["difficulty"]["hard"]["money"])
                    initFloor()
                    start()
        pygame.display.flip()
        pygame.display.update()


def blit_initial():
    global screen
    global x, y, dx, dy
    for i in range(0, 13):
        screen.blit(wall_image, (-32 + i * 64, -32))
    for i in range(0, 13):
        screen.blit(wall_image, (-32, -32 + i * 64))
    for i in range(0, 13):
        screen.blit(wall_image, (736, -32 + i * 64))
    for i in range(0, 13):
        screen.blit(wall_image, (-32 + i * 64, 736))
    for i in range(0, 11):
        for j in range(0, 11):
            screen.blit(floor_image, (32 + i * 64, 32 + j * 64))
    x = 6
    y = 11
    dx = 352
    dy = 672
    for i in range(0, len(level.config["floor"][current_level])):
        for j in range(0, len(level.config["floor"][current_level][i])):
            if level.config["floor"][current_level][i][j] == "lucky-coin":
                screen.blit(lucky_coin_image, (32 + j * 64, 32 + i * 64))
            elif level.config["floor"][current_level][i][j] == "ice-magic":
                screen.blit(ice_magic_image, (32 + j * 64, 32 + i * 64))
            elif level.config["floor"][current_level][i][j] == "pickaxe":
                screen.blit(pickaxe_image, (32 + j * 64, 32 + i * 64))
            elif level.config["floor"][current_level][i][j] == "holy-water":
                screen.blit(holy_water_image, (32 + j * 64, 32 + i * 64))
            elif level.config["floor"][current_level][i][j] == "tnt":
                screen.blit(tnt_image, (32 + j * 64, 32 + i * 64))
            elif level.config["floor"][current_level][i][j] == "quake-scroll":
                screen.blit(quake_scroll_image, (32 + j * 64, 32 + i * 64))
            elif level.config["floor"][current_level][i][j] == "magic-key":
                screen.blit(magic_key_image, (32 + j * 64, 32 + i * 64))
            elif "wall" in level.config["floor"][current_level][i][j]:
                screen.blit(wall_image, (32 + j * 64, 32 + i * 64))
            elif "floor" in level.config["floor"][current_level][i][j]:
                pass
            elif level.config["floor"][current_level][i][j] == "lava":
                screen.blit(lava_image, (32 + j * 64, 32 + i * 64))
            elif level.config["floor"][current_level][i][j] == "upstairs":
                screen.blit(upstairs, (32 + j * 64, 32 + i * 64))
            elif level.config["floor"][current_level][i][j] == "downstairs":
                screen.blit(downstairs, (32 + j * 64, 32 + i * 64))
            elif level.config["floor"][current_level][i][j] == "emerald":
                screen.blit(emerald_image, (32 + j * 64, 32 + i * 64))
            elif level.config["floor"][current_level][i][j] == "ruby":
                screen.blit(ruby_image, (32 + j * 64, 32 + i * 64))
            elif level.config["floor"][current_level][i][j] == "sapphire":
                screen.blit(sapphire_image, (32 + j * 64, 32 + i * 64))
            elif level.config["floor"][current_level][i][j] == "topaz":
                screen.blit(topaz_image, (32 + j * 64, 32 + i * 64))
            elif level.config["floor"][current_level][i][j] in level.config["monster"].keys():
                monster_image = pygame.image.load(
                    level.config["monster"][level.config["floor"][current_level][i][j]]["texture"])
                screen.blit(monster_image, (32 + j * 64, 32 + i * 64))
            # elif level.config["floor"][current_level][i][j] == "green-slime":
            #     screen.blit(green_slime_image, (32 + j * 64, 32 + i * 64))
            # elif level.config["floor"][current_level][i][j] == "red-slime":
            #     screen.blit(red_slime_image, (32 + j * 64, 32 + i * 64))
            # elif level.config["floor"][current_level][i][j] == "blue-slime":
            #     screen.blit(blue_slime_image, (32 + j * 64, 32 + i * 64))
            # elif level.config["floor"][current_level][i][j] == "yellow-slime":
            #     screen.blit(yellow_slime_image, (32 + j * 64, 32 + i * 64))
            elif level.config["floor"][current_level][i][j] == "red-key":
                screen.blit(red_key_image, (32 + j * 64, 32 + i * 64))
            elif level.config["floor"][current_level][i][j] == "blue-key":
                screen.blit(blue_key_image, (32 + j * 64, 32 + i * 64))
            elif level.config["floor"][current_level][i][j] == "green-key":
                screen.blit(green_key_image, (32 + j * 64, 32 + i * 64))
            elif level.config["floor"][current_level][i][j] == "yellow-key":
                screen.blit(yellow_key_image, (32 + j * 64, 32 + i * 64))
            elif level.config["floor"][current_level][i][j] == "red-door":
                screen.blit(red_door_image, (32 + j * 64, 32 + i * 64))
            elif level.config["floor"][current_level][i][j] == "blue-door":
                screen.blit(blue_door_image, (32 + j * 64, 32 + i * 64))
            elif level.config["floor"][current_level][i][j] == "green-door":
                screen.blit(green_door_image, (32 + j * 64, 32 + i * 64))
            elif level.config["floor"][current_level][i][j] == "yellow-door":
                screen.blit(yellow_door_image, (32 + j * 64, 32 + i * 64))
            elif "villager" in level.config["floor"][current_level][i][j]:
                screen.blit(villager_image, (32 + j * 64, 32 + i * 64))
            elif "messenger" in level.config["floor"][current_level][i][j]:
                screen.blit(messenger_image, (32 + j * 64, 32 + i * 64))
            elif level.config["floor"][current_level][i][j] == "player":
                screen.blit(player_face_image, (32 + j * 64, 32 + i * 64))
                dx = j + 1
                dy = i + 1
                x = (32 + j * 64)
                y = (32 + i * 64)
            else:
                screen.blit(error_image, (32 + j * 64, 32 + i * 64))


def init():
    global can_turn, ice_magic, lucky_coin, pickaxe, holy_water, magic_key, tnt, quake_scroll
    global current_level, yellow_key, red_key, blue_key, green_key, face
    ice_magic = False
    lucky_coin = False
    pickaxe = False
    holy_water = False
    magic_key = False
    tnt = False
    quake_scroll = False
    yellow_key = 0
    red_key = 0
    blue_key = 0
    green_key = 0
    current_level = 0
    face = 1
    update()
    pygame.mixer.music.load(".\\music\\bgm.mp3")
    pygame.mixer.music.play(-1, 0.0)
    message("=游玩须知=  ：  按Enter键继续……", True)
    message("=游玩须知=  ：  在本魔塔游戏中，任何角色的名字都是虚构的，与现实生活毫无关系。", True)
    message("=游玩须知=  ：  在游玩时，你需要注意，不要轻易相信任何角色的对话，因为他们大多数不可信。", True)
    message("=游玩须知=  ：  如果你同意，请按Enter键继续。", True)
    can_turn = True


temp_first = True


def initFloor():
    global screen
    global can_turn, current_level, temp_first
    blit_initial()
    if temp_first:
        temp_first = False
        init()


def start():
    global screen
    global can_turn, is_fail, temp_first
    global current_level
    global x, y, dx, dy, face
    global player_health
    global pickaxe, holy_water, quake_scroll, tnt, magic_key
    while True:
        screen.blit(floor_image, (x, y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.mixer.music.stop()
                    temp_first = True
                    level.spawn_json()
                    level.load_json()
                    game_launch()
                if event.key == pygame.K_UP:
                    if can_turn:
                        face = 2
                        level.config["floor"][current_level][dy - 1][dx - 1] = "floor"
                        y -= 64
                        dy -= 1
                if event.key == pygame.K_DOWN:
                    if can_turn:
                        face = 1
                        level.config["floor"][current_level][dy - 1][dx - 1] = "floor"
                        y += 64
                        dy += 1
                if event.key == pygame.K_LEFT:
                    if can_turn:
                        face = 3
                        level.config["floor"][current_level][dy - 1][dx - 1] = "floor"
                        x -= 64
                        dx -= 1
                if event.key == pygame.K_RIGHT:
                    if can_turn:
                        face = 4
                        level.config["floor"][current_level][dy - 1][dx - 1] = "floor"
                        x += 64
                        dx += 1
                if event.key == pygame.K_RETURN:  # 回车测试按钮
                    print(level.config["floor"])
                    print(str(x) + " " + str(y))
                if event.key == pygame.K_v:  # 查看怪物手册
                    pass
            if event.type == pygame.MOUSEBUTTONDOWN:  # 使用道具
                mouse = pygame.mouse.get_pos()
                mouse_left = mouse[0]
                mouse_top = mouse[1]
                if 896 < mouse_left < 960 and 256 < mouse_top < 320:
                    if holy_water:
                        h = (current_level + 1) * 1000
                        message("你使用了圣水，你恢复了" + str(h) + "的生命值。", False)
                        player_health += h
                        holy_water = False
                        update()
                if 960 < mouse_left < 1024 and 256 < mouse_top < 320:
                    if pickaxe:
                        if not dy >= 11 and level.config["floor"][current_level][dy][dx - 1] == "wall":
                            level.config["floor"][current_level][dy][dx - 1] = "floor"
                            screen.blit(floor_image, (x, y + 64))
                        if not dy <= 1 and level.config["floor"][current_level][dy - 2][dx - 1] == "wall":
                            level.config["floor"][current_level][dy - 2][dx - 1] = "floor"
                            screen.blit(floor_image, (x, y - 64))
                        if not dx >= 11 and level.config["floor"][current_level][dy - 1][dx] == "wall":
                            level.config["floor"][current_level][dy - 1][dx] = "floor"
                            screen.blit(floor_image, (x + 64, y))
                        if not dx <= 1 and level.config["floor"][current_level][dy - 1][dx - 2] == "wall":
                            level.config["floor"][current_level][dy - 1][dx - 2] = "floor"
                            screen.blit(floor_image, (x - 64, y))
                        message("你使用了镐子，破除了周围的墙壁。", False)
                        pickaxe = False
                        update()
                if 768 < mouse_left < 832 and 320 < mouse_top < 384:
                    if magic_key:
                        for i in range(0, len(level.config["floor"][current_level])):
                            for j in range(0, len(level.config["floor"][current_level][i])):
                                if "door" in level.config["floor"][current_level][i][j]:
                                    level.config["floor"][current_level][i][j] = "floor"
                                    screen.blit(floor_image, (32 + j * 64, 32 + i * 64))
                        message("你使用了魔法钥匙，现在这一层楼全部的门都已打开。", False)
                        magic_key = False
                        update()
                if 832 < mouse_left < 896 and 320 < mouse_top < 384:
                    if tnt:
                        if (not dy >= 11 and level.config["floor"][current_level][dy][dx - 1] in
                                level.config["monster"].keys()):
                            level.config["floor"][current_level][dy][dx - 1] = "floor"
                            screen.blit(floor_image, (x, y + 64))
                        if (not dy <= 1 and level.config["floor"][current_level][dy - 2][dx - 1] in
                                level.config["monster"].keys()):
                            level.config["floor"][current_level][dy - 2][dx - 1] = "floor"
                            screen.blit(floor_image, (x, y - 64))
                        if (not dx >= 11 and level.config["floor"][current_level][dy - 1][dx] in
                                level.config["monster"].keys()):
                            level.config["floor"][current_level][dy - 1][dx] = "floor"
                            screen.blit(floor_image, (x + 64, y))
                        if (not dx <= 1 and level.config["floor"][current_level][dy - 1][dx - 2] in
                                level.config["monster"].keys()):
                            level.config["floor"][current_level][dy - 1][dx - 2] = "floor"
                            screen.blit(floor_image, (x - 64, y))
                        message("你使用了炸弹，你周围的怪物被杀死了。", False)
                        tnt = False
                        update()
                if 896 < mouse_left < 960 and 320 < mouse_top < 384:
                    if quake_scroll:
                        for i in range(0, len(level.config["floor"][current_level])):
                            for j in range(0, len(level.config["floor"][current_level][i])):
                                if ("wall" in level.config["floor"][current_level][i][j] or
                                        "floor" in level.config["floor"][current_level][i][j]):
                                    level.config["floor"][current_level][i][j] = "floor"
                                    screen.blit(floor_image, (32 + j * 64, 32 + i * 64))
                        message("你使用了地震卷轴，现在这一层楼全部的墙都已被破坏。", False)
                        quake_scroll = False
                        update()
        player_move()
        draw_player()
        if is_fail:
            screen.blit(failed_image, (x, y))
            message("你输了，你打了不该打的怪物……按下回车键退出至标题……", True)
            pygame.mixer.music.stop()
            temp_first = True
            level.spawn_json()
            level.load_json()
            game_launch()
        pygame.display.flip()
        pygame.display.update()


if __name__ == '__main__':
    level.spawn_json()
    level.load_json()
    game_launch()
