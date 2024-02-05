import os
import re

def convert_and_rename_file(original_filename, prefix, output_folder):
    # 提取文件名中的序号和文字部分
    parts = original_filename.split('_')
    number = int(parts[0])  # Convert number to integer for proper sorting
    text = parts[1].split('.')[0]
    
    # 如果{text}末尾不是！或？或。或……，那就加一个
    if not re.search(r'[！？。…… . ? !]$', text):
        text += '。'  # Add a period if not already ending with '！', '？', '。', or '……'
    
    # 构建新的文件名
    new_filename = f"{prefix}_{number}.mp3"

    # 构建新的文件路径
    new_filepath = os.path.join(output_folder, new_filename)
    
    # 重命名文件
    os.rename(os.path.join(folder_path, original_filename), new_filepath)
    
    return new_filename, text

def batch_convert_and_rename(folder_path, prefix, output_folder, output_txt):
    with open(output_txt, 'w', encoding='utf-8') as output_file:
        filenames = sorted(os.listdir(folder_path), key=lambda x: int(x.split('_')[0]))
        for filename in filenames:
            if filename.endswith('.mp3'):
                new_filename, text = convert_and_rename_file(filename, prefix, output_folder)
                output_line = f"{{{{HOKAudio|file1={new_filename}|zh={text}}}}}"
                # output_line = f"|file2={new_filename}|en={text}}}}}"
                output_file.write(output_line + '\n')

if __name__ == "__main__":
    folder_path = "E:\王者荣耀音频处理\dump_vo/"  # 输入文件夹路径
    prefix = "敖隐_凌霄真龙_语音"  # 输入要添加的字符串

    output_folder = "E:\王者荣耀音频处理/rename_vo/"  # 输入输出文件夹路径
    output_txt = "E:\王者荣耀音频处理/new.txt"  # 输入输出txt文件路径

    batch_convert_and_rename(folder_path, prefix, output_folder, output_txt)
    print("文件重命名和导出成功！")
