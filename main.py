import os
os.environ['KIVY_AUDIO'] = 'sdl2'

from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

import math
import random
import wave
import struct
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.videoplayer import VideoPlayer
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.animation import Animation
from kivy.graphics import Color, Rectangle, Ellipse, RoundedRectangle, Line, Triangle, PushMatrix, PopMatrix, Rotate

Window.clearcolor = (0.05, 0.05, 0.1, 1)

# -----------------------------------------------------------------------------
# AUDIO GENERATOR & SOUND MANAGER
# -----------------------------------------------------------------------------
def generate_enhanced_audio():
    if not os.path.exists("click.wav"):
        try:
            with wave.open("click.wav", "w") as f:
                f.setnchannels(1)
                f.setsampwidth(2)
                f.setframerate(22050)
                frames = bytearray()
                for i in range(1200):
                    decay = (1.0 - (i / 1200.0)) ** 2
                    freq = 600 - (i * 0.3)
                    val = int(20000 * math.sin(2 * math.pi * freq * (i / 22050.0)) * decay)
                    frames.extend(struct.pack("<h", val))
                f.writeframes(frames)
        except Exception:
            pass

    if not os.path.exists("jump.wav"):
        try:
            with wave.open("jump.wav", "w") as f:
                f.setnchannels(1)
                f.setsampwidth(2)
                f.setframerate(22050)
                frames = bytearray()
                for i in range(3800):
                    t = i / 22050.0
                    freq = 350 + (t * 850)
                    val = int(18000 * math.sin(2 * math.pi * freq * t))
                    frames.extend(struct.pack("<h", val))
                f.writeframes(frames)
        except Exception:
            pass

    if not os.path.exists("squish.wav"):
        try:
            with wave.open("squish.wav", "w") as f:
                f.setnchannels(1)
                f.setsampwidth(2)
                f.setframerate(22050)
                frames = bytearray()
                for i in range(2500):
                    t = i / 22050.0
                    freq = 220 - (t * 150)
                    val = int(18000 * math.sin(2 * math.pi * freq * t) * (1.0 - t / 0.11))
                    frames.extend(struct.pack("<h", val))
                f.writeframes(frames)
        except Exception:
            pass

    if not os.path.exists("coin.wav"):
        try:
            with wave.open("coin.wav", "w") as f:
                f.setnchannels(1)
                f.setsampwidth(2)
                f.setframerate(22050)
                frames = bytearray()
                notes = [(987.77, 80), (1318.51, 200)]
                for freq, duration_ms in notes:
                    num_frames = int(22050 * (duration_ms / 1000.0))
                    for i in range(num_frames):
                        t = i / 22050.0
                        decay = 1.0 - (i / num_frames)
                        val = int(22000 * math.sin(2 * math.pi * freq * t) * decay)
                        frames.extend(struct.pack("<h", val))
                f.writeframes(frames)
        except Exception:
            pass

    if not os.path.exists("heartpop.wav"):
        try:
            with wave.open("heartpop.wav", "w") as f:
                f.setnchannels(1)
                f.setsampwidth(2)
                f.setframerate(22050)
                frames = bytearray()
                notes = [(523.25, 60), (659.25, 60), (783.99, 120)]
                for freq, duration_ms in notes:
                    num_frames = int(22050 * (duration_ms / 1000.0))
                    for i in range(num_frames):
                        t = i / 22050.0
                        decay = 1.0 - (i / num_frames)
                        val = int(20000 * math.sin(2 * math.pi * freq * t) * decay)
                        frames.extend(struct.pack("<h", val))
                f.writeframes(frames)
        except Exception:
            pass

    if not os.path.exists("gameover.wav"):
        try:
            with wave.open("gameover.wav", "w") as f:
                f.setnchannels(1)
                f.setsampwidth(2)
                f.setframerate(22050)
                frames = bytearray()
                notes = [300, 260, 220, 150]
                for note in notes:
                    for i in range(1500):
                        t = i / 22050.0
                        val = int(16000 * math.sin(2 * math.pi * note * t) * (1.0 - i / 1500.0))
                        frames.extend(struct.pack("<h", val))
                f.writeframes(frames)
        except Exception:
            pass

    if not os.path.exists("victory.wav"):
        try:
            with wave.open("victory.wav", "w") as f:
                f.setnchannels(1)
                f.setsampwidth(2)
                f.setframerate(22050)
                frames = bytearray()
                notes = [260, 330, 390, 520]
                for note in notes:
                    for i in range(1800):
                        t = i / 22050.0
                        val = int(16000 * math.sin(2 * math.pi * note * t) * (1.0 - i / 1800.0))
                        frames.extend(struct.pack("<h", val))
                f.writeframes(frames)
        except Exception:
            pass

    if not os.path.exists("scream.wav"):
        try:
            with wave.open("scream.wav", "w") as f:
                f.setnchannels(1)
                f.setsampwidth(2)
                f.setframerate(22050)
                frames = bytearray()
                for i in range(11025):
                    t = i / 22050.0
                    freq = 800 + 400 * math.sin(t * 30) + random.uniform(-100, 100)
                    decay = (1.0 - (i / 11025.0))
                    val = int(24000 * math.sin(2 * math.pi * freq * t) * decay)
                    frames.extend(struct.pack("<h", val))
                f.writeframes(frames)
        except Exception:
            pass

    if not os.path.exists("firework.wav"):
        try:
            with wave.open("firework.wav", "w") as f:
                f.setnchannels(1)
                f.setsampwidth(2)
                f.setframerate(22050)
                frames = bytearray()
                total_frames = 22050 * 2  # 2 seconds of sound
                for i in range(total_frames):
                    t = i / 22050.0
                    progress = i / total_frames
                    whistle = math.sin(2 * math.pi * (300 + t * 600) * t) * max(0.0, (0.3 - t)) * 8000
                    boom = random.uniform(-16000, 16000) * math.exp(-t * 4.0) * (1.0 if t < 0.5 else 0.3)
                    crackle = (random.uniform(-12000, 12000) if random.random() < 0.15 and t > 0.1 else 0.0)
                    val = int((whistle + boom + crackle) * 0.5)
                    frames.extend(struct.pack("<h", max(-32768, min(32767, val))))
                f.writeframes(frames)
        except Exception:
            pass

    if not os.path.exists("rain.wav"):
        try:
            with wave.open("rain.wav", "w") as f:
                f.setnchannels(1)
                f.setsampwidth(2)
                f.setframerate(22050)
                frames = bytearray()
                for i in range(22050 * 3):
                    val = int(random.uniform(-4000, 4000))
                    frames.extend(struct.pack("<h", val))
                f.writeframes(frames)
        except Exception:
            pass

    if not os.path.exists("thunder.wav"):
        try:
            with wave.open("thunder.wav", "w") as f:
                f.setnchannels(1)
                f.setsampwidth(2)
                f.setframerate(22050)
                frames = bytearray()
                for i in range(22050 * 2):
                    t = i / 22050.0
                    decay = (1.0 - (i / (22050 * 2.0)))
                    val = int(random.uniform(-16000, 16000) * math.sin(2 * math.pi * 55 * t) * decay)
                    frames.extend(struct.pack("<h", val))
                f.writeframes(frames)
        except Exception:
            pass

generate_enhanced_audio()

class SoundManager:
    bgm_sound = None
    rain_sound = None
    master_vol = 1.0
    sfx_vol = 1.0
    bgm_vol = 0.6
    
    _sound_cache = {}

    @classmethod
    def _play_sfx(cls, filename):
        if filename not in cls._sound_cache or cls._sound_cache[filename] is None:
            cls._sound_cache[filename] = SoundLoader.load(filename)
        
        snd = cls._sound_cache[filename]
        if snd:
            if snd.state == 'play':
                snd.stop()
            snd.volume = cls.master_vol * cls.sfx_vol
            snd.play()

    @classmethod
    def play_click(cls):
        cls._play_sfx("click.wav")

    @classmethod
    def play_jump(cls):
        cls._play_sfx("jump.wav")

    @classmethod
    def play_squish(cls):
        cls._play_sfx("squish.wav")

    @classmethod
    def play_coin(cls):
        cls._play_sfx("coin.wav")

    @classmethod
    def play_heartpop(cls):
        cls._play_sfx("heartpop.wav")

    @classmethod
    def play_gameover(cls):
        cls._play_sfx("gameover.wav")

    @classmethod
    def play_victory(cls):
        cls._play_sfx("victory.wav")

    @classmethod
    def play_scream(cls):
        cls._play_sfx("scream.wav")

    @classmethod
    def play_firework(cls):
        cls._play_sfx("firework.wav")

    @classmethod
    def play_thunder(cls):
        cls._play_sfx("thunder.wav")

    @classmethod
    def start_bgm(cls, level_num=1):
        audio_file = None
        for ext in [".wav", ".mp3", ".ogg"]:
            if os.path.exists("bgmusic" + ext):
                audio_file = "bgmusic" + ext
                break

        if audio_file:
            if not cls.bgm_sound:
                cls.bgm_sound = SoundLoader.load(audio_file)
                if cls.bgm_sound:
                    cls.bgm_sound.loop = True
                    cls.bgm_sound.volume = cls.master_vol * cls.bgm_vol
                    cls.bgm_sound.play()
            elif cls.bgm_sound.state != 'play':
                cls.bgm_sound.play()

        if level_num == 5:
            if not cls.rain_sound and os.path.exists("rain.wav"):
                cls.rain_sound = SoundLoader.load("rain.wav")
            if cls.rain_sound:
                cls.rain_sound.loop = True
                cls.rain_sound.volume = cls.master_vol * cls.sfx_vol * 0.8
                if cls.rain_sound.state != 'play':
                    cls.rain_sound.play()
        else:
            cls.stop_rain()

    @classmethod
    def stop_rain(cls):
        if cls.rain_sound:
            cls.rain_sound.stop()
            cls.rain_sound = None

    @classmethod
    def stop_bgm(cls):
        if cls.bgm_sound:
            cls.bgm_sound.stop()
            cls.bgm_sound = None
        cls.stop_rain()

    @classmethod
    def update_volumes(cls):
        if cls.bgm_sound:
            cls.bgm_sound.volume = cls.master_vol * cls.bgm_vol
        if cls.rain_sound:
            cls.rain_sound.volume = cls.master_vol * cls.sfx_vol * 0.8

