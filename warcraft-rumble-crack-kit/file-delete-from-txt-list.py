import os

def remove_files_from_list(folder_b, file_list_path):
    # 读取文件名列表文件
    with open(file_list_path, 'r') as file:
        files_to_remove = set(file.read().splitlines())

    # 获取文件夹B中的文件名列表
    files_b = os.listdir(folder_b)
    
    # 遍历文件夹B中的文件名
    for file_b in files_b:
        # 如果文件夹B中的文件名也在文件名列表中，则移除文件夹B中的文件
        if file_b in files_to_remove:
            os.remove(os.path.join(folder_b, file_b))
            print(f"Removed {file_b} from folder B.")

# 指定文件夹B的路径
folder_b_path = "F:\魔兽大作战\en_audio\en_wav_re-DX_Unit"

# 指定包含文件名列表的txt文件路径
file_list_path = "F:\魔兽大作战/audio/all-sfx-file.txt"

# 执行移除操作
remove_files_from_list(folder_b_path, file_list_path)
