import os

def process_folder(input_folder, output_folder):
    # 获取输入文件夹中的所有txt文件
    txt_files = [f for f in os.listdir(input_folder) if f.endswith('.txtp')]
    
    # 打开总结文档，准备写入内容
    with open(txt_path, 'w', encoding='utf8') as summary:
        for txt_file in txt_files:
            # 构造txt文件的完整路径
            txt_file_path = os.path.join(input_folder, txt_file)

            # 读取txt文件的每一行
            with open(txt_file_path, 'r') as file:
                for line in file:
                    # 检查每一行是否以"##memory"结尾
                    if line.strip().endswith("##memory"):
                        # 以"#i"分离一次，取第一个
                        parts = line.split("#i")
                        first_part = parts[0].strip()

                        # 以"/"分离一次，取最后一个
                        sub_parts = first_part.split("/")
                        target_string = sub_parts[-1].strip().split(".wem")[0]+'.wem.wav'
                        # 构造目标文件的完整路径
                        target_file_path = os.path.join(output_folder, target_string)

                        new_file_prefix = txt_file.split("-")[0]
                        # 构造目标文件的新文件名
                        new_file_name = f"{new_file_prefix}_{target_string}"
                        new_file_path = os.path.join(output_folder, new_file_name)

                        # 重命名目标文件
                        if os.path.exists(target_file_path):
                            os.rename(target_file_path, new_file_path)
                            print(f"Renamed: {target_file_path} -> {new_file_path}", file=summary)
                        else:
                            print(f"Target file not found: {target_file_path}", file=summary)

# 指定输入和输出文件夹的路径
input_folder_path = "F:\魔兽大作战/new/txtp" #txtp目录
output_folder_path = "F:\魔兽大作战/new" #wav目录
txt_path = "F:\魔兽大作战/new/对应结果4.txt"

# 执行处理
process_folder(input_folder_path, output_folder_path)


