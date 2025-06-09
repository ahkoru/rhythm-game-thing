import subprocess
import os

def read_osu_map(file_path: str,
                 reverse: bool = False) -> tuple[str, str, dict[str, list[int]], str]:
    """Converts a .osu file to something more readable for a certain rhythm game *cough* *cough*

    Args:
        reversed (bool, optional): Whether to reverse the notes' order. Defaults to False

    Returns:
        list[dict[str,int]]: A list containing dictionaries of notes containing the x, y, and time
    """
    hit_objects: dict[str, list[int]] = {"lane 1":[], "lane 2":[], "lane 3":[], "lane 4":[]}
    in_hit_objects: bool = False
    
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line: str = line.strip()
            
            if "AudioFilename" in line:
                audio_name = line.split(' ')[-1]
            
            if "TitleUnicode" in line:
                title = line.split(':')[-1]
                
            if "ArtistUnicode" in line:
                artist = line.split(':')[-1]
            
            if line == "[HitObjects]":
                in_hit_objects = True
            
            if not in_hit_objects:
                continue
            
            if not line:
                continue
            
            if not line[0].isdigit():
                continue
            
            parts: list[str] = line.split(',')
            
            if not len(parts) >= 3:
                continue
            
            x: int = int(parts[0])
            x = int((x / 64 + 1) / 2)  # Convert x value to lane number(1,2,3,4)
            time: int = int(parts[2])
            lane: str = f"lane {x}"
            hit_objects[lane].append(time)
            
        
        if reverse:
            for lane, y_values in hit_objects.items():
                hit_objects[lane] = y_values[::-1]
            
    return title, artist, hit_objects, audio_name

def get_file_path(start_dir="~/Downloads"):
    start_dir = os.path.expanduser(start_dir)
    print(start_dir)
    result = subprocess.run(['zenity', '--file-selection', f'--filename={start_dir}/'], stdout=subprocess.PIPE)
    file_path = result.stdout.decode('utf-8').strip()
    return file_path
