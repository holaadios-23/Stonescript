import sys

# --- Funciones de Conversión ---

def time_to_ssrpg_frames(days, hours, minutes, seconds):
    """Convierte duración a frames de Stone Story RPG (30 FPS)."""
    FRAMES_PER_SECOND = 30
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24

    total_seconds = (days * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE) + \
                    (hours * MINUTES_PER_HOUR * SECONDS_PER_MINUTE) + \
                    (minutes * SECONDS_PER_MINUTE) + \
                    seconds

    return total_seconds * FRAMES_PER_SECOND

def frames_to_time(total_frames):
    """Convierte frames a tiempo (días, horas, minutos, segundos)."""
    if total_frames < 0:
        return 0, 0, 0, 0

    FRAMES_PER_SECOND = 30
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24

    total_seconds = total_frames // FRAMES_PER_SECOND
    seconds = total_seconds % SECONDS_PER_MINUTE
    total_minutes = total_seconds // SECONDS_PER_MINUTE
    minutes = total_minutes % MINUTES_PER_HOUR
    total_hours = total_minutes // MINUTES_PER_HOUR
    hours = total_hours % HOURS_PER_DAY
    days = total_hours // HOURS_PER_DAY
    
    return days, hours, minutes, seconds

def main():
    while True:
        print("\n" + "="*40)
        print(" CONVERSOR TIEMPO <=> FRAMES (SSR PG)")
        print("="*40)
        print("1. Tiempo a Frames")
        print("2. Frames a Tiempo")
        print("3. Salir")
        
        opcion = input("\nSelecciona una opción (1-3): ")
        
        if opcion == "1":
            try:
                d = int(input("Días: ") or 0)
                h = int(input("Horas: ") or 0)
                m = int(input("Minutos: ") or 0)
                s = int(input("Segundos: ") or 0)
                
                frames = time_to_ssrpg_frames(d, h, m, s)
                print(f"\n>> TOTAL DE FRAMES: {frames:,}")
            except ValueError:
                print("\n[Error] Por favor, introduce solo números enteros.")
                
        elif opcion == "2":
            try:
                f = int(input("Introduce el total de frames: ") or 0)
                days, hours, minutes, seconds = frames_to_time(f)
                print(f"\n>> RESULTADO: {days}d, {hours}h, {minutes}m, {seconds}s")
            except ValueError:
                print("\n[Error] Por favor, introduce solo números enteros.")
                
        elif opcion == "3":
            print("\n¡Buena suerte en la Piedra Mental! Saliendo...")
            sys.exit()
        else:
            print("\n[!] Opción no válida.")

        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSaliendo...")
        sys.exit()
