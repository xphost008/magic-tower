# !/usr/bin/python3.10
# -*- coding: utf-8 -*-
# Copyright (C) 2023 Rechalow, Inc. All Rights Reserved
#
# @Time    : 2023/8/29
# @Author  : Rechalow
# @Email   : 273020451@qq.com
# @File    : main.py
# @Software: MagicTower

import pygame
from pygame.locals import *
import level

# 初始化pygame
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1024, 768))  # 设定窗口宽高为1024 x 768

pygame.display.set_caption("Magic Tower Remake 2 Fantastic Work!!")  # 设定窗口标题为此

player_health = 0  # 玩家生命
player_attack = 0  # 玩家攻击
player_defense = 0  # 玩家防御
player_money = 0  # 玩家金钱

yellow_key = 0  # 黄钥匙个数
blue_key = 0  # 蓝钥匙个数
red_key = 0  # 红钥匙个数
green_key = 0  # 绿钥匙个数

failed_image = pygame.image.load(".\\image\\boom.png")  # 死亡动画

player_face_image = pygame.image.load(".\\image\\player_face.png")  # 玩家正脸
player_left_image = pygame.image.load(".\\image\\player_left.png")  # 玩家左脸
player_right_image = pygame.image.load(".\\image\\player_right.png")  # 玩家右脸
player_back_image = pygame.image.load(".\\image\\player_back.png")  # 玩家背面

wall_image = pygame.image.load(".\\image\\wall.png")  # 墙壁
floor_image = pygame.image.load(".\\image\\floor.png")  # 地板
upstairs = pygame.image.load(".\\image\\upstairs.png")
downstairs = pygame.image.load(".\\image\\downstairs.png")

emerald_image = pygame.image.load(".\\image\\emerald.png")  # 绿宝石
sapphire_image = pygame.image.load(".\\image\\sapphire.png")  # 蓝宝石
topaz_image = pygame.image.load(".\\image\\topaz.png")  # 黄宝石
ruby_image = pygame.image.load(".\\image\\ruby.png")  # 红宝石

green_key_image = pygame.image.load(".\\image\\green_key.png")  # 绿钥匙
blue_key_image = pygame.image.load(".\\image\\blue_key.png")  # 蓝钥匙
yellow_key_image = pygame.image.load(".\\image\\yellow_key.png")  # 黄钥匙
red_key_image = pygame.image.load(".\\image\\red_key.png")  # 红钥匙

green_slime_image = pygame.image.load(".\\image\\green_slime.png")  # 绿色史莱姆
blue_slime_image = pygame.image.load(".\\image\\blue_slime.png")  # 蓝色史莱姆
red_slime_image = pygame.image.load(".\\image\\red_slime.png")  # 红色史莱姆
yellow_slime_image = pygame.image.load(".\\image\\yellow_slime.png")  # 黄色史莱姆

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

can_turn = True  # 玩家此时是否可以行走
is_exit = False  # 是否直接退出游戏
is_fail = False  # 是否失败

current_level = 0  # 当前楼层
face = 1  # 玩家朝向【1：前、2：后、3：左、4：右】

x = 0  # 当前走过的横坐标真实值
y = 0  # 当前走过的纵坐标真实值
dx = 0  # 当前走过的横坐标比例值
dy = 0  # 当前走过的纵坐标比例值

help_page = 0


