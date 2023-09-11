import numpy as np
import threading
import time
import sounddevice as sd

# Funzione per generare un suono basato su una frequenza
def generate_note(frequency, duration):
    sample_rate = 44100  # Frequenza di campionamento in Hz
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    return wave

letter_to_frequency = {
    'A': 1760.0,
    'B': 329.63,
    'C': 2349.32,
    'D': 987.77,
    'E': 1318.51,
    'F': 4186.01,
    'G': 293.66,
    'H': 1396.91,
    'I': 659.26,
    'J': 1975.53,
    'K': 587.33,
    'L': 349.23,
    'M': 783.99,
    'N': 523.25,
    'O': 3951.07,
    'P': 3520.0,
    'Q': 1046.5,
    'R': 1760.0,
    'S': 2637.02,
    'T': 261.63,
    'U': 3135.96,
    'V': 1174.66,
    'W': 4698.63,
    'X': 261.63,
    'Y': 349.23,
    'Z': 2093.0,
    '0': 659.26,
    '1': 987.77,
    '2': 493.88,
    '3': 329.63,
    '4': 1046.5,
    '5': 880.0,
    '6': 440.0,
    '7': 1396.91,
    '8': 293.66,
    '9': 329.63,
    ' ': 000.00
}


# Sequenza di lettere inserita dall'utente
sequence = input("Inserisci una sequenza di lettere per generare una melodia: ")

# Funzione per interrompere il loop
def stop_playing():
    global is_playing
    is_playing = False

# Creazione di un thread per l'input dell'utente
input_thread = threading.Thread(target=stop_playing)
input_thread.daemon = True
input_thread.start()

# Variabile per controllare il loop di riproduzione
is_playing = True

# Genera la melodia basata sulla sequenza
melody = np.array([])

for letter in sequence:
    letter = letter.upper()  # Trasforma la lettera in maiuscolo per la ricerca nella mappa
    if letter in letter_to_frequency:
        frequency = letter_to_frequency[letter]
        note = generate_note(frequency, 0.4)  # Durata di ogni nota
        melody = np.concatenate((melody, note))

# Ottieni la lista dei dispositivi audio disponibili
available_devices = sd.query_devices()
print("Dispositivi audio disponibili:")
for i, device in enumerate(available_devices):
    print(f"{i + 1}: {device['name']}")

# Lascia l'utente scegliere un dispositivo
selected_device_index = int(input("Inserisci il numero del dispositivo desiderato: ")) - 1

# Riproduci la melodia in loop fino a quando non interrompi manualmente
while is_playing:
    try:
        sd.play(melody, 44100, device=selected_device_index)
        sd.wait()
    except sd.PortAudioError as e:
        print(f"Errore durante la riproduzione audio: {e}")
        print("Riproduzione in console:")
        for note in melody:
            print(note)
            time.sleep(0.5)  # Tempo tra le note (0.5 secondi)
