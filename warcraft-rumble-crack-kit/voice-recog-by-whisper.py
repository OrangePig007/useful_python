import os
import whisper

def clean_filename(filename):
    # 替换无效字符
    invalid_chars = r'\/:*?"<>|'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    
    return filename

def transcribe_and_rename(input_folder, output_folder, model_name="base"):
    # 加载Whisper模型
    model = whisper.load_model(model_name)

    # 获取输入文件夹中的所有音频文件
    audio_files = [f for f in os.listdir(input_folder) if f.endswith(('.wav'))]

    for audio_file in audio_files:
        # 构造音频文件的完整路径
        audio_file_path = os.path.join(input_folder, audio_file)

        # 进行音频文件的识别
        result = model.transcribe(audio_file_path, language="Chinese")

        # 获取识别结果的文本
        transcription = clean_filename(result["text"])

        # 构造目标文件的新文件名
        new_file_name = f"{audio_file[:-4].replace('.wem', '')}_{transcription.replace(' ', '_')}{audio_file[-4:]}"

        # 构造目标文件的完整路径
        new_file_path = os.path.join(output_folder, new_file_name)

        # 重命名目标文件
        os.rename(audio_file_path, new_file_path)
        print(f"Renamed: {audio_file_path} -> {new_file_path}")

if __name__ == "__main__":
    # 指定输入和输出文件夹的路径
    input_folder_path = "F:/魔兽大作战/audio/wem-has-name-zhcn-2 - 副本"
    output_folder_path = "F:/魔兽大作战/audio/wem-has-name-zhcn-2 - rename"

    # 执行音频文件的识别和重命名
    transcribe_and_rename(input_folder_path, output_folder_path)