# -----------------------------------------------------------------------------
# UI COMPONENTS
# -----------------------------------------------------------------------------
class StylizedMenuButton(Button):
    def __init__(self, text="", **kwargs):
        super().__init__(text=text, **kwargs)
        self.background_color = (0, 0, 0, 0)
        self.background_normal = ''
        self.color = (1, 1, 1, 1)
        self.bold = True
        self.font_size = '22sp'
        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.05, 0.25, 0.05, 0.9)
            RoundedRectangle(pos=(self.x - 3, self.y - 3), size=(self.width + 6, self.height + 6), radius=[12])
            Color(0.1, 0.45, 0.1, 0.95)
            RoundedRectangle(pos=(self.x - 1, self.y - 1), size=(self.width + 2, self.height + 2), radius=[10])
            Color(0.2, 0.75, 0.25, 0.95)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[8])
            Color(1, 1, 1, 0.25)
            RoundedRectangle(pos=(self.x, self.y + self.height * 0.5), size=(self.width, self.height * 0.5), radius=[8, 8, 0, 0])

class TouchControlButton(Button):
    def __init__(self, text="", **kwargs):
        super().__init__(text=text, **kwargs)
        self.background_color = (0, 0, 0, 0)
        self.background_normal = ''
        self.text = ""
        self.raw_text = text
        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        self.canvas.before.clear()
        dim = min(self.width, self.height)
        cx, cy = self.center_x, self.center_y
        
        with self.canvas.before:
            Color(0, 0, 0, 0.25)
            Ellipse(pos=(cx - dim * 0.48, cy - dim * 0.52), size=(dim * 0.96, dim * 0.96))
            
            Color(1, 1, 1, 0.85)
            Line(circle=(cx, cy, dim * 0.46), width=2.5)

            Color(1, 1, 1, 0.95)
            t = self.raw_text.upper()
            if t == "<":
                Triangle(points=[cx + dim * 0.15, cy + dim * 0.25, cx + dim * 0.15, cy - dim * 0.25, cx - dim * 0.2, cy])
            elif t == ">":
                Triangle(points=[cx - dim * 0.15, cy + dim * 0.25, cx - dim * 0.15, cy - dim * 0.25, cx + dim * 0.2, cy])
            elif t == "JUMP":
                Triangle(points=[cx - dim * 0.2, cy, cx + dim * 0.2, cy, cx, cy + dim * 0.28])
                Rectangle(pos=(cx - dim * 0.22, cy - dim * 0.28), size=(dim * 0.44, dim * 0.18))
            elif t == "CROUCH":
                Triangle(points=[cx - dim * 0.2, cy, cx + dim * 0.2, cy, cx, cy - dim * 0.28])
                Rectangle(pos=(cx - dim * 0.22, cy + dim * 0.1), size=(dim * 0.44, dim * 0.18))

