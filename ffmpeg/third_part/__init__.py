from pathlib import Path

base_path = Path(__file__).parent.absolute()
ffmpeg_path = (base_path / "./ffmpeg").resolve()
print(ffmpeg_path)