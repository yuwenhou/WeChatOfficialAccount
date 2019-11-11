import sys
import random
import pygame
from pygame.locals import *

# 背景大小、颜色
WIDTH, HEIGHT = 640, 360
BACKGROUND = (255, 255, 255)
button_text_list = ['你再想想', '我养你','好吃的都给你', '保大','房产证给你', '我妈会游泳', '我会修电脑', '我会写代码']


# 按钮
def button(text, x, y, w, h, color, screen):
    pygame.draw.rect(screen, color, (x, y, w, h))
    font = pygame.font.Font('./font/ziti.ttf', 20)
    textRender = font.render(text, True, (0, 0, 0))
    textRect = textRender.get_rect()
    textRect.center = ((x + w / 2), (y + h / 2))
    screen.blit(textRender, textRect)


# 标题
def title(text, screen, scale, color=(0, 0, 0)):
    font = pygame.font.Font('./font/ziti.ttf', WIDTH // (len(text) * 2))
    textRender = font.render(text, True, color)
    textRect = textRender.get_rect()
    textRect.midtop = (WIDTH / scale[0], HEIGHT / scale[1])
    screen.blit(textRender, textRect)


# 生成随机的位置坐标
def get_random_pos():
    x, y = random.randint(20, WIDTH - 20), random.randint(20, HEIGHT - 20)
    return x, y


# 点击喜欢按钮后显示的页面
def show_like_interface(text, screen, color=(255, 0, 0)):
    screen.fill(BACKGROUND)
    font = pygame.font.Font('./font/simkai.ttf', WIDTH // (len(text)))
    textRender = font.render(text, True, color)
    textRect = textRender.get_rect()
    textRect.midtop = (WIDTH / 2, HEIGHT / 2)
    screen.blit(textRender, textRect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


# 主函数
def main():
    text = '算了吧'
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    pygame.display.set_caption('FROM一个喜欢你很久的小哥哥')
    clock = pygame.time.Clock()

    # 不喜欢按钮的初始位置和大小
    unlike_pos_x = 330
    unlike_pos_y = 250
    unlike_pos_width = 100
    unlike_pos_height = 50

    # 喜欢按钮的初始位置和大小
    like_pos_x = 180
    like_pos_y = 250
    like_pos_width = 100
    like_pos_height = 50
    running = True

    # 按钮颜色
    like_color = (216, 191, 216)

    # 若不点击喜欢按钮，就一直运行
    while running:
        screen.fill(BACKGROUND)

        # 加载图片
        img = pygame.image.load("./imgs/3.jpg")
        imgRect = img.get_rect()
        # 图片位置
        imgRect.midtop = 80, 10
        screen.blit(img, imgRect)

        # 监听事件
        for event in pygame.event.get():
            # 检测到鼠标
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 获取鼠标位置
                mouse_pos = pygame.mouse.get_pos()
                # 若点击了喜欢按钮，停止 while 循环
                if like_pos_x + like_pos_width > mouse_pos[0] > like_pos_x and \
                        like_pos_y + like_pos_height > mouse_pos[1] > like_pos_y:
                    like_color = BACKGROUND
                    running = False
        # 获取鼠标位置
        # 若鼠标位置位于按钮区域内
        # 则随机生成按钮位置进行显示
        mouse_pos = pygame.mouse.get_pos()
        if unlike_pos_x + unlike_pos_width > mouse_pos[0] > unlike_pos_x and \
                unlike_pos_y + unlike_pos_height > mouse_pos[1] > unlike_pos_y:
            while True:
                unlike_pos_x, unlike_pos_y = get_random_pos()
                text = button_text_list[random.randint(0, len(button_text_list) - 1)]
                if unlike_pos_x + unlike_pos_width > mouse_pos[0] > unlike_pos_x and \
                        unlike_pos_y + unlike_pos_height > mouse_pos[1] > unlike_pos_y:
                    continue
                break
        title('小姐姐，我观察你很久了', screen, scale=[1.8, 10])
        title('做我女朋友好不好呀?', screen, scale=[1.8, 3])
        button('好呀', like_pos_x, like_pos_y, like_pos_width,
               like_pos_height, like_color, screen)
        button(text, unlike_pos_x, unlike_pos_y, unlike_pos_width,
               unlike_pos_height, (216, 191, 216), screen)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)
    show_like_interface('我就知道小姐姐你也喜欢我~', screen, color=(0, 0, 0))


if __name__ == '__main__':
    main()
