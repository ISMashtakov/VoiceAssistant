from .command import Command
from windows_sound_manager.keyboard import Keyboard

NEXT_SONG = Command(
    ['Включи следующую песню', 'Дальше'],
    lambda: Keyboard.keyDown(Keyboard.VK_MEDIA_NEXT_TRACK), 'Следующая песня'
)

PREVIOUS_SONG = Command(
    ['Включи предыдущую песню', 'Назад'],
    lambda: Keyboard.keyDown(Keyboard.VK_MEDIA_PREV_TRACK), 'Предыдущая песня'
)

STOP = Command(
    ['Останови', 'Останови музыку', 'Поставь на паузу', 'Пауза'],
    lambda: Keyboard.keyDown(Keyboard.VK_MEDIA_STOP), 'Пауза'
)

ALL_COMMANDS = [NEXT_SONG, PREVIOUS_SONG, STOP]