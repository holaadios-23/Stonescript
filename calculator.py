import tkinter as tk
from tkinter import ttk

# --- Funciones de Conversión ---

def time_to_ssrpg_frames(days, hours, minutes, seconds):
  """
  Convierte una duración de tiempo (días, horas, minutos, segundos)
  a frames de Stone Story RPG, asumiendo 30 FPS.

  Args:
    days (int): Número de días.
    hours (int): Número de horas.
    minutes (int): Número de minutos.
    seconds (int): Número de segundos.

  Returns:
    int: El número total de frames correspondientes.
  """
  # Constantes de conversión
  FRAMES_PER_SECOND = 30
  SECONDS_PER_MINUTE = 60
  MINUTES_PER_HOUR = 60
  HOURS_PER_DAY = 24

  # 1. Calcular el total de segundos
  total_seconds = (days * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE) + \
                  (hours * MINUTES_PER_HOUR * SECONDS_PER_MINUTE) + \
                  (minutes * SECONDS_PER_MINUTE) + \
                  seconds

  # 2. Calcular el total de frames
  total_frames = total_seconds * FRAMES_PER_SECOND

  return total_frames

def frames_to_time(total_frames):
    """
    Convierte un número total de frames de Stone Story RPG a tiempo
    (días, horas, minutos, segundos).

    Args:
      total_frames (int): El número total de frames.

    Returns:
      tuple: Una tupla con (días, horas, minutos, segundos).
    """
    if total_frames < 0:
        return 0, 0, 0, 0

    FRAMES_PER_SECOND = 30
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24

    # 1. Convertir frames a segundos totales (usando división entera)
    total_seconds = total_frames // FRAMES_PER_SECOND
    
    # 2. Calcular segundos y minutos restantes
    seconds = total_seconds % SECONDS_PER_MINUTE
    total_minutes = total_seconds // SECONDS_PER_MINUTE
    
    # 3. Calcular minutos y horas restantes
    minutes = total_minutes % MINUTES_PER_HOUR
    total_hours = total_minutes // MINUTES_PER_HOUR
    
    # 4. Calcular horas y días restantes
    hours = total_hours % HOURS_PER_DAY
    days = total_hours // HOURS_PER_DAY
    
    return days, hours, minutes, seconds

# --- Funciones de la Interfaz ---

def calculate_frames_and_display():
    """Toma los valores de tiempo, calcula frames y muestra el resultado."""
    try:
        days = int(days_entry.get() or 0)
        hours = int(hours_entry.get() or 0)
        minutes = int(minutes_entry.get() or 0)
        seconds = int(seconds_entry.get() or 0)
    except ValueError:
        days, hours, minutes, seconds = 0, 0, 0, 0

    total_frames = time_to_ssrpg_frames(days, hours, minutes, seconds)
    result_frames_label.config(text=f"Frames totales: {total_frames:,}")

def calculate_time_and_display():
    """Toma los frames, calcula el tiempo y muestra el resultado."""
    try:
        total_frames = int(frames_entry.get() or 0)
    except ValueError:
        total_frames = 0
    
    days, hours, minutes, seconds = frames_to_time(total_frames)
    
    result_time_label.config(text=f"Resultado: {days}d, {hours}h, {minutes}m, {seconds}s")

def clear_time_fields():
    """Limpia los campos de tiempo."""
    days_entry.delete(0, tk.END)
    hours_entry.delete(0, tk.END)
    minutes_entry.delete(0, tk.END)
    seconds_entry.delete(0, tk.END)
    result_frames_label.config(text="Frames totales: 0")
    days_entry.focus()

def clear_frames_field():
    """Limpia el campo de frames."""
    frames_entry.delete(0, tk.END)
    result_time_label.config(text="Resultado: 0d, 0h, 0m, 0s")
    frames_entry.focus()

def handle_enter(event):
    """Ejecuta el cálculo correspondiente según el campo que tenga el foco."""
    focused_widget = root.focus_get()
    if focused_widget in [days_entry, hours_entry, minutes_entry, seconds_entry]:
        calculate_frames_and_display()
    elif focused_widget == frames_entry:
        calculate_time_and_display()

# --- Configuración de la Interfaz Gráfica (GUI) ---
root = tk.Tk()
root.title("Conversor Tiempo <=> Frames (Stone Story RPG)")
root.resizable(False, False)
root.configure(bg='#222222') # Fondo oscuro para la ventana principal