def match_face():
    """
    匹配玩家的朝向，从而判定此时是否是墙壁
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


def reduce_hp(own_attack: int, own_defense: int, enemy_attack: int, enemy_defense: int, enemy_hp: int):
    """
    :param own_attack: 己方攻击
    :param own_defense: 己方防御
    :param enemy_attack: 敌方攻击
    :param enemy_defense: 敌方防御
    :param enemy_hp: 敌方血量
    :return: 己方克除血量
    """
    if enemy_attack <= own_defense:
        return 0
    red = (round(enemy_hp / (own_attack - enemy_defense))) * (enemy_attack - own_defense)
    if red < 0:
        red = 0
    return red


def update_level(lvl: int):
    """
    :param lvl: 层数
    :return:
    """
    global screen
    global font_level
    surface = pygame.Surface((256, 52))
    surface.fill((192, 192, 192))
    screen.blit(surface, (768, 0))
    text = font_level.render("第" + str(lvl + 1) + "层", True, (0, 0, 0))
    screen.blit(text, (768, 0))


def update_prop():
    global screen
    surface = pygame.Surface((256, 256))
    surface.fill((192, 192, 192))
    screen.blit(surface, (768, 256))
    pygame.draw.rect(screen, (0, 0, 0), ((768, 256), (256, 256)), width=10)


def help_message(text: str):
    """
    :param text: 帮助文本
    :return:
    """
    global screen
    surface = pygame.Surface((960, 604))
    surface.fill((192, 192, 192))
    screen.blit(surface, (32, 32))
    pygame.draw.rect(screen, (0, 190, 190), ((32, 32), (960, 604)), width=10)
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
        text = font_help.render(lines[i], True, (0, 0, 0))
        screen.blit(text, (46, 42 + 28 * i))


def message(text: str, is_lock: bool):
    """
    :param text: 信息框文本【自动换行】。
    :param is_lock: 是否锁住屏幕
    :return: 无
    """
    global can_turn
    global screen
    global is_exit
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
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    # is_exit = True
                    # running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        screen.blit(surface, (768, 512))
                        pygame.draw.rect(screen, (0, 0, 0), ((768, 512), (256, 256)), width=10)
                        running = False
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
    text_defense = font_attribute.render("防御：" + str(player_defense), True, (0, 0, 0))
    text_money = font_attribute.render("金钱：" + str(player_money), True, (0, 0, 0))
    screen.blit(text_health, (772, 52))
    screen.blit(text_attack, (772, 76))
    screen.blit(text_defense, (772, 100))
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
    update_level(current_level)
    update_prop()
    update_attribute()
    update_key()


def player_move():
    """
    玩家移动，通过全局变量控制，无需参数
    """
    global player_health, player_attack, player_defense, player_money
    global red_key, blue_key, green_key, yellow_key
    global is_fail, can_turn, current_level
    global x, y, dx, dy
    if is_fail:
        return
    x = max(32, min(672, x))
    y = max(32, min(672, y))
    dx = max(1, min(11, dx))
    dy = max(1, min(11, dy))
    lvl = level.floor[current_level]
    match face:
        case 1:
            if lvl[dy - 1][dx - 1] == "wall":
                y -= 64
                dy -= 1
                return
        case 2:
            if lvl[dy - 1][dx - 1] == "wall":
                y += 64
                dy += 1
                return
        case 3:
            if lvl[dy - 1][dx - 1] == "wall":
                x += 64
                dx += 1
                return
        case 4:
            if lvl[dy - 1][dx - 1] == "wall":
                x -= 64
                dx -= 1
                return

    for key in level.monster.keys():
        if lvl[dy - 1][dx - 1] == key:
            if player_attack < int(level.monster[key]["defense"]):
                message("无法击打" + key, False)
                match_face()
                return
            player_health -= reduce_hp(player_attack, player_defense, int(level.monster[key]["attack"]),
                                       int(level.monster[key]["defense"]), int(level.monster[key]["health"]))
            player_money += int(level.monster[key]["money"])
            message("你战胜了" + key + "，金钱+" + str(level.monster[key]["money"]), False)
    # if lvl[dy - 1][dx - 1] == "slime":
    #     if player_attack < 10:
    #         return x, y, dx, dy
    #     player_health -= reduce_hp(player_attack, player_defense, 10, 10, 30)
    #     player_money += 5
    #     message("你战胜了史莱姆，金钱 + 5")
    #     can_turn = True
    if lvl[dy - 1][dx - 1] == "topaz":
        player_money += 20
        message("你吃掉了黄宝石，金钱+20", False)
    if lvl[dy - 1][dx - 1] == "sapphire":
        player_defense += 5
        message("你吃掉了蓝宝石，防御+5", False)
    if lvl[dy - 1][dx - 1] == "ruby":
        player_attack += 5
        message("你吃掉了红宝石，攻击+5", False)
    if lvl[dy - 1][dx - 1] == "emerald":
        player_health += 200
        message("你吃掉了绿宝石，生命+200", False)
    if lvl[dy - 1][dx - 1] == "yellow-key":
        yellow_key += 1
        message("你得到了黄钥匙", False)
    if lvl[dy - 1][dx - 1] == "blue-key":
        blue_key += 1
        message("你得到了蓝钥匙", False)
    if lvl[dy - 1][dx - 1] == "green-key":
        green_key += 1
        message("你得到了绿钥匙", False)
    if lvl[dy - 1][dx - 1] == "red-key":
        red_key += 1
        message("你得到了红钥匙", False)

    if lvl[dy - 1][dx - 1] == "yellow-door":
        if yellow_key < 1:
            message("黄钥匙不够", False)
            match_face()
            return
        else:
            message("你打开了黄门", False)
            yellow_key -= 1
    if lvl[dy - 1][dx - 1] == "blue-door":
        if blue_key < 1:
            message("蓝钥匙不够", False)
            match_face()
            return
        else:
            message("你打开了蓝门", False)
            blue_key -= 1
    if lvl[dy - 1][dx - 1] == "red-door":
        if red_key < 1:
            message("红钥匙不够", False)
            match_face()
            return
        else:
            message("你打开了红门", False)
            red_key -= 1
    if lvl[dy - 1][dx - 1] == "green-door":
        if green_key < 1:
            message("绿钥匙不够", False)
            match_face()
            return
        else:
            message("你打开了绿门", False)
            green_key -= 1
    if lvl[dy - 1][dx - 1] == "upstairs":
        match_face()
        lvl[dy - 1][dx - 1] = "player"
        level.floor[current_level] = lvl
        current_level += 1
        if current_level >= len(level.floor) - 1:
            current_level = len(level.floor) - 1
        initFloor()
        message("上到：" + str(current_level + 1) + "层", False)
        return
    if lvl[dy - 1][dx - 1] == "downstairs":
        match_face()
        lvl[dy - 1][dx - 1] = "player"
        level.floor[current_level] = lvl
        current_level -= 1
        if current_level <= 0:
            current_level = 0
        initFloor()
        message("下到：" + str(current_level + 1) + "层", False)
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
    level.floor[current_level] = lvl
    return


def draw_button(txt: str, b: tuple[int, int, int, int], lvl: tuple[int, int], c: tuple[int, int, int]):
    """
    :param txt: 按钮文字
    :param b: 【1：按钮宽度，2：按钮高度，3：按钮距左，4：按钮距上】
    :param lvl: 【1：文字距左，2：文字距上】
    :param c: 颜色
    :return: 无
    """
    surface = pygame.Surface((b[0], b[1]))
    surface.fill((192, 192, 192))
    screen.blit(surface, (b[2], b[3]))
    text = font_start_button.render(txt, True, (c[0], c[1], c[2]))
    screen.blit(text, (lvl[0], lvl[1]))
    pygame.draw.rect(screen, (c[0], c[1], c[2]), ((b[2], b[3]), (b[0], b[1])), width=10)


def game_help():
    global screen
    global is_exit
    global help_page
    screen.fill((192, 192, 192))
    help_message(level.help_page[help_page])
    if help_page != 0:
        draw_button("上一页", (200, 100, 32, 650), (77, 680), (0, 190, 190))
    draw_button("返回", (200, 100, 412, 650), (472, 680), (0, 190, 190))
    if help_page != len(level.help_page) - 1:
        draw_button("下一页", (200, 100, 792, 650), (837, 680), (0, 190, 190))
    running = True
    while running:
        if is_exit:
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_exit = True
            if event.type == pygame.MOUSEMOTION:
                mouse = pygame.mouse.get_pos()
                mouse_left = mouse[0]
                mouse_top = mouse[1]
                if help_page != 0:
                    if 650 <= mouse_top <= 750 and 32 <= mouse_left <= 232:
                        draw_button("上一页", (200, 100, 32, 650), (77, 680), (0, 190, 0))
                    else:
                        draw_button("上一页", (200, 100, 32, 650), (77, 680), (0, 190, 190))
                if 650 <= mouse_top <= 750 and 412 <= mouse_left <= 612:
                    draw_button("返回", (200, 100, 412, 650), (472, 680), (0, 190, 0))
                else:
                    draw_button("返回", (200, 100, 412, 650), (472, 680), (0, 190, 190))
                if help_page != len(level.help_page) - 1:
                    if 650 <= mouse_top <= 750 and 792 <= mouse_left <= 992:
                        draw_button("下一页", (200, 100, 792, 650), (837, 680), (0, 190, 0))
                    else:
                        draw_button("下一页", (200, 100, 792, 650), (837, 680), (0, 190, 190))
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                mouse_left = mouse[0]
                mouse_top = mouse[1]
                if help_page != 0:
                    if 650 <= mouse_top <= 750 and 32 <= mouse_left <= 232:
                        help_page -= 1
                        game_help()
                        running = False
                if help_page != len(level.help_page) - 1:
                    if 650 <= mouse_top <= 750 and 792 <= mouse_left <= 992:
                        help_page += 1
                        game_help()
                        running = False
                if 650 <= mouse_top <= 750 and 412 <= mouse_left <= 612:
                    game_launch()
                    running = False
        pygame.display.flip()
        pygame.display.update()


def game_launch():
    global screen
    global is_exit
    screen.fill((192, 192, 192))
    text_start_menu = font_start_menu.render("欢迎来到魔塔世界", True, (190, 10, 60))
    screen.blit(text_start_menu, (108, 128))
    draw_button("开始游戏", (200, 100, 400, 300), (430, 330), (0, 190, 190))
    draw_button("帮助", (200, 100, 400, 430), (460, 460), (0, 190, 190))
    running = True
    while running:
        if is_exit:
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_exit = True
            if event.type == pygame.MOUSEMOTION:
                mouse = pygame.mouse.get_pos()
                mouse_left = mouse[0]
                mouse_top = mouse[1]
                if 300 <= mouse_top <= 400 <= mouse_left <= 600:
                    draw_button("开始游戏", (200, 100, 400, 300), (430, 330), (0, 190, 0))
                else:
                    draw_button("开始游戏", (200, 100, 400, 300), (430, 330), (0, 190, 190))
                if 530 >= mouse_top >= 430 and 600 >= mouse_left >= 400:
                    draw_button("帮助", (200, 100, 400, 430), (460, 460), (0, 190, 0))
                else:
                    draw_button("帮助", (200, 100, 400, 430), (460, 460), (0, 190, 190))
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                mouse_left = mouse[0]
                mouse_top = mouse[1]
                if 300 <= mouse_top <= 400 <= mouse_left <= 600:
                    choose_level()
                    running = False
                if 530 >= mouse_top >= 430 and 600 >= mouse_left >= 400:
                    game_help()
                    running = False
        pygame.display.flip()
        pygame.display.update()
    pygame.quit()


def choose_level():
    global player_health, player_attack, player_defense, player_money
    global is_exit
    global screen
    screen.fill((192, 192, 192))
    pygame.draw.rect(screen, (0, 190, 190), ((400, 100), (200, 100)), 10)
    pygame.draw.rect(screen, (0, 190, 190), ((400, 230), (200, 100)), 10)
    pygame.draw.rect(screen, (0, 190, 190), ((400, 360), (200, 100)), 10)
    pygame.draw.rect(screen, (0, 190, 190), ((400, 490), (200, 100)), 10)
    text_cheat_button = font_start_button.render("作弊", True, (0, 190, 190))
    text_easy_button = font_start_button.render("简单", True, (0, 190, 190))
    text_normal_button = font_start_button.render("普通", True, (0, 190, 190))
    text_hard_button = font_start_button.render("困难", True, (0, 190, 190))
    screen.blit(text_cheat_button, (460, 130))
    screen.blit(text_easy_button, (460, 260))
    screen.blit(text_normal_button, (460, 390))
    screen.blit(text_hard_button, (460, 520))
    running = True
    while running:
        if is_exit:
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_exit = True
            if event.type == pygame.MOUSEMOTION:
                mouse = pygame.mouse.get_pos()
                mouse_left = mouse[0]
                mouse_top = mouse[1]
                if 400 <= mouse_left <= 600 and 100 <= mouse_top <= 200:
                    draw_button("作弊", (200, 100, 400, 100), (460, 130), (0, 190, 0))
                else:
                    draw_button("作弊", (200, 100, 400, 100), (460, 130), (0, 190, 190))
                if 400 <= mouse_left <= 600 and 230 <= mouse_top <= 330:
                    draw_button("简单", (200, 100, 400, 230), (460, 260), (0, 190, 0))
                else:
                    draw_button("简单", (200, 100, 400, 230), (460, 260), (0, 190, 190))
                if 400 <= mouse_left <= 600 and 360 <= mouse_top <= 460:
                    draw_button("普通", (200, 100, 400, 360), (460, 390), (0, 190, 0))
                else:
                    draw_button("普通", (200, 100, 400, 360), (460, 390), (0, 190, 190))
                if 400 <= mouse_left <= 600 and 490 <= mouse_top <= 590:
                    draw_button("困难", (200, 100, 400, 490), (460, 520), (0, 190, 0))
                else:
                    draw_button("困难", (200, 100, 400, 490), (460, 520), (0, 190, 190))
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                mouse_left = mouse[0]
                mouse_top = mouse[1]
                if 400 <= mouse_left <= 600 and 100 <= mouse_top <= 200:
                    player_health = 9999999
                    player_attack = 9999999
                    player_defense = 9999999
                    player_money = 9999999
                    initFloor()
                    start()
                    running = False
                if 400 <= mouse_left <= 600 and 230 <= mouse_top <= 330:
                    player_health = 10000
                    player_attack = 50
                    player_defense = 50
                    player_money = 200
                    initFloor()
                    start()
                    running = False
                if 400 <= mouse_left <= 600 and 360 <= mouse_top <= 460:
                    player_health = 6000
                    player_attack = 30
                    player_defense = 30
                    player_money = 150
                    initFloor()
                    start()
                    running = False
                if 400 <= mouse_left <= 600 and 490 <= mouse_top <= 590:
                    player_health = 4000
                    player_attack = 20
                    player_defense = 15
                    player_money = 100
                    initFloor()
                    start()
                    running = False
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
    for i in range(0, len(level.floor[current_level])):
        for j in range(0, len(level.floor[current_level][i])):
            if level.floor[current_level][i][j] == "wall":
                screen.blit(wall_image, (32 + j * 64, 32 + i * 64))
            if level.floor[current_level][i][j] == "upstairs":
                screen.blit(upstairs, (32 + j * 64, 32 + i * 64))
            if level.floor[current_level][i][j] == "downstairs":
                screen.blit(downstairs, (32 + j * 64, 32 + i * 64))
            if level.floor[current_level][i][j] == "emerald":
                screen.blit(emerald_image, (32 + j * 64, 32 + i * 64))
            if level.floor[current_level][i][j] == "ruby":
                screen.blit(ruby_image, (32 + j * 64, 32 + i * 64))
            if level.floor[current_level][i][j] == "sapphire":
                screen.blit(sapphire_image, (32 + j * 64, 32 + i * 64))
            if level.floor[current_level][i][j] == "topaz":
                screen.blit(topaz_image, (32 + j * 64, 32 + i * 64))
            if level.floor[current_level][i][j] == "green-slime":
                screen.blit(green_slime_image, (32 + j * 64, 32 + i * 64))
            if level.floor[current_level][i][j] == "red-slime":
                screen.blit(red_slime_image, (32 + j * 64, 32 + i * 64))
            if level.floor[current_level][i][j] == "blue-slime":
                screen.blit(blue_slime_image, (32 + j * 64, 32 + i * 64))
            if level.floor[current_level][i][j] == "yellow-slime":
                screen.blit(yellow_slime_image, (32 + j * 64, 32 + i * 64))
            if level.floor[current_level][i][j] == "red-key":
                screen.blit(red_key_image, (32 + j * 64, 32 + i * 64))
            if level.floor[current_level][i][j] == "blue-key":
                screen.blit(blue_key_image, (32 + j * 64, 32 + i * 64))
            if level.floor[current_level][i][j] == "green-key":
                screen.blit(green_key_image, (32 + j * 64, 32 + i * 64))
            if level.floor[current_level][i][j] == "yellow-key":
                screen.blit(yellow_key_image, (32 + j * 64, 32 + i * 64))
            if level.floor[current_level][i][j] == "red-door":
                screen.blit(red_door_image, (32 + j * 64, 32 + i * 64))
            if level.floor[current_level][i][j] == "blue-door":
                screen.blit(blue_door_image, (32 + j * 64, 32 + i * 64))
            if level.floor[current_level][i][j] == "green-door":
                screen.blit(green_door_image, (32 + j * 64, 32 + i * 64))
            if level.floor[current_level][i][j] == "yellow-door":
                screen.blit(yellow_door_image, (32 + j * 64, 32 + i * 64))
            if level.floor[current_level][i][j] == "player":
                screen.blit(player_face_image, (32 + j * 64, 32 + i * 64))
                dx = j + 1
                dy = i + 1
                x = (32 + j * 64)
                y = (32 + i * 64)


def init():
    global can_turn
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
    update()
    if temp_first:
        temp_first = False
        init()


def start():
    global screen
    global can_turn, is_exit, is_fail
    global current_level
    global x, y, dx, dy, face
    running = True
    while running:
        if is_exit:
            running = False
        screen.blit(floor_image, (x, y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if can_turn:
                        face = 2
                        level.floor[current_level][dy - 1][dx - 1] = "floor"
                        y -= 64
                        dy -= 1
                if event.key == pygame.K_DOWN:
                    if can_turn:
                        face = 1
                        level.floor[current_level][dy - 1][dx - 1] = "floor"
                        y += 64
                        dy += 1
                if event.key == pygame.K_LEFT:
                    if can_turn:
                        face = 3
                        level.floor[current_level][dy - 1][dx - 1] = "floor"
                        x -= 64
                        dx -= 1
                if event.key == pygame.K_RIGHT:
                    if can_turn:
                        face = 4
                        level.floor[current_level][dy - 1][dx - 1] = "floor"
                        x += 64
                        dx += 1
                if event.key == pygame.K_RETURN:
                    print(level.floor)
            if event.type == pygame.MOUSEBUTTONDOWN:  # 使用道具
                pass
        player_move()
        match face:
            case 1:
                screen.blit(player_face_image, (x, y))
            case 2:
                screen.blit(player_back_image, (x, y))
            case 3:
                screen.blit(player_left_image, (x, y))
            case 4:
                screen.blit(player_right_image, (x, y))
        if is_fail:
            screen.blit(failed_image, (x, y))
            message("你输了，你打了不该打的怪物……按下回车键退出游戏……", True)
            is_exit = True
        pygame.display.flip()
        pygame.display.update()


if __name__ == '__main__':
    game_launch()