import time
import sys
import os
import subprocess
from rich.console import Console
from rich.text import Text
from rich.live import Live

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:   
        subprocess.call('clear')

def reff1():
    lirik = [
        (18.9,'🎵...'),
        (1.5,'Your morning eyes..I could stare like watching stars'),
        (0.27,"I could walk you by..and I'll tell without a tought"),
        (0.3,"You'd be mine..."),
        (1.0,'Would you mind...if I took your hand tonight'),
        (3.3,"Know you're all...that I want - this life"),
    ]

    def per_huruf(baris, delay = 0.2):
        for huruf in baris:
            sys.stdout.write(huruf)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def per_baris(lirik, delay_huruf = 0.2):
        clear_terminal()
        for delay, baris in lirik:
            per_huruf(baris, delay= delay_huruf)
            time.sleep(delay)
    per_baris(lirik, delay_huruf = 0.11)

def reff2():
    lirik = [
        (0.1,"I'll imagine we fell in love"),
        (0.11,"I'll nap under moonlight skies with you"),
        (0.12,"I think I'll picture us, you with the waves"),
        (0.15,"The ocean's colors on your face"),
        (1.5,"I'll leave my heart..with your air..."),
        (1.0,'So let me fly with you..'),
    ]
    
    def per_huruf(baris, delay = 0.1):
        for huruf in baris:
            sys.stdout.write(huruf)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    def per_baris(lirik, delay_huruf = 0.1):
        clear_terminal()
        for delay, baris in lirik:
            per_huruf(baris, delay= delay_huruf)
            time.sleep(delay)
    per_baris(lirik, delay_huruf = 0.09)

def get_terminal_width():
    """Mengembalikan lebar terminal saat ini."""
    return os.get_terminal_size().columns

# def fireworks(console):
#     """Menampilkan animasi kembang api sederhana."""
#     patterns = [
#         "     🎆        🎆        🎆     ",
#         "         🎇          🎇         ",
#         "    🌟     🌟     🌟    ",
#         "        ✨       ✨        ",
#         "   🌠       🌠      🌠   ",
#     ]
#     clear_terminal()
#     with Live(console=console, refresh_per_second=4) as live:
#         for _ in range(10):  
#             for pattern in patterns:
#                 live.update(Text(pattern, style="bold yellow"))
#                 console.print(pattern, style="bold yellow", justify="center")
#                 time.sleep(0.3)

def display_love(console):
    """Menampilkan hati dengan pola ASCII di terminal."""
    heart = [
        "   ******       ******   ",
        " **      **   **      ** ",
        "**        ** **        **",
        "**         ***         **",
        " **        *         ** ",
        "   **               **   ",
        "     **           **     ",
        "       **       **       ",
        "         **   **         ",
        "           **           "
    ]
    terminal_width = get_terminal_width()
    for line in heart:
        console.print(line.center(terminal_width), style="bold red")
        time.sleep(0.2)


def las_reff():
    console = Console()
    teks = "Will you be forever with me?"
    delay = 0.2

    def tampilkan_perhuruf(teks, delay):
        """Menampilkan teks per huruf dengan posisi di tengah terminal."""
        terminal_width = get_terminal_width()
        padding = (terminal_width - len(teks)) // 2  
        for i in range(len(teks) + 1):
            clear_terminal()
            baris = " " * padding + teks[:i]  
            console.print(baris, style="bold magenta")
            time.sleep(delay)

    
    clear_terminal()
    console.print("\n💖 CONFESSION TIME 💖\n", style="bold green underline", justify="center")
    tampilkan_perhuruf(teks, delay)
    console.print("\n💖 Will you be my heart? 💖", style="bold cyan", justify="center")
    
    
    display_love(console)  


def main():
    reff1()
    reff2()
    las_reff()
main()