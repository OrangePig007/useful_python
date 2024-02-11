import os

def rename_files(folder_path):
    # 获取文件夹中所有文件名
    files = os.listdir(folder_path)
    
    # 创建一个字典来存储文件名对应的计数器
    name_counter = {}
    
    # 遍历文件夹中的每个文件
    for filename in files:
        # 分割文件名
        parts = filename.split('_')
        # 获取第3个_之前的内容
        new_filename = '_'.join(parts[:3])
        # 如果字典中已经有该文件名，则递增计数器
        if new_filename in name_counter:
            name_counter[new_filename] += 1
        else:
            name_counter[new_filename] = 1
        # 生成新的文件名
        new_filename = f"{new_filename}_{name_counter[new_filename]:02d}_en.wav"
        # 重命名文件
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
        print(f"Renamed {filename} to {new_filename}")

# 使用示例
folder_path = 'F:\魔兽大作战\en_audio\en_wav_re-DX_Unit'
rename_files(folder_path)