# -----------------------------------------------------------------------------
# GAME HUD
# -----------------------------------------------------------------------------
class GameHUD(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lives = 3
        self.coins = 0
        self.size_hint = (1, None)
        self.height = 70
        self.pos_hint = {'top': 1, 'x': 0}
        self.bind(pos=self.draw_hud, size=self.draw_hud)

    def set_stats(self, lives, coins):
        self.lives = lives
        self.coins = coins
        self.draw_hud()

    def draw_hud(self, *args):
        self.canvas.clear()
        hud_top = Window.height - 10
        with self.canvas:
            for i in range(3):
                h_x = Window.width - 140 + (i * 38)
                if i < self.lives:
                    Color(0.95, 0.15, 0.15, 1)
                else:
                    Color(0.25, 0.25, 0.25, 0.6)
                Ellipse(pos=(h_x, hud_top - 20), size=(14, 14))
                Ellipse(pos=(h_x + 12, hud_top - 20), size=(14, 14))
                Rectangle(pos=(h_x + 3, hud_top - 32), size=(20, 15))

# -----------------------------------------------------------------------------
# GAME ENGINE & ANIMATION GRAPHICS
# -----------------------------------------------------------------------------
class GameEngine(Widget):
    def __init__(self, app_ref, level_num=1, **kwargs):
        super().__init__(**kwargs)
        self.app = app_ref
        self.level = level_num
        self.is_paused = False
        self.anim_time = 0.0

        self.lives = 3
        self.invincible_timer = 0.0

        self.gravity = 0.85
        self.base_ground_y = 110
        self.player_x = 80
        self.player_y = self.base_ground_y
        self.velocity_y = 0
        self.is_grounded = True
        self.is_crouching = False
        self.is_holding_jump = False
        self.jump_frames = 0
        
        self.last_jump_time = 0.0
        self.has_double_jumped = False
        self._prev_jump_state = False
        
        self.key_left = False
        self.key_right = False
        self.moving_dir = 0
        self.facing_right = True
        self.camera_x = 0

        self.entering_pipe = False
        self.pipe_enter_progress = 0.0
        self.active_pipe = None
        self.pipe_sequence_stage = 0

        self.is_falling_in_pit = False
        self.pit_fall_timer = 0.0

        self.headstart_timer = 5.0
        self.boss_active = False
        self.boss_x = -300.0
        self.boss_y = self.base_ground_y

        self.end_sequence_state = 'none'
        self.flag_cloth_y = self.base_ground_y + 240
        self.flag_x = 3500 + (self.level * 600)
        self.castle_x = self.flag_x + 180

        self.enemies = []
        self.coins = []
        self.platforms = []
        self.stairs = []
        self.pipes = []
        self.ground_segments = []
        self.clouds = []
        self.buildings = []
        self.flowers = []
        self.raindrops = []
        self.fireworks = []
        self.thunder_timer = 0.0
        self.flash_alpha = 0.0

        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        if self._keyboard:
            self._keyboard.bind(on_key_down=self._on_key_down, on_key_up=self._on_key_up)

        self.textures = {}
        model_files = {
            'mario': 'mario.png',
            'mariocrouch': 'mariocrouch.png',
            'mushroom': 'mushroom.png',
            'turtle': 'turtle.png',
            'coin': 'coin.png',
            'flower': 'flower.png',
            'castle': 'castle.png',
            'flag': 'flag.png',
            'boss': '5boss.png'
        }
        for key, fname in model_files.items():
            if os.path.exists(fname):
                try:
                    self.textures[key] = Image(source=fname).texture
                except Exception:
                    self.textures[key] = None
            else:
                self.textures[key] = None

        self.setup_world()

    def _keyboard_closed(self):
        if self._keyboard:
            self._keyboard.unbind(on_key_down=self._on_key_down, on_key_up=self._on_key_up)
            self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        key = keycode[1]
        if key in ('left', 'a'):
            self.key_left = True
        elif key in ('right', 'd'):
            self.key_right = True
        elif key in ('up', 'w', 'space'):
            self.is_holding_jump = True
        elif key in ('down', 's'):
            self.is_crouching = True
        self.update_moving_dir()
        return True

    def _on_key_up(self, keyboard, keycode):
        key = keycode[1]
        if key in ('left', 'a'):
            self.key_left = False
        elif key in ('right', 'd'):
            self.key_right = False
        elif key in ('up', 'w', 'space'):
            self.is_holding_jump = False
        elif key in ('down', 's'):
            self.is_crouching = False
        self.update_moving_dir()
        return True

    def update_moving_dir(self):
        if self.key_left and not self.key_right:
            self.moving_dir = -1
        elif self.key_right and not self.key_left:
            self.moving_dir = 1
        else:
            self.moving_dir = 0

    def get_ground_y_at(self, x_pos):
        for seg in self.ground_segments:
            if seg['start_x'] <= x_pos <= seg['end_x']:
                return seg['y']
        return -999.0

    def setup_world(self):
        random.seed(self.level * 9999 + 42)

        level_themes = [
            (0.15, 0.45, 0.85, 1),
            (0.10, 0.10, 0.30, 1),
            (0.70, 0.30, 0.15, 1),
            (0.25, 0.05, 0.30, 1),
            (0.05, 0.25, 0.20, 1)
        ]
        self.sky_color = level_themes[(self.level - 1) % len(level_themes)]

        curr_x = 0
        while curr_x < self.flag_x + 300:
            pit_chance = 0.25 if self.level >= 3 else 0.05
            
            if self.level >= 3 and curr_x > 300 and random.random() < pit_chance:
                pit_width = random.randint(50, 90)
                curr_x += pit_width
            else:
                seg_width = random.randint(180, 320) if self.level >= 3 else random.randint(250, 450)
                if self.level >= 3:
                    seg_y = self.base_ground_y + random.choice([-30, 0, 35, 65, 90])
                else:
                    seg_y = self.base_ground_y
                
                self.ground_segments.append({
                    'start_x': curr_x,
                    'end_x': curr_x + seg_width,
                    'y': seg_y
                })
                curr_x += seg_width

        for i in range(30):
            self.buildings.append({
                'x': i * 220 + random.randint(-40, 40),
                'w': random.randint(110, 190),
                'h': random.randint(150, 500),
                'color': (0.15 + (self.level * 0.02), 0.2 + random.uniform(0.0, 0.2), 0.35 + random.uniform(0.0, 0.2), 0.85)
            })

        for i in range(40):
            self.clouds.append({
                'x': i * 160 + random.randint(-40, 40),
                'y': Window.height - random.randint(100, 220),
                'w': random.randint(130, 220),
                'h': random.randint(50, 75)
            })

        if self.level == 5:
            for i in range(120):
                self.raindrops.append({
                    'x': random.randint(0, int(Window.width * 2)),
                    'y': random.randint(0, int(Window.height)),
                    'len': random.randint(14, 26),
                    'speed': random.randint(18, 28)
                })
            self.boss_x = -300.0
            self.boss_y = self.base_ground_y
            self.headstart_timer = 5.0
            self.boss_active = False

        num_flowers = 12 + random.randint(0, 6)
        for i in range(num_flowers):
            fx = random.randint(150, int(self.flag_x - 300))
            gy = self.get_ground_y_at(fx)
            if gy > 0:
                self.flowers.append({
                    'x': fx,
                    'y': gy,
                    'offset': random.uniform(0, 6.28),
                    'color': random.choice([(1, 0.4, 0.7, 1), (1, 0.8, 0.2, 1), (0.4, 0.7, 1, 1)])
                })

        pipe_count = 2 + (self.level % 3)
        pipe_start_x = 400
        for i in range(pipe_count):
            px = pipe_start_x + i * random.randint(500, 800) + random.randint(-50, 50)
            if px < self.flag_x - 500:
                ph = 90 + ((i * 40 + self.level * 25) % 90)
                p_ground = self.get_ground_y_at(px)
                if p_ground > 0:
                    self.pipes.append({'x': px, 'y': p_ground, 'w': 90, 'h': ph})

        for i in range(6 + self.level * 2):
            gc_x = 300 + i * random.randint(250, 450)
            if gc_x < self.flag_x - 400:
                g_y = self.get_ground_y_at(gc_x)
                if g_y > 0:
                    self.coins.append({'x': gc_x, 'y': g_y + 10, 'collected': False})

        if self.level == 1:
            curr_x = 650
            while curr_x < self.flag_x - 700:
                p_w = max(110, 260)
                p_h = self.base_ground_y + random.choice([80, 140, 200])
                self.platforms.append({'x': curr_x, 'y': p_h, 'w': p_w, 'h': 34})

                for j in range(random.randint(2, 5)):
                    self.coins.append({'x': curr_x + (j * 32) + 15, 'y': p_h + 45, 'collected': False})

                curr_x += p_w + random.randint(140, 280)
        else:
            curr_x = 550
            climbing_y = self.base_ground_y + 110
            for chain in range(3 + self.level):
                p_w = random.randint(90, 140)
                climbing_y += random.randint(55, 80)
                self.platforms.append({'x': curr_x, 'y': climbing_y, 'w': p_w, 'h': 28})

                if random.random() > 0.3:
                    self.coins.append({'x': curr_x + p_w / 2 - 10, 'y': climbing_y + 40, 'collected': False})

                curr_x += p_w + random.randint(110, 180)

        stair_start_x = self.flag_x - 360
        num_steps = 4 + min(4, self.level)
        stair_base_y = self.get_ground_y_at(stair_start_x)
        if stair_base_y < 0:
            stair_base_y = self.base_ground_y
        for step in range(num_steps):
            step_w = 40
            step_h = (step + 1) * 36
            self.stairs.append({'x': stair_start_x + (step * step_w), 'y': stair_base_y, 'w': step_w, 'h': step_h})

        enemy_count = 3 + self.level * 2
        for i in range(enemy_count):
            ex = 600 + i * ((self.flag_x - 800) / enemy_count) + random.randint(-40, 40)
            e_ground = self.get_ground_y_at(ex)
            if e_ground > 0:
                self.enemies.append({
                    'type': 'mushroom',
                    'x': ex,
                    'y': e_ground,
                    'w': 34,
                    'h': 34,
                    'min_x': max(200, ex - random.randint(100, 220)),
                    'max_x': min(self.flag_x - 200, ex + random.randint(100, 220)),
                    'dir': 1 if i % 2 == 0 else -1,
                    'speed': 1.4 + (self.level * 0.35) + random.uniform(-0.2, 0.3),
                    'velocity_y': 0.0,
                    'is_grounded': True
                })

        if self.level >= 2:
            turtle_count = 1 + self.level
            for i in range(turtle_count):
                tx = 900 + i * 550 + random.randint(-50, 50)
                if tx < self.flag_x - 400:
                    t_ground = self.get_ground_y_at(tx)
                    if t_ground > 0:
                        self.enemies.append({
                            'type': 'turtle',
                            'x': tx,
                            'y': t_ground,
                            'w': 38,
                            'h': 44,
                            'min_x': max(300, tx - 180),
                            'max_x': min(self.flag_x - 200, tx + 180),
                            'dir': -1,
                            'speed': 1.8 + (self.level * 0.25),
                            'velocity_y': 0.0,
                            'is_grounded': True
                        })

        if self.level >= 3:
            flyer_count = 2 + (self.level - 2) * 2
            for i in range(flyer_count):
                fx = 800 + i * 450 + random.randint(-50, 50)
                if fx < self.flag_x - 300:
                    flyer_type = random.choice(['bird', 'wyvern'])
                    self.enemies.append({
                        'type': flyer_type,
                        'x': fx,
                        'y': self.base_ground_y + random.randint(150, 260),
                        'w': 42 if flyer_type == 'wyvern' else 32,
                        'h': 30 if flyer_type == 'wyvern' else 24,
                        'min_x': max(400, fx - 250),
                        'max_x': min(self.flag_x - 200, fx + 250),
                        'dir': 1 if i % 2 == 0 else -1,
                        'speed': 2.2 + (self.level * 0.3),
                        'sine_offset': random.uniform(0, 6.28),
                        'velocity_y': 0.0,
                        'is_grounded': False
                    })

        self.flag_cloth_y = self.base_ground_y + 240

    def update(self, dt):
        if self.is_paused:
            return

        self.anim_time += dt

        if self.level == 5 and self.end_sequence_state == 'none':
            if self.headstart_timer > 0:
                self.headstart_timer -= dt
                if self.headstart_timer <= 0:
                    self.headstart_timer = 0
                    self.boss_active = True
                    self.boss_x = self.player_x - 380
                    self.boss_y = self.player_y
            elif self.boss_active:
                dx = self.player_x - self.boss_x
                dy = self.player_y - self.boss_y
                dist = math.hypot(dx, dy)
                if dist > 1.0:
                    boss_screen_x = self.boss_x - self.camera_x
                    if boss_screen_x < 0 or dist > 450:
                        boss_speed = 12.5
                    elif dist < 120:
                        boss_speed = 2.0
                    else:
                        boss_speed = 3.2

                    self.boss_x += (dx / dist) * boss_speed
                    self.boss_y += (dy / dist) * boss_speed

        if self.level == 5 and self.end_sequence_state != 'none':
            if random.random() < 0.05:
                self.fireworks.append({
                    'x': random.randint(50, int(Window.width - 50)),
                    'y': random.randint(int(Window.height * 0.4), int(Window.height - 50)),
                    'timer': 1.0,
                    'color': (random.random(), random.random(), random.random(), 1)
                })
                SoundManager.play_firework()

        for fw in self.fireworks[:]:
            fw['timer'] -= dt
            if fw['timer'] <= 0:
                self.fireworks.remove(fw)

        if self.is_falling_in_pit:
            self.pit_fall_timer += dt
            self.player_y -= 8.0
            self.draw_scene()
            if self.player_y < -120 or self.pit_fall_timer > 2.0:
                Clock.unschedule(self.update)
                SoundManager.play_gameover()
                self.app.show_void_death_popup()
            return

        if self.level == 5:
            self.thunder_timer += dt
            if self.thunder_timer >= random.uniform(4.0, 8.0):
                self.thunder_timer = 0.0
                self.flash_alpha = 1.0
                SoundManager.play_thunder()

            if self.flash_alpha > 0:
                self.flash_alpha -= dt * 2.0

        if self.invincible_timer > 0:
            self.invincible_timer -= dt

        if self.entering_pipe:
            self.pipe_enter_progress += dt
            if self.pipe_sequence_stage == 0:
                if self.pipe_enter_progress >= 0.5:
                    self.pipe_sequence_stage = 1
                    self.pipe_enter_progress = 0.0
            elif self.pipe_sequence_stage == 1:
                if self.pipe_enter_progress >= 2.0:
                    self.pipe_sequence_stage = 2
                    self.pipe_enter_progress = 0.0
            elif self.pipe_sequence_stage == 2:
                if self.pipe_enter_progress >= 4.5 and self.pipe_sequence_stage != 3:
                    self.pipe_sequence_stage = 3
                    Clock.unschedule(self.update)
                    self.app.show_pipe_dide_popup(is_pipe=True)
            self.draw_scene()
            return

        if self.end_sequence_state != 'none':
            self.update_end_sequence()
            self.draw_scene()
            return

        for pipe in self.pipes:
            p_w = 36
            pipe_top = pipe['y'] + pipe['h']
            if self.is_crouching and self.is_grounded:
                if (self.player_x + p_w > pipe['x'] + 10) and (self.player_x < pipe['x'] + pipe['w'] - 10):
                    if abs(self.player_y - pipe_top) < 8:
                        self.entering_pipe = True
                        self.active_pipe = pipe
                        self.pipe_enter_progress = 0.0
                        self.pipe_sequence_stage = 0
                        self.player_x = pipe['x'] + (pipe['w'] - p_w) / 2
                        return

        for e in self.enemies:
            e['x'] += e['dir'] * e['speed']
            if e['type'] in ('bird', 'wyvern'):
                e['y'] += math.sin(self.anim_time * 5 + e.get('sine_offset', 0)) * 1.5
            else:
                e_ground = self.get_ground_y_at(e['x'] + e['w'] / 2)
                for p in self.platforms:
                    if (e['x'] + e['w'] > p['x']) and (e['x'] < p['x'] + p['w']):
                        plat_top = p['y'] + p['h']
                        if e['y'] >= plat_top - 15:
                            e_ground = max(e_ground, plat_top)

                if e_ground < 0 or e['y'] > e_ground + 5:
                    e['velocity_y'] -= self.gravity
                    e['y'] += e['velocity_y']
                    e['is_grounded'] = False
                
                if e_ground >= 0 and e['y'] <= e_ground:
                    e['y'] = e_ground
                    e['velocity_y'] = 0.0
                    e['is_grounded'] = True

            if e['x'] <= e['min_x']:
                e['x'] = e['min_x']
                e['dir'] = 1
            elif e['x'] >= e['max_x']:
                e['x'] = e['max_x']
                e['dir'] = -1

        if self.moving_dir != 0:
            self.facing_right = (self.moving_dir > 0)

        p_w, p_h = 36, (32 if self.is_crouching else 48)
        
        desired_x = self.player_x + (self.moving_dir * 4.5)

        for st in self.stairs:
            st_top = st['y'] + st['h']
            if self.player_y < st_top - 6:
                if (desired_x + p_w > st['x']) and (desired_x < st['x'] + st['w']):
                    if self.player_x + p_w <= st['x']:
                        desired_x = st['x'] - p_w
                    elif self.player_x >= st['x'] + st['w']:
                        desired_x = st['x'] + st['w']

        castle_w = 180 if self.textures.get('castle') else 140
        max_level_x = self.castle_x + castle_w - p_w
        self.player_x = max(0, min(desired_x, max_level_x))

        standing_surface = self.get_ground_y_at(self.player_x + p_w / 2)

        for pipe in self.pipes:
            if (self.player_x + p_w > pipe['x']) and (self.player_x < pipe['x'] + pipe['w']):
                pipe_top = pipe['y'] + pipe['h']
                if self.player_y >= pipe_top - 12:
                    standing_surface = max(standing_surface, pipe_top)

        for st in self.stairs:
            if (self.player_x + p_w > st['x']) and (self.player_x < st['x'] + st['w']):
                st_top = st['y'] + st['h']
                if self.player_y >= st_top - 12:
                    standing_surface = max(standing_surface, st_top)

        for p in self.platforms:
            if (self.player_x + p_w > p['x']) and (self.player_x < p['x'] + p['w']):
                plat_top = p['y'] + p['h']
                if self.player_y >= plat_top - 15:
                    standing_surface = max(standing_surface, plat_top)

        jump_pressed_edge = self.is_holding_jump and not self._prev_jump_state
        self._prev_jump_state = self.is_holding_jump

        if self.is_grounded:
            self.has_double_jumped = False
            if jump_pressed_edge and not self.is_crouching:
                self.velocity_y = 13.5
                self.is_grounded = False
                self.jump_frames = 0
                self.last_jump_time = self.anim_time
                SoundManager.play_jump()
        else:
            if jump_pressed_edge and not self.has_double_jumped:
                time_since_last_jump = self.anim_time - self.last_jump_time
                if time_since_last_jump <= 1.0:
                    self.velocity_y = 12.0
                    self.jump_frames = 0
                    self.has_double_jumped = True
                    SoundManager.play_jump()

        if self.is_holding_jump and self.velocity_y > 0 and self.jump_frames < 12:
            self.velocity_y += 0.35
            self.jump_frames += 1

        self.player_y += self.velocity_y
        
        if standing_surface < 0:
            if self.player_y <= self.base_ground_y - 20:
                self.is_falling_in_pit = True
                self.pit_fall_timer = 0.0
                self.draw_scene()
                return
            else:
                self.velocity_y -= self.gravity
                self.is_grounded = False
        else:
            if self.player_y > standing_surface:
                self.velocity_y -= self.gravity
                self.is_grounded = False
            else:
                self.player_y = standing_surface
                self.velocity_y = 0
                self.is_grounded = True
                self.has_double_jumped = False

        if self.level == 5 and self.boss_active:
            boss_rect = (self.boss_x, self.boss_y, 300, 300)
            p_rect_check = (self.player_x, self.player_y, p_w, p_h)
            if self.check_collision(p_rect_check, boss_rect):
                Clock.unschedule(self.update)
                SoundManager.play_gameover()
                self.app.trigger_boss_jumpscare_sequence()
                return

        target_camera_x = self.player_x - (Window.width / 2)
        self.camera_x += (target_camera_x - self.camera_x) * 0.3

        p_rect = (self.player_x, self.player_y, p_w, p_h)
        for c in self.coins:
            if not c['collected']:
                c_rect = (c['x'], c['y'], 24, 24)
                if self.check_collision(p_rect, c_rect):
                    c['collected'] = True
                    SoundManager.play_coin()
                    self.app.update_coin_display(self.app.hud.coins + 1)

        for e in self.enemies:
            e_rect = (e['x'], e['y'], e['w'], e['h'])
            if self.check_collision(p_rect, e_rect):
                if self.velocity_y < 0 and self.player_y > e['y'] + (e['h'] * 0.4):
                    self.enemies.remove(e)
                    self.velocity_y = 10.0
                    SoundManager.play_squish()
                    break
                else:
                    if self.invincible_timer <= 0:
                        self.lives -= 1
                        self.app.hud.set_stats(self.lives, self.app.hud.coins)
                        SoundManager.play_heartpop()
                        
                        if self.lives <= 0:
                            Clock.unschedule(self.update)
                            SoundManager.play_gameover()
                            self.app.show_pipe_dide_popup(is_pipe=False)
                            return
                        else:
                            self.invincible_timer = 2.5
                            self.velocity_y = 8.0
                            self.player_x -= (15 if self.facing_right else -15)
                    break

        pole_box = (self.flag_x - 12, self.base_ground_y, 45, 500)
        flag_cloth_box = (self.flag_x + 10, self.base_ground_y, 110, 500)
        if (self.check_collision(p_rect, pole_box) or self.check_collision(p_rect, flag_cloth_box)) and self.end_sequence_state == 'none':
            self.end_sequence_state = 'sliding'
            self.player_x = self.flag_x - 12
            self.flag_cloth_y = max(self.base_ground_y + 20, min(self.base_ground_y + 240, self.player_y + 10))

        self.draw_scene()

    def update_end_sequence(self):
        if self.end_sequence_state == 'sliding':
            if self.flag_cloth_y > self.base_ground_y + 20:
                self.flag_cloth_y -= 1.8
            if self.player_y > self.base_ground_y:
                self.player_y -= 1.8
            else:
                self.player_y = self.base_ground_y
                self.end_sequence_state = 'walking'

        elif self.end_sequence_state == 'walking':
            self.facing_right = True
            self.moving_dir = 1
            castle_w = 180 if self.textures.get('castle') else 140
            door_center = self.castle_x + (castle_w / 2) - 18
            fully_inside_target = door_center + 45
            
            if self.player_x < fully_inside_target:
                self.player_x += 1.5
            else:
                self.end_sequence_state = 'finished'
                SoundManager.play_victory()
                Clock.unschedule(self.update)
                self.app.on_level_clear(self.level)

    def check_collision(self, r1, r2):
        return not (r1[0] + r1[2] < r2[0] or r1[0] > r2[0] + r2[2] or r1[1] + r1[3] < r2[1] or r1[1] > r2[1] + r2[3])

    def draw_mario(self, px, py):
        if self.end_sequence_state == 'finished':
            return

        if self.invincible_timer > 0:
            if int(self.anim_time * 20) % 2 == 0:
                return

        with self.canvas:
            w_factor = -1.0 if not self.facing_right else 1.0

            if self.is_crouching:
                if self.textures.get('mariocrouch'):
                    tc = self.textures['mariocrouch']
                    Color(1, 1, 1, 1)
                    crouch_w = -w_factor
                    Rectangle(pos=(px + (36 if crouch_w < 0 else 0), py), size=(36 * crouch_w, 34), texture=tc)
                elif self.textures.get('mario'):
                    t = self.textures['mario']
                    tc = t.get_region(0, 0, t.width / 3, t.height * 0.7)
                    Color(1, 1, 1, 1)
                    Rectangle(pos=(px + (36 if w_factor < 0 else 0), py), size=(36 * w_factor, 34), texture=tc)
                else:
                    f_dir = 1 if self.facing_right else -1
                    head_y = py + 16
                    Color(0.85, 0.1, 0.1, 1)
                    Rectangle(pos=(px + 4 + (f_dir * 2), head_y), size=(26, 12))
                    Color(0.98, 0.8, 0.65, 1)
                    Rectangle(pos=(px + 6, py + 8), size=(22, 10))
                    Color(0.85, 0.1, 0.1, 1)
                    Rectangle(pos=(px + 5, py + 4), size=(24, 8))
                    Color(0.15, 0.25, 0.85, 1)
                    Rectangle(pos=(px + 7, py), size=(20, 6))
            else:
                if self.textures.get('mario'):
                    t = self.textures['mario']
                    if t.width >= t.height * 2:
                        frame = 0
                        if not self.is_grounded and self.end_sequence_state == 'none':
                            frame = 2
                        elif self.moving_dir != 0 or self.end_sequence_state != 'none':
                            frame = int(self.anim_time * 10) % 2 + 1
                        
                        tc = t.get_region(frame * (t.width / 3), 0, t.width / 3, t.height)
                        Color(1, 1, 1, 1)
                        Rectangle(pos=(px + (36 if w_factor < 0 else 0), py), size=(36 * w_factor, 48), texture=tc)
                    else:
                        Color(1, 1, 1, 1)
                        Rectangle(pos=(px + (36 if w_factor < 0 else 0), py), size=(36 * w_factor, 48), texture=t)
                else:
                    head_y = py + 34
                    Color(0.85, 0.1, 0.1, 1)
                    Rectangle(pos=(px + 4, head_y), size=(28, 14))
                    Color(0.98, 0.8, 0.65, 1)
                    Rectangle(pos=(px + 6, py + 20), size=(24, 14))
                    Color(0.85, 0.1, 0.1, 1)
                    Rectangle(pos=(px + 6, py + 10), size=(24, 12))
                    Color(0.15, 0.25, 0.85, 1)
                    Rectangle(pos=(px + 8, py + 2), size=(20, 12))

    def draw_enemies(self):
        with self.canvas:
            for e in self.enemies:
                ex = e['x'] - self.camera_x
                if ex < -80 or ex > Window.width + 80:
                    continue
                ey = e['y']

                if e['type'] == 'mushroom':
                    squish = abs(math.sin(self.anim_time * 8)) * 4
                    if self.textures.get('mushroom'):
                        Color(1, 1, 1, 1)
                        Rectangle(pos=(ex, ey), size=(e['w'], e['h'] - squish), texture=self.textures['mushroom'])
                    else:
                        Color(0.85, 0.15, 0.15, 1)
                        Ellipse(pos=(ex, ey + 10 - squish), size=(34, 24))
                        Color(1, 1, 1, 1)
                        Ellipse(pos=(ex + 13, ey + 20 - squish), size=(8, 8))
                        Color(0.95, 0.9, 0.8, 1)
                        Rectangle(pos=(ex + 7, ey), size=(20, 12 - squish))

                elif e['type'] == 'turtle':
                    t_step = math.sin(self.anim_time * 10) * 4
                    if self.textures.get('turtle'):
                        Color(1, 1, 1, 1)
                        Rectangle(pos=(ex, ey + abs(t_step)), size=(e['w'], e['h']), texture=self.textures['turtle'])
                    else:
                        Color(0.15, 0.75, 0.2, 1)
                        Ellipse(pos=(ex + 2, ey + 10), size=(34, 28))
                        Color(0.95, 0.85, 0.3, 1)
                        Ellipse(pos=(ex + (24 if e['dir'] > 0 else -2) + t_step, ey + 24), size=(16, 16))

                elif e['type'] == 'bird':
                    wing_flap = math.sin(self.anim_time * 15) * 8
                    Color(0.9, 0.4, 0.1, 1)
                    Ellipse(pos=(ex, ey + 4), size=(30, 20))
                    Color(1, 0.9, 0.2, 1)
                    Triangle(points=[ex + 28, ey + 14, ex + 38, ey + 10, ex + 28, ey + 6])
                    Color(0.8, 0.3, 0.05, 1)
                    Triangle(points=[ex + 10, ey + 14, ex + 18, ey + 24 + wing_flap, ex + 24, ey + 14])

                elif e['type'] == 'wyvern':
                    wing_flap = math.sin(self.anim_time * 12) * 12
                    Color(0.4, 0.15, 0.55, 1)
                    Ellipse(pos=(ex, ey + 6), size=(40, 22))
                    Color(0.9, 0.2, 0.2, 1)
                    Triangle(points=[ex + 34, ey + 16, ex + 48, ey + 12, ex + 34, ey + 8])
                    Color(0.3, 0.1, 0.45, 1)
                    Triangle(points=[ex + 12, ey + 16, ex + 22, ey + 32 + wing_flap, ex + 30, ey + 16])

    def draw_scene(self):
        self.canvas.clear()
        with self.canvas:
            if self.entering_pipe:
                if self.pipe_sequence_stage == 0:
                    Color(*self.sky_color)
                    Rectangle(pos=(0, 0), size=Window.size)
                    Color(0.15, 0.75, 0.2, 1)
                    p = self.active_pipe
                    px = p['x'] - self.camera_x
                    Rectangle(pos=(px, p['y']), size=(p['w'], p['h']))
                    Rectangle(pos=(px - 5, p['y'] + p['h'] - 26), size=(p['w'] + 10, 26))
                    return

                if self.pipe_sequence_stage == 1:
                    Color(0, 0, 0, 1)
                    Rectangle(pos=(0, 0), size=Window.size)
                    return

                if self.pipe_sequence_stage >= 2:
                    Color(0, 0, 0, 1)
                    Rectangle(pos=(0, 0), size=Window.size)

                    pipe_w, pipe_h = 240, 380
                    pipe_center_x = (Window.width - pipe_w) / 2
                    pipe_center_y = (Window.height - pipe_h) / 2

                    Color(0.02, 0.08, 0.03, 1)
                    Rectangle(pos=(pipe_center_x, pipe_center_y), size=(pipe_w, pipe_h))

                    Color(0.1, 0.6, 0.15, 1)
                    Rectangle(pos=(pipe_center_x - 12, pipe_center_y), size=(12, pipe_h))
                    Rectangle(pos=(pipe_center_x + pipe_w, pipe_center_y), size=(12, pipe_h))

                    spike_y = pipe_center_y
                    spike_width = 20
                    num_spikes = int(pipe_w / spike_width)
                    for s in range(num_spikes):
                        sx = pipe_center_x + s * spike_width
                        Color(0.75, 0.75, 0.8, 1)
                        Triangle(points=[sx, spike_y, sx + spike_width / 2, spike_y + 40, sx + spike_width, spike_y])

                    elapsed_fall = self.pipe_enter_progress
                    start_fall_y = pipe_center_y + pipe_h - 60
                    target_spike_y = spike_y + 35
                    
                    current_mario_y = max(target_spike_y, start_fall_y - (elapsed_fall * 90.0))
                    mario_w, mario_h = 45, 60
                    mario_x = pipe_center_x + (pipe_w - mario_w) / 2

                    if current_mario_y <= target_spike_y:
                        if not hasattr(self, '_scream_played') or not self._scream_played:
                            SoundManager.play_scream()
                            self._scream_played = True

                        Color(0.85, 0, 0, 0.9)
                        for b_particle in range(12):
                            bx_offset = math.sin(b_particle * 55) * (15 + (elapsed_fall * 30))
                            by_offset = math.cos(b_particle * 33) * (10 + (elapsed_fall * 25))
                            Ellipse(pos=(mario_x + mario_w/2 + bx_offset, target_spike_y + by_offset), size=(8, 8))
                        
                        Rectangle(pos=(pipe_center_x + 10, spike_y), size=(pipe_w - 20, 12))

                    if self.textures.get('mario'):
                        Color(1, 0.8, 0.8, 1)
                        Rectangle(pos=(mario_x, current_mario_y), size=(mario_w, mario_h), texture=self.textures['mario'])
                    else:
                        Color(0.85, 0.1, 0.1, 1)
                        Rectangle(pos=(mario_x, current_mario_y + 30), size=(mario_w, 20))
                        Color(0.98, 0.8, 0.65, 1)
                        Rectangle(pos=(mario_x + 5, current_mario_y + 12), size=(mario_w - 10, 18))
                        Color(0.15, 0.25, 0.85, 1)
                        Rectangle(pos=(mario_x + 5, current_mario_y), size=(mario_w - 10, 15))

                return

            Color(*self.sky_color)
            Rectangle(pos=(0, 0), size=Window.size)

            for c in self.clouds:
                cx = c['x'] - (self.camera_x * 0.15)
                if cx < -300 or cx > Window.width + 300:
                    continue
                cy = c['y']
                cw = c['w']
                ch = c['h']
                Color(1, 1, 1, 0.85)
                Ellipse(pos=(cx, cy), size=(cw, ch))
                Ellipse(pos=(cx + cw * 0.25, cy + ch * 0.35), size=(cw * 0.65, ch * 0.9))
                Ellipse(pos=(cx + cw * 0.5, cy - ch * 0.2), size=(cw * 0.5, ch * 0.8))

            for b in self.buildings:
                bx = b['x'] - (self.camera_x * 0.35)
                if bx < -300 or bx > Window.width + 300:
                    continue
                bw = b['w']
                bh = b['h']
                Color(*b['color'])
                Rectangle(pos=(bx, 0), size=(bw, self.base_ground_y + bh))

                cols = max(2, int(bw // 35))
                rows = max(3, int((bh + self.base_ground_y) // 50))
                col_w = bw / (cols + 1)
                row_h = (bh + self.base_ground_y - 30) / rows
                
                for r in range(rows):
                    for co in range(cols):
                        wx = bx + col_w * (co + 1) - 8
                        wy = 20 + row_h * r + 10
                        if (r + co) % 3 == 0:
                            Color(0.95, 0.85, 0.4, 0.8)
                        else:
                            Color(0.08, 0.12, 0.18, 0.85)
                        Rectangle(pos=(wx, wy), size=(14, 22))

            Color(0.35, 0.20, 0.08, 1)
            Rectangle(pos=(0, 0), size=(Window.width, self.base_ground_y - 20))

            for seg in self.ground_segments:
                gx = seg['start_x'] - self.camera_x
                if gx + (seg['end_x'] - seg['start_x']) < -100 or gx > Window.width + 100:
                    continue
                gw = seg['end_x'] - seg['start_x']
                gy = seg['y']

                Color(0.52, 0.32, 0.13, 1)
                Rectangle(pos=(gx, 0), size=(gw, gy - 14))
                
                Color(0.42, 0.24, 0.09, 0.7)
                for tx_i in range(int(gw // 45)):
                    t_spot_x = gx + (tx_i * 45) + 12
                    t_spot_y = (tx_i * 23) % (int(gy) - 25) + 8
                    Rectangle(pos=(t_spot_x, t_spot_y), size=(16, 10))

                Color(0.1, 0.75, 0.15, 1)
                Rectangle(pos=(gx, gy - 14), size=(gw, 14))
                Color(0.25, 0.9, 0.25, 1)
                Rectangle(pos=(gx, gy - 4), size=(gw, 4))

            for fl in self.flowers:
                fx = fl['x'] - self.camera_x
                if fx < -50 or fx > Window.width + 50:
                    continue
                sway = math.sin(self.anim_time * 3.5 + fl['offset']) * 4
                if self.textures.get('flower'):
                    Color(1, 1, 1, 1)
                    Rectangle(pos=(fx + sway, fl['y']), size=(18, 18), texture=self.textures['flower'])
                else:
                    Color(*fl['color'])
                    Ellipse(pos=(fx + sway, fl['y']), size=(12, 12))

            for st in self.stairs:
                sx = st['x'] - self.camera_x
                if sx < -100 or sx > Window.width + 100:
                    continue
                Color(0.65, 0.35, 0.15, 1)
                Rectangle(pos=(sx, st['y']), size=(st['w'], st['h']))
                
                Color(0.45, 0.22, 0.08, 0.85)
                for line_y in range(int(st['y']) + 8, int(st['y'] + st['h']), 12):
                    Rectangle(pos=(sx + 2, line_y), size=(st['w'] - 4, 3))
                for col_line in range(int(sx) + 10, int(sx + st['w']), 15):
                    Rectangle(pos=(col_line, st['y']), size=(2, st['h']))

            for pipe in self.pipes:
                px = pipe['x'] - self.camera_x
                if px < -120 or px > Window.width + 120:
                    continue
                py = pipe['y']
                pw = pipe['w']
                ph = pipe['h']
                
                Color(0.15, 0.75, 0.2, 1)
                Rectangle(pos=(px, py), size=(pw, ph))
                
                Color(0.25, 0.9, 0.3, 1)
                Rectangle(pos=(px + 8, py), size=(12, ph))
                
                Color(0.08, 0.45, 0.1, 1)
                Rectangle(pos=(px + pw - 14, py), size=(8, ph))

                Color(0.12, 0.65, 0.16, 1)
                Rectangle(pos=(px - 5, py + ph - 26), size=(pw + 10, 26))
                Color(0.3, 0.95, 0.35, 1)
                Rectangle(pos=(px - 5, py + ph - 6), size=(pw + 10, 6))

            for p in self.platforms:
                rx = p['x'] - self.camera_x
                if rx < -200 or rx > Window.width + 200:
                    continue
                pw = p['w']
                ph = p['h']
                
                Color(0.72, 0.42, 0.2, 1)
                Rectangle(pos=(rx, p['y']), size=(pw, ph))
                
                Color(0.52, 0.28, 0.1, 1)
                Rectangle(pos=(rx, p['y'] + ph * 0.5 - 2), size=(pw, 4))
                
                Color(0.4, 0.2, 0.06, 0.9)
                for bx_div in range(int(rx) + 25, int(rx + pw) - 10, 35):
                    Rectangle(pos=(bx_div, p['y']), size=(3, ph))
                
                Color(0.9, 0.9, 0.9, 0.9)
                Ellipse(pos=(rx + 4, p['y'] + ph - 8), size=(5, 5))
                Ellipse(pos=(rx + pw - 9, p['y'] + ph - 8), size=(5, 5))

            for c in self.coins:
                if not c['collected']:
                    cx = c['x'] - self.camera_x
                    if cx < -50 or cx > Window.width + 50:
                        continue
                    scale = abs(math.sin(self.anim_time * 6))
                    w = max(4, int(22 * scale))
                    if self.textures.get('coin'):
                        Color(1, 1, 1, 1)
                        Rectangle(pos=(cx + (22 - w) / 2, c['y']), size=(w, 24), texture=self.textures['coin'])
                    else:
                        Color(1, 0.85, 0.1, 1)
                        Ellipse(pos=(cx + (22 - w) / 2, c['y']), size=(w, 22))

            cx = self.castle_x - self.camera_x
            if -250 < cx < Window.width + 250:
                castle_w, castle_h = (180, 180) if self.textures.get('castle') else (140, 120)

                if self.textures.get('castle'):
                    Color(1, 1, 1, 1)
                    Rectangle(pos=(cx, self.base_ground_y), size=(castle_w, castle_h), texture=self.textures['castle'])
                else:
                    Color(0.5, 0.5, 0.55, 1)
                    Rectangle(pos=(cx, self.base_ground_y), size=(140, 120))
                    Rectangle(pos=(cx + 35, self.base_ground_y + 120), size=(70, 60))
                    Color(0.2, 0.1, 0.05, 1)
                    Rectangle(pos=(cx + 50, self.base_ground_y), size=(40, 60))

            fx = self.flag_x - self.camera_x
            if -150 < fx < Window.width + 150:
                Color(0.9, 0.9, 0.9, 1)
                Rectangle(pos=(fx, self.base_ground_y), size=(10, 280))
                Color(1, 0.85, 0.1, 1)
                Ellipse(pos=(fx - 5, self.base_ground_y + 275), size=(20, 20))

                fy = self.flag_cloth_y
                wave_flex = math.sin(self.anim_time * 6.0) * 12
                if self.textures.get('flag'):
                    Color(1, 1, 1, 1)
                    Rectangle(pos=(fx + 10, fy), size=(90 + wave_flex, 55), texture=self.textures['flag'])
                else:
                    Color(0.95, 0.15, 0.15, 1)
                    Rectangle(pos=(fx + 10, fy), size=(90 + wave_flex, 55))

            self.draw_enemies()
            
            if self.level == 5 and self.boss_active:
                bx = self.boss_x - self.camera_x
                if -350 < bx < Window.width + 350:
                    if self.textures.get('boss'):
                        Color(1, 1, 1, 1)
                        Rectangle(pos=(bx, self.boss_y), size=(300, 300), texture=self.textures['boss'])
                    else:
                        Color(0.8, 0.1, 0.8, 1)
                        Rectangle(pos=(bx, self.boss_y), size=(300, 300))

            self.draw_mario(self.player_x - self.camera_x, self.player_y)

            for fw in self.fireworks:
                Color(*fw['color'])
                f_size = (1.0 - fw['timer']) * 60
                Ellipse(pos=(fw['x'] - f_size/2, fw['y'] - f_size/2), size=(f_size, f_size))

            if self.level == 5:
                Color(0.7, 0.8, 1.0, 0.6)
                for drop in self.raindrops:
                    drop['y'] -= drop['speed']
                    drop['x'] -= 2
                    if drop['y'] < 0:
                        drop['y'] = Window.height + 20
                        drop['x'] = random.randint(0, int(Window.width * 2))
                    Rectangle(pos=(drop['x'] - (self.camera_x * 0.2), drop['y']), size=(2, drop['len']))

                if self.flash_alpha > 0:
                    Color(1, 1, 1, self.flash_alpha * 0.45)
                    Rectangle(pos=(0, 0), size=Window.size)

# -----------------------------------------------------------------------------
# ROTATED VIDEO CONTAINER WIDGET (CLEAN CROPPED & BAR-FREE)
# -----------------------------------------------------------------------------
class RotatedVideoWidget(FloatLayout):
    def __init__(self, source, angle=0, volume=0.7, eos_action='stop', on_eos=None, **kwargs):
        super().__init__(**kwargs)
        self.angle = angle
        self.on_eos = on_eos
        
        with self.canvas.before:
            PushMatrix()
            self.rot = Rotate(angle=self.angle, origin=(0, 0))
        with self.canvas.after:
            PopMatrix()
            
        self.bind(pos=self.update_origin, size=self.update_origin)
        
        try:
            self.vid_container = FloatLayout(size_hint=(1, 1.25), pos_hint={'x': 0, 'y': -0.25})
            self.video = VideoPlayer(source='', volume=volume, options={'eos': eos_action}, size_hint=(1, 1))
            try:
                self.video.remove_widget(self.video.controller)
            except Exception:
                pass

            self.video.bind(state=self.check_video_state)
            self.vid_container.add_widget(self.video)
            self.add_widget(self.vid_container)
            Clock.schedule_once(lambda dt: self.set_source_and_play(source), 0.1)
        except Exception:
            self.video = None

    def set_source_and_play(self, source):
        if self.video and os.path.exists(source):
            try:
                self.video.source = source
                self.video.state = 'play'
            except Exception:
                pass

    def check_video_state(self, instance, value):
        if value == 'stop' and self.video and self.video.position > 0:
            if self.on_eos:
                self.on_eos()

    def update_origin(self, *args):
        self.rot.origin = self.center

# -----------------------------------------------------------------------------
# APPLICATION CLASS & CONTROLS BINDING
# -----------------------------------------------------------------------------
class MarioGameApp(App):
    def build(self):
        self.title = "Mario(NPC.ver)"  # Add this line
        Clock.maxfps = 60
        self.max_unlocked_level = 5
        self.root_layout = FloatLayout()
        self.bg_texture = None
        self.active_popup = None
        self.polyester_timers = []
        self.spawned_videos = []

        if os.path.exists("background.jpg"):
            try:
                self.bg_texture = Image(source="background.jpg").texture
            except Exception:
                pass

        self.show_startup_loading_screen()
        return self.root_layout

    def show_startup_loading_screen(self):
        self.root_layout.clear_widgets()
        
        with self.root_layout.canvas:
            Color(0.02, 0.02, 0.05, 1)
            Rectangle(pos=(0, 0), size=Window.size)

        load_box = BoxLayout(orientation='vertical', size_hint=(None, None), size=(260, 260), spacing=15, pos_hint={'center_x': 0.5, 'center_y': 0.5})

        if os.path.exists("5boss.png"):
            img_boss = Image(source="5boss.png", size_hint=(None, None), size=(140, 140), pos_hint={'center_x': 0.5})
            load_box.add_widget(img_boss)
        else:
            lbl_fallback = Label(text="[5boss.png missing]", font_size='14sp', color=(1,1,1,1), size_hint=(None,None), size=(140,40))
            load_box.add_widget(lbl_fallback)

        lbl_studio = Label(text="syriSTUDIO", font_size='24sp', bold=True, color=(1, 1, 1, 1), size_hint=(None, None), size=(260, 40), pos_hint={'center_x': 0.5})
        load_box.add_widget(lbl_studio)

        self.root_layout.add_widget(load_box)

        Clock.schedule_once(lambda dt: self.show_main_menu(), 2.5)

    def apply_background(self):
        if self.bg_texture:
            bg_img = Image(texture=self.bg_texture, fit_mode='fill', pos_hint={'x': 0, 'y': 0}, size_hint=(1, 1))
            self.root_layout.add_widget(bg_img)

    def show_main_menu(self):
        SoundManager.stop_bgm()
        self.root_layout.clear_widgets()
        self.apply_background()

        menu_box = BoxLayout(orientation='vertical', size_hint=(None, None), size=(280, 310), spacing=14, pos_hint={'center_x': 0.5, 'center_y': 0.55})

        btn_play = StylizedMenuButton(text="PLAY")
        btn_play.bind(on_press=lambda i: (SoundManager.play_click(), self.load_level(1)))

        btn_levels = StylizedMenuButton(text="LEVELS")
        btn_levels.bind(on_press=lambda i: (SoundManager.play_click(), self.show_levels_menu(i)))

        btn_settings = StylizedMenuButton(text="SETTINGS")
        btn_settings.bind(on_press=lambda i: (SoundManager.play_click(), self.open_settings_menu(i)))

        btn_credits = StylizedMenuButton(text="CREDITS")
        btn_credits.bind(on_press=lambda i: (SoundManager.play_click(), self.open_credits_menu(i)))

        menu_box.add_widget(btn_play)
        menu_box.add_widget(btn_levels)
        menu_box.add_widget(btn_settings)
        menu_box.add_widget(btn_credits)

        syri_label = Label(text="Made by syri", font_size='26sp', bold=True, color=(1, 1, 1, 1), size_hint=(None, None), size=(200, 40), pos_hint={'center_x': 0.5, 'center_y': 0.15})

        self.root_layout.add_widget(menu_box)
        self.root_layout.add_widget(syri_label)

    def open_settings_menu(self, instance):
        content = BoxLayout(orientation='vertical', padding=15, spacing=15)

        content.add_widget(Label(text="Master Audio", font_size='14sp', bold=True, color=(1, 1, 1, 1)))
        slider_master = Slider(min=0, max=1, value=SoundManager.master_vol, size_hint_y=None, height=40)
        def on_master_change(inst, val):
            SoundManager.master_vol = val
            SoundManager.update_volumes()
        slider_master.bind(value=on_master_change)
        content.add_widget(slider_master)

        content.add_widget(Label(text="BG Music Audio", font_size='14sp', bold=True, color=(1, 1, 1, 1)))
        slider_bgm = Slider(min=0, max=1, value=SoundManager.bgm_vol, size_hint_y=None, height=40)
        def on_bgm_change(inst, val):
            SoundManager.bgm_vol = val
            SoundManager.update_volumes()
        slider_bgm.bind(value=on_bgm_change)
        content.add_widget(slider_bgm)

        content.add_widget(Label(text="SFX Audio", font_size='14sp', bold=True, color=(1, 1, 1, 1)))
        slider_sfx = Slider(min=0, max=1, value=SoundManager.sfx_vol, size_hint_y=None, height=40)
        def on_sfx_change(inst, val):
            SoundManager.sfx_vol = val
            SoundManager.update_volumes()
        slider_sfx.bind(value=on_sfx_change)
        content.add_widget(slider_sfx)

        btn_close = StylizedMenuButton(text="BACK")
        popup = Popup(title="Settings", content=content, size_hint=(None, None), size=(320, 360), auto_dismiss=False)
        btn_close.bind(on_press=lambda i: (SoundManager.play_click(), popup.dismiss()))
        content.add_widget(btn_close)
        
        popup.open()

    def open_credits_menu(self, instance):
        content = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        lbl_credit_text = Label(
            text="im syri yes syri is me yes i made it im not gay", 
            font_size='16sp', 
            bold=True, 
            color=(1, 1, 1, 1), 
            halign='center', 
            valign='middle'
        )
        lbl_credit_text.bind(size=lambda s, w: setattr(s, 'text_size', w))
        content.add_widget(lbl_credit_text)

        btn_close = StylizedMenuButton(text="BACK")
        popup = Popup(title="Credits", content=content, size_hint=(None, None), size=(340, 240), auto_dismiss=False)
        btn_close.bind(on_press=lambda i: (SoundManager.play_click(), popup.dismiss()))
        content.add_widget(btn_close)

        popup.open()

    def show_levels_menu(self, instance):
        self.root_layout.clear_widgets()
        self.apply_background()

        grid = GridLayout(cols=3, size_hint=(None, None), size=(420, 240), spacing=15, pos_hint={'center_x': 0.5, 'center_y': 0.55})

        for i in range(1, 6):
            btn = StylizedMenuButton(text=f"LEVEL {i}")
            if i <= self.max_unlocked_level:
                btn.bind(on_press=lambda inst, l=i: (SoundManager.play_click(), self.load_level(l)))
            else:
                btn.opacity = 0.5
            grid.add_widget(btn)

        btn_back = StylizedMenuButton(text="BACK", size_hint=(None, None), size=(180, 50), pos_hint={'center_x': 0.5, 'center_y': 0.2})
        btn_back.bind(on_press=lambda i: (SoundManager.play_click(), self.show_main_menu()))

        self.root_layout.add_widget(grid)
        self.root_layout.add_widget(btn_back)

    def load_level(self, level_num):
        self.clear_polyester_videos()
        self.root_layout.clear_widgets()
        SoundManager.start_bgm(level_num=level_num)

        self.engine = GameEngine(self, level_num=level_num)
        self.hud = GameHUD()
        self.hud.set_stats(3, 0)

        self.root_layout.add_widget(self.engine)
        self.root_layout.add_widget(self.hud)

        btn_pause = Button(text="||", size_hint=(None, None), size=(45, 45), pos_hint={'x': 0.02, 'top': 0.98}, bold=True)
        btn_pause.bind(on_press=lambda i: (SoundManager.play_click(), self.toggle_pause(i)))
        self.root_layout.add_widget(btn_pause)

        self.level_lbl = Label(text=f"LEVEL {level_num}", font_size='22sp', bold=True, color=(1, 1, 1, 1), size_hint=(None, None), size=(140, 30), pos_hint={'center_x': 0.5, 'top': 0.95})
        self.root_layout.add_widget(self.level_lbl)

        if level_num == 5:
            self.timer_lbl = Label(text="HEADSTART: 5.0s", font_size='18sp', bold=True, color=(1, 0.3, 0.3, 1), size_hint=(None, None), size=(200, 30), pos_hint={'center_x': 0.5, 'top': 0.88})
            self.root_layout.add_widget(self.timer_lbl)
            Clock.schedule_interval(self.update_headstart_hud, 0.1)

        self.coin_lbl = Label(text="COINS: 0", font_size='18sp', bold=True, color=(1, 0.85, 0.1, 1), size_hint=(None, None), size=(140, 30), pos_hint={'right': 0.98, 'top': 0.90})
        self.root_layout.add_widget(self.coin_lbl)

        self.setup_touch_controls()
        Clock.schedule_interval(self.engine.update, 1.0 / 60.0)

    def update_headstart_hud(self, dt):
        if hasattr(self, 'timer_lbl') and self.engine:
            if self.engine.headstart_timer > 0:
                self.timer_lbl.text = f"HEADSTART: {self.engine.headstart_timer:.1f}s"
            else:
                self.timer_lbl.text = "BOSS CHASING!"
                return False

    def update_coin_display(self, count):
        self.hud.coins = count
        self.coin_lbl.text = f"COINS: {count}"

    def setup_touch_controls(self):
        left_box = BoxLayout(size_hint=(None, None), size=(210, 95), pos_hint={'x': 0.02, 'y': 0.02}, spacing=12)
        btn_l = TouchControlButton(text="<")
        btn_l.bind(on_press=lambda i: self.set_key_state('key_left', True))
        btn_l.bind(on_release=lambda i: self.set_key_state('key_left', False))

        btn_r = TouchControlButton(text=">")
        btn_r.bind(on_press=lambda i: self.set_key_state('key_right', True))
        btn_r.bind(on_release=lambda i: self.set_key_state('key_right', False))

        left_box.add_widget(btn_l)
        left_box.add_widget(btn_r)

        right_box = BoxLayout(size_hint=(None, None), size=(210, 95), pos_hint={'right': 0.98, 'y': 0.02}, spacing=12)
        btn_c = TouchControlButton(text="CROUCH")
        btn_c.bind(on_press=lambda i: setattr(self.engine, 'is_crouching', True))
        btn_c.bind(on_release=lambda i: setattr(self.engine, 'is_crouching', False))

        btn_j = TouchControlButton(text="JUMP")
        btn_j.bind(on_press=lambda i: setattr(self.engine, 'is_holding_jump', True))
        btn_j.bind(on_release=lambda i: setattr(self.engine, 'is_holding_jump', False))

        right_box.add_widget(btn_c)
        right_box.add_widget(btn_j)

        self.root_layout.add_widget(left_box)
        self.root_layout.add_widget(right_box)

    def set_key_state(self, attr_name, value):
        setattr(self.engine, attr_name, value)
        self.engine.update_moving_dir()

    def toggle_pause(self, instance):
        self.engine.is_paused = not self.engine.is_paused
        if self.engine.is_paused:
            content = BoxLayout(orientation='vertical', padding=15, spacing=10)
            lbl = Label(text="Dont quit now buddy", font_size='18sp', bold=True)
            btn_resume = StylizedMenuButton(text="RESUME")
            btn_retry = StylizedMenuButton(text="RETRY")
            btn_menu = StylizedMenuButton(text="MAIN MENU")

            content.add_widget(lbl)
            content.add_widget(btn_resume)
            content.add_widget(btn_retry)
            content.add_widget(btn_menu)

            popup = Popup(title="Game Paused", content=content, size_hint=(None, None), size=(320, 280), auto_dismiss=False)
            btn_resume.bind(on_press=lambda i: (SoundManager.play_click(), popup.dismiss(), setattr(self.engine, 'is_paused', False)))
            btn_retry.bind(on_press=lambda i: (SoundManager.play_click(), popup.dismiss(), self.clear_polyester_videos(), self.load_level(self.engine.level)))
            btn_menu.bind(on_press=lambda i: (SoundManager.play_click(), popup.dismiss(), self.clear_polyester_videos(), self.show_main_menu()))
            popup.open()

    def clear_polyester_videos(self):
        for t in self.polyester_timers:
            t.cancel()
        self.polyester_timers.clear()
        
        for v in self.spawned_videos:
            if hasattr(v, 'video') and v.video:
                try:
                    v.video.state = 'stop'
                    v.video.source = ''
                except Exception:
                    pass
            if v.parent:
                v.parent.remove_widget(v)
        self.spawned_videos.clear()

    def spawn_polyester_video(self):
        if not os.path.exists("polyester.mp4"):
            return

        vw, vh = 320, 240
        win_w = max(Window.width, 600)
        win_h = max(Window.height, 400)

        max_x = int(win_w - vw - 40)
        max_y = int(win_h - vh - 40)
        
        rand_x = random.randint(20, max_x) if max_x > 20 else 50
        rand_y = random.randint(20, max_y) if max_y > 20 else 50
        angle = random.randint(-45, 45)

        vid_widget = RotatedVideoWidget(source="polyester.mp4", angle=angle, volume=0.0, size_hint=(None, None), size=(vw, vh), pos=(rand_x, rand_y))
        
        self.root_layout.add_widget(vid_widget)
        self.spawned_videos.append(vid_widget)

    def trigger_game_over_timers(self):
        self.clear_polyester_videos()
        delay_1 = 6.0 + random.uniform(0.0, 2.0)
        t1 = Clock.schedule_once(lambda dt: self.spawn_polyester_video(), delay_1)
        self.polyester_timers.append(t1)

    def trigger_boss_jumpscare_sequence(self):
        self.clear_polyester_videos()
        self.root_layout.clear_widgets()

        if not os.path.exists("jumpscare.mp4"):
            self.show_pipe_dide_popup(is_pipe=False)
            return

        video_layout = FloatLayout(size_hint=(1, 1))
        self.root_layout.add_widget(video_layout)

        def show_you_are_died_popup():
            self.root_layout.clear_widgets()
            content = BoxLayout(orientation='vertical', padding=20, spacing=20)
            
            lbl_died = Label(text="You are Died", font_size='26sp', bold=True, color=(1, 0.2, 0.2, 1), halign='center')
            content.add_widget(lbl_died)

            btn_retry = StylizedMenuButton(text="RETRY LEVEL")
            content.add_widget(btn_retry)

            popup = Popup(title="Game Over", content=content, size_hint=(None, None), size=(320, 220), auto_dismiss=False)
            
            def do_retry(instance):
                SoundManager.play_click()
                popup.dismiss()
                self.load_level(5)

            btn_retry.bind(on_press=do_retry)
            self.active_popup = popup
            popup.open()

        jumpscare_widget = RotatedVideoWidget(
            source="jumpscare.mp4", 
            angle=0, 
            volume=1.0, 
            eos_action='stop', 
            on_eos=show_you_are_died_popup, 
            size_hint=(1, 1)
        )
        video_layout.add_widget(jumpscare_widget)

    def show_void_death_popup(self):
        SoundManager.stop_bgm()
        self.clear_polyester_videos()
        
        content = BoxLayout(orientation='vertical', padding=15, spacing=15)
        
        if os.path.exists("question.png"):
            img = Image(source="question.png", size_hint=(None, None), size=(120, 120), pos_hint={'center_x': 0.5})
            content.add_widget(img)
        
        lbl = Label(text="how you gon die to the void yo", font_size='16sp', bold=True, color=(1, 0.3, 0.3, 1), halign='center')
        content.add_widget(lbl)

        btn_retry = StylizedMenuButton(text="retry level")
        content.add_widget(btn_retry)

        popup = Popup(title="Void Death", content=content, size_hint=(None, None), size=(340, 280), auto_dismiss=False)
        
        def do_retry(instance):
            SoundManager.play_click()
            popup.dismiss()
            self.load_level(self.engine.level)

        btn_retry.bind(on_press=do_retry)
        self.active_popup = popup
        popup.open()

    def show_pipe_dide_popup(self, is_pipe=False):
        SoundManager.stop_bgm()
        content = BoxLayout(orientation='vertical', padding=15, spacing=15)
        
        if is_pipe:
            lbl = Label(text="you dide", font_size='22sp', bold=True, color=(1, 0.2, 0.2, 1))
            content.add_widget(lbl)

        btn_retry = StylizedMenuButton(text="RETRY LEVEL")
        btn_menu = StylizedMenuButton(text="MAIN MENU")

        content.add_widget(btn_retry)
        content.add_widget(btn_menu)

        popup_title = "You Dide!" if is_pipe else "Game Over"
        popup_height = 230 if is_pipe else 180

        popup = Popup(title=popup_title, content=content, size_hint=(None, None), size=(300, popup_height), auto_dismiss=False)
        
        def close_and_cleanup(instance, *args):
            self.clear_polyester_videos()
            popup.dismiss()

        btn_retry.bind(on_press=lambda i: (SoundManager.play_click(), close_and_cleanup(i), self.load_level(self.engine.level)))
        btn_menu.bind(on_press=lambda i: (SoundManager.play_click(), close_and_cleanup(i), self.show_main_menu()))
        
        self.active_popup = popup
        popup.open()
        
        self.trigger_game_over_timers()

    def on_level_clear(self, lvl):
        SoundManager.stop_bgm()
        if lvl + 1 > self.max_unlocked_level:
            self.max_unlocked_level = lvl + 1

        content = BoxLayout(orientation='vertical', padding=15, spacing=15)
        
        if lvl == 5:
            if os.path.exists("notbad.png"):
                img = Image(source="notbad.png", size_hint=(None, None), size=(180, 120), pos_hint={'center_x': 0.5})
                content.add_widget(img)
            else:
                fallback_lbl = Label(text="[Image: notbad.png]", font_size='14sp', color=(0.7, 0.7, 0.7, 1))
                content.add_widget(fallback_lbl)

            lbl_msg = Label(text="Not bad kid, Not bad", font_size='18sp', bold=True, color=(1, 0.9, 0.2, 1))
            content.add_widget(lbl_msg)

            btn_next = StylizedMenuButton(text="Next")
            content.add_widget(btn_next)

            popup = Popup(title="Congratulations!", content=content, size_hint=(None, None), size=(340, 320), auto_dismiss=False)
            
            def on_next_pressed(instance):
                SoundManager.play_click()
                popup.dismiss()
                self.show_syri_thank_you_display()

            btn_next.bind(on_press=on_next_pressed)
            popup.open()
        else:
            lbl = Label(text=f"Level {lvl} Completed!", font_size='18sp', bold=True)
            btn_next = StylizedMenuButton(text="NEXT LEVEL")
            btn_menu = StylizedMenuButton(text="MAIN MENU")

            content.add_widget(lbl)
            content.add_widget(btn_next)
            content.add_widget(btn_menu)

            popup = Popup(title="Stage Cleared", content=content, size_hint=(None, None), size=(300, 230), auto_dismiss=False)
            btn_next.bind(on_press=lambda i: (SoundManager.play_click(), popup.dismiss(), self.load_level(min(5, lvl + 1))))
            btn_menu.bind(on_press=lambda i: (SoundManager.play_click(), popup.dismiss(), self.show_main_menu()))
            popup.open()

    def show_syri_thank_you_display(self):
        content = BoxLayout(orientation='vertical', padding=15, spacing=15)
        
        if os.path.exists( "syri.png"):
            img_syri = Image(source="syri.png", size_hint=(None, None), size=(140, 140), pos_hint={'center_x': 0.5})
            content.add_widget(img_syri)
        else:
            fallback_lbl = Label(text="[Image: syri.png]", font_size='14sp', color=(0.7, 0.7, 0.7, 1))
            content.add_widget(fallback_lbl)

        lbl_thanks = Label(text="thank you for playing brolio", font_size='16sp', bold=True, color=(1, 1, 1, 1), halign='center')
        content.add_widget(lbl_thanks)

        btn_quit = StylizedMenuButton(text="Quit game")
        content.add_widget(btn_quit)

        popup = Popup(title="Thank You!", content=content, size_hint=(None, None), size=(340, 340), auto_dismiss=False)
        
        def handle_quit_button(instance):
            SoundManager.play_click()
            popup.dismiss()
            self.start_quit_sequence()

        btn_quit.bind(on_press=handle_quit_button)
        popup.open()

    def start_quit_sequence(self):
        self.root_layout.clear_widgets()

        with self.root_layout.canvas:
            Color(0, 0, 0, 1)
            Rectangle(pos=(0, 0), size=Window.size)

        Clock.schedule_once(lambda dt: self.play_break_and_polyester_videos(), 1.0)

    def play_break_and_polyester_videos(self):
        self.root_layout.clear_widgets()

        layout = FloatLayout(size_hint=(1, 1))
        self.root_layout.add_widget(layout)

        if os.path.exists("polyester.mp4"):
            def on_break_eos():
                App.get_running_app().stop()

            break_widget = RotatedVideoWidget(
                source="polyester.mp4", 
                angle=0, 
                volume=1.0, 
                eos_action='stop', 
                on_eos=on_break_eos, 
                size_hint=(1, 1)
            )
            layout.add_widget(break_widget)
        else:
            App.get_running_app().stop()

if __name__ == '__main__':
    MarioGameApp().run()