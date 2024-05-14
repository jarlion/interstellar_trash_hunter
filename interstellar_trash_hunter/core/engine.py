import pygame
import sys

from interstellar_trash_hunter.setting.base import FPS, NAME, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_BGCOLOR
from interstellar_trash_hunter.view.ui.view import View


class Engine:

    def __init__(self, root: View):
        self.clock = pygame.time.Clock()

        self.root = root
        self.running = False
        # 初始化Pygame
        pygame.init()
        # 设置窗口大小
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # 设置标题
        pygame.display.set_caption(NAME)

    def start(self) -> None:
        self.running = True
        while self.running:
            for event in pygame.event.get():
                self.root.on_enter_frame(self.screen, self.root.rect)
                if event.type == pygame.QUIT:
                    self.running = False
                # elif event.type == pygame.MOUSEBUTTONDOWN:
                # if pygame.Rect(*START_BTN_POS, 200,
                # FONT_SIZE * 2).collidepoint(mouse_pos):
                #         print("开始游戏")
                #     elif pygame.Rect(*HELP_BTN_POS, 100,
                #                     FONT_SIZE * 2).collidepoint(mouse_pos):
                #         print("显示帮助")
                #     elif pygame.Rect(*EXIT_BTN_POS, 200,
                #                     FONT_SIZE * 2).collidepoint(mouse_pos):
                #         running = False
                elif is_mouse_event(event):
                    mouse_pos = pygame.mouse.get_pos()
                    self.root.capture(event, mouse_pos)

            # self.screen.fill(SCREEN_BGCOLOR)

            # # 绘制文本
            # draw_text(self.screen, "星际垃圾猎手", (400, 300))
            # draw_text(screen, "v0.0.1", VERSION_POS)
            # draw_text(screen, "by Jarlion", AUTHOR_POS)

            # # 绘制按钮（这里简化处理，实际应绘制矩形框和文字）
            # draw_text(screen, "开始游戏", START_BTN_POS)
            # pygame.draw.rect(screen, WHITE,
            #                 pygame.Rect(*PASSWORD_INPUT_POS, 200, FONT_SIZE),
            #                 2)  # 输入框边框
            # draw_text(screen, "请输入游戏密码", PASSWORD_INPUT_POS)
            # draw_text(screen, "帮助", HELP_BTN_POS)
            # draw_text(screen, "退出游戏", EXIT_BTN_POS)

            pygame.display.flip()
            self.clock.tick(FPS)

        self.stop()

    def stop(self) -> None:
        pygame.quit()
        sys.exit()


def is_mouse_event(event):
    return event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP
    # return event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEWHEEL


def draw_text(surface, text, position, color=(255, 255, 255)):
    font = pygame.font.Font(None, 36)

    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=position)
    surface.blit(text_obj, text_rect)