# --- Estilos (Theming) ---
style = ttk.Style()
style.theme_use('clam') # 'clam' permite mayor personalización de colores

# Definición de colores
BG_COLOR = '#222222'
FG_COLOR = '#EEEEEE'
ACCENT_COLOR = '#00FF99' # Un verde cian estilo "loot raro"
ENTRY_BG = '#333333'
BUTTON_BG = '#444444'

style.configure('TFrame', background=BG_COLOR)
style.configure('TLabel', background=BG_COLOR, foreground=FG_COLOR)
style.configure('Header.TLabel', font=("Segoe UI", 10, "bold"), foreground=ACCENT_COLOR)
style.configure('Result.TLabel', font=("Segoe UI", 12, "bold"), foreground=ACCENT_COLOR)
style.configure('TEntry', fieldbackground=ENTRY_BG, foreground='#FFFFFF', insertcolor='#FFFFFF')
style.configure('TButton', background=BUTTON_BG, foreground='#FFFFFF', borderwidth=1, focuscolor='none')
style.map('TButton', background=[('active', '#555555')]) # Color al pasar el mouse
style.configure('Horizontal.TSeparator', background='#555555')

main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# --- Parte 1: Tiempo a Frames ---
time_to_frames_label = ttk.Label(main_frame, text="Tiempo a Frames", style="Header.TLabel")
time_to_frames_label.grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky='w')

ttk.Label(main_frame, text="Días:").grid(row=1, column=0, sticky=tk.W, pady=2)
days_entry = ttk.Entry(main_frame, width=20)
days_entry.grid(row=1, column=1, pady=2)

ttk.Label(main_frame, text="Horas:").grid(row=2, column=0, sticky=tk.W, pady=2)
hours_entry = ttk.Entry(main_frame, width=20)
hours_entry.grid(row=2, column=1, pady=2)

ttk.Label(main_frame, text="Minutos:").grid(row=3, column=0, sticky=tk.W, pady=2)
minutes_entry = ttk.Entry(main_frame, width=20)
minutes_entry.grid(row=3, column=1, pady=2)

ttk.Label(main_frame, text="Segundos:").grid(row=4, column=0, sticky=tk.W, pady=2)
seconds_entry = ttk.Entry(main_frame, width=20)
seconds_entry.grid(row=4, column=1, pady=2)

# Botones Parte 1
btn_frame_1 = ttk.Frame(main_frame)
btn_frame_1.grid(row=5, column=0, columnspan=2, pady=10)

ttk.Button(btn_frame_1, text="Calcular", command=calculate_frames_and_display).pack(side=tk.LEFT, padx=5)
ttk.Button(btn_frame_1, text="Limpiar", command=clear_time_fields).pack(side=tk.LEFT, padx=5)

result_frames_label = ttk.Label(main_frame, text="Frames totales: 0", style="Result.TLabel")
result_frames_label.grid(row=6, column=0, columnspan=2)

# --- Separador y Parte 2: Frames a Tiempo ---
separator = ttk.Separator(main_frame, orient='horizontal')
separator.grid(row=7, column=0, columnspan=2, sticky='ew', pady=20)

frames_to_time_label = ttk.Label(main_frame, text="Frames a Tiempo", style="Header.TLabel")
frames_to_time_label.grid(row=8, column=0, columnspan=2, pady=(0, 10), sticky='w')

ttk.Label(main_frame, text="Frames:").grid(row=9, column=0, sticky=tk.W, pady=2)
frames_entry = ttk.Entry(main_frame, width=20)
frames_entry.grid(row=9, column=1, pady=2)

# Botones Parte 2
btn_frame_2 = ttk.Frame(main_frame)
btn_frame_2.grid(row=10, column=0, columnspan=2, pady=10)

ttk.Button(btn_frame_2, text="Calcular", command=calculate_time_and_display).pack(side=tk.LEFT, padx=5)
ttk.Button(btn_frame_2, text="Limpiar", command=clear_frames_field).pack(side=tk.LEFT, padx=5)

result_time_label = ttk.Label(main_frame, text="Resultado: 0d, 0h, 0m, 0s", style="Result.TLabel")
result_time_label.grid(row=11, column=0, columnspan=2)

# --- Iniciar la aplicación ---
days_entry.focus()
root.bind('<Return>', handle_enter)
root.mainloop()
