from pydub import AudioSegment
import os

def merge_audio_with_space(parent_folder, subfolder_order, audio_file_names, space_duration=1500):
    # Convert space duration from milliseconds to seconds
    space_duration /= 1000

    # Initialize an empty audio segment to store the final result
    final_audio = AudioSegment.silent(duration=0)
    for audio_file_name in audio_file_names:
        for subfolder_name in subfolder_order:
            audio_path = os.path.join(parent_folder, subfolder_name, audio_file_name)

            # Load the audio file
            audio_segment = AudioSegment.from_file(audio_path)

            # Append the current audio segment to the final result
            final_audio += audio_segment

            # Add empty space after each audio segment (except the last one)
            final_audio += AudioSegment.silent(duration=space_duration * 1000)

    return final_audio

# Example usage with different subfolder order and a list of audio file names
parent_folder = "E:/apex素材/sounds"
subfolder_order = ["Mandarin", "English","Japanese","Korean","Russian","German","French","Spanish","Italian","Polish"]
audio_file_names = ["diag_mp_bloodhound_bc_super_01_01_1p.wav", "diag_mp_bloodhound_bc_super_02_01_1p.wav","diag_mp_bloodhound_bc_super_03_01_1p.wav","diag_mp_bloodhound_bc_super_04_01_1p.wav"]
result = merge_audio_with_space(parent_folder, subfolder_order, audio_file_names)

# Export the result to a new file
result.export("E:/apex素材/sounds/final_result.wav", format="wav")
