import os
import shutil
from pygame import mixer
import time

# Initialize Pygame Mixer
mixer.init()

# Directories
base_dir = './'  # The directory where your files are located
yes_dir = os.path.join(base_dir, 'perfect')
no_dir = os.path.join(base_dir, 'no')
maybe_dir = os.path.join(base_dir, 'maybe')

# Ensure the directories exist
os.makedirs(yes_dir, exist_ok=True)
os.makedirs(no_dir, exist_ok=True)
os.makedirs(maybe_dir, exist_ok=True)

# Get all MP3 files in base directory, sort by size
mp3_files = [f for f in os.listdir(base_dir) if f.endswith('.mp3')]
mp3_files.sort(key=lambda f: os.path.getsize(os.path.join(base_dir, f)), reverse=True)

for mp3 in mp3_files:
    txt_file = mp3.replace('.mp3', '.txt')

    while True:
        # Try to display the contents of the .txt file
        try:
            with open(os.path.join(base_dir, txt_file), 'r') as f:
                print(f.read())
        except Exception as e:
            print(f'Error reading file {txt_file}: {e}')

        # Try to play the MP3 file
        try:
            mixer.music.load(os.path.join(base_dir, mp3))
            mixer.music.play()
        except Exception as e:
            print(f'Error playing file {mp3}: {e}')

        # Wait for the music to finish
        while mixer.music.get_busy():
            time.sleep(1)

        # Offer options
        action = input("(R) Replay, (Y) Yes, (N) No, (L) Later, (E) Edit: ").upper()
        if action == 'R':
            # Replay the MP3
            try:
                mixer.music.play()
            except Exception as e:
                print(f'Error replaying file {mp3}: {e}')
        elif action in ['Y', 'N', 'L']:
            target_dir = yes_dir if action == 'Y' else no_dir if action == 'N' else maybe_dir

            # Try to move both the MP3 and the corresponding .txt file to the target folder
            try:
                shutil.move(os.path.join(base_dir, mp3), target_dir)
                shutil.move(os.path.join(base_dir, txt_file), target_dir)
            except Exception as e:
                print(f'Error moving files {mp3} and {txt_file}: {e}')

            break
        elif action == 'E':
            # Edit the .txt file
            try:
                os.system(f'vim {os.path.join(base_dir, txt_file)}')
            except Exception as e:
                print(f'Error editing file {txt_file}: {e}')
