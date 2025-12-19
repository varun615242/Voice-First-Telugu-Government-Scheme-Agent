import subprocess
import os

def convert_aac_to_mp4_in_folder(folder_path):
    if not os.path.isdir(folder_path):
        raise NotADirectoryError("Invalid folder path")

    for file in os.listdir(folder_path):
        if file.lower().endswith(".aac"):
            input_path = os.path.join(folder_path, file)
            output_file = os.path.splitext(file)[0] + ".mp4"
            output_path = os.path.join(folder_path, output_file)

            command = [
                "ffmpeg",
                "-y",              # overwrite if exists
                "-i", input_path,
                "-c", "copy",
                output_path
            ]

            subprocess.run(command, check=True)
            print(f"✅ Converted: {file} → {output_file}")

# ---------------- Run ----------------
if __name__ == "__main__":
    folder = "audios"   # change to your folder path
    convert_aac_to_mp4_in_folder(folder)