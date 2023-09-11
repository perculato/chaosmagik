# chaosmagik
Ask me about my cryptosorcery

## music_sigil.py
This code is a Python script that generates and plays a melody based on a sequence of letters entered by the user. 
Each letter corresponds to a musical note, and the script uses the sounddevice library to play the generated melody through the selected audio output device.
I've calculated the frequencies assigning on each letter of my name based on a tetractyc pyramid and then devising the rest.

### How it Works
The code defines a function generate_note(frequency, duration) that generates a sound wave based on a given frequency and duration.
It also creates a dictionary called letter_to_frequency, mapping uppercase letters, numbers, and spaces to corresponding frequencies for musical notes.
The user is prompted to enter a sequence of letters (state your desire or intention). The input is case-insensitive, and the code converts all letters to uppercase for consistency.
A separate thread is started to allow the user to stop the melody playback manually. This is achieved by setting the is_playing flag to False when the user enters any input.
The code generates the melody based on the user's input sequence. It looks up the frequency for each letter in the letter_to_frequency dictionary and generates a short note (0.4 seconds) for each letter.
The code then lists the available audio output devices and prompts the user to select one by entering the device number.
The melody is played in a loop until the user manually interrupts it. The sounddevice library is used to play the melody with the selected audio output device. 
If an error occurs during playback, it falls back to printing the notes in the console with a 0.5-second delay between each note.

### Usage
Run the script in your Python environment.
Enter a sequence of letters when prompted. You can use uppercase letters, numbers, and spaces.
Choose an audio output device by entering the device number as listed.
The script will start playing the melody based on your input. You can manually interrupt the playback by entering any input.

### Note
If you encounter any errors during audio playback, the script will print the notes in the console, allowing you to hear the melody in a different way.
Ensure that you have a speaker or audio output device connected and configured correctly to hear the melody.

## star_sigil.py

### Introduction
This Python script generates an artistic representation of planets and their connections based on a user-provided seed phrase. 
It utilizes the matplotlib library to create the visual artwork and randomly selects planets' symbols to form a unique astrological image.

### How it Works
The code prompts the user to input a seed phrase, which is used to initialize the random number generator. The length of the seed phrase is also recorded.
It defines a set of planet symbols, such as ☉ (Sun), ♁ (Earth), ♃ (Jupiter), etc., to be used in the artwork.
A figure and axis are created using matplotlib.
The script draws a black circle at the center of the plot, representing the background layer.
Randomized positions for the planet symbols are generated within the circle, with their quantity determined by a random range between 1 and 12 (to limit the number of symbols).
Planet symbols are displayed at the generated positions with some transparency to create an artistic effect.
Lines are added to connect the planet symbols, forming a network-like pattern.
White circles with black borders are added on top of the planet symbols to create a layered effect.
The aspect ratio of the plot is set to be equal to ensure the image appears circular.
Axis limits are defined, and the axes are removed for a clean and focused visual.
The script saves the generated artwork as an image file with a filename based on the provided seed phrase.
The final artwork is displayed using matplotlib.

### Usage
Run the script in your Python environment.
Enter a seed phrase when prompted. You can use any phrase to generate a unique astrological artwork.
The script will create an artistic representation of planets and their connections based on the seed phrase and display it on your screen.
The artwork will also be saved as an image file named after the seed phrase.

#### Optional: Adding a Legend
If you want to add a legend below the circle with the names of the planets, you can uncomment the relevant code block. This will provide a brief description of each planet symbol.

### Note
You can experiment with different seed phrases to create a variety of unique astrological artworks.
Make sure you have the matplotlib library properly configured to display the generated artwork.
Enjoy generating your own astrological art!






