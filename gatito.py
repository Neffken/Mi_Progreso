import subprocess

# Ejecuta el script en segundo plano con pythonw.exe (sin ventana)
subprocess.Popen(['pythonw', r'C:\Users\neffken\Desktop\2.py'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

import pygame
import random
import ctypes
import time
import sys
import win32gui
import win32con

# Inicializar pygame
pygame.init()

# Obtener el tamaño de la pantalla
user32 = ctypes.windll.user32
SCREEN_WIDTH, SCREEN_HEIGHT = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# Crear la ventana de Pygame sin bordes (esto es necesario pero se mantendrá invisible)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)

# Usar win32gui para hacer la ventana transparente
hwnd = pygame.display.get_wm_info()['window']
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32con.WS_EX_LAYERED | win32con.WS_EX_TOPMOST)
win32gui.SetLayeredWindowAttributes(hwnd, 0x000000, 0, win32con.LWA_COLORKEY)

# Crear un overlay transparente
overlay_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
overlay_surface.set_alpha(128)  # 128 es el nivel de transparencia (0-255)

# Cargar imagen del gatito
cat_img = pygame.image.load("C:/Users/neffken/Downloads/580b57fbd9996e24bc43bb8f.webp")
cat_img = pygame.transform.scale(cat_img, (50, 50))

# Lista de gatitos en pantalla
cats = [{'rect': cat_img.get_rect(), 'dx': 3, 'dy': 3}]
cats[0]['rect'].x = random.randint(0, SCREEN_WIDTH - 50)
cats[0]['rect'].y = random.randint(0, SCREEN_HEIGHT - 50)

# Temporizador para la duplicación
last_duplication_time = time.time()

# Bucle principal
running = True
while running:
    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener la posición actual del mouse
    mouse_pos = pygame.mouse.get_pos()

    # Limpiar pantalla con transparencia
    screen.fill((0, 0, 0, 0)) 

    # Actualizar posición de cada gatito
    for cat in cats:
        cat['rect'].x += cat['dx']
        cat['rect'].y += cat['dy']

        # Rebote en los bordes de la pantalla
        if cat['rect'].left <= 0 or cat['rect'].right >= SCREEN_WIDTH:
            cat['dx'] *= -1
        if cat['rect'].top <= 0 or cat['rect'].bottom >= SCREEN_HEIGHT:
            cat['dy'] *= -1

        # Verificar si el mouse toca el gatito y limitar duplicación
        if cat['rect'].collidepoint(mouse_pos) and time.time() - last_duplication_time > 0.3:
            last_duplication_time = time.time()  # Actualiza el tiempo de duplicación
            new_cat = {
                'rect': cat_img.get_rect(),
                'dx': random.choice([-3, 3]),
                'dy': random.choice([-3, 3])
            }
            # Ubica el nuevo gatito en una posición cercana al original para mayor efecto visual
            new_cat['rect'].x = cat['rect'].x + random.randint(-30, 30)
            new_cat['rect'].y = cat['rect'].y + random.randint(-30, 30)
            cats.append(new_cat)

        # Dibujar el gatito en pantalla
        screen.blit(cat_img, cat['rect'])

    # Actualizar la pantalla
    pygame.display.update()
    pygame.time.delay(30)

# Salir
pygame.quit()
sys.exit()
