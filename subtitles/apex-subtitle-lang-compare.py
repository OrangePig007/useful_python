import os

def extract_lines_from_txt(folder_path, line_number):
    combined_text = ""
    
    # 遍历文件夹
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            lang = filename.split('_')[-1].replace('.txt','').strip()
            # 打开文件并读取指定行的文本
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                
                # 检查行号是否在文件范围内
                if 0 < line_number <= len(lines):
                    split_result = lines[line_number-1].split(':', 1)
                    if len(split_result) > 1:
                        text_after_colon = split_result[1].strip()
                        combined_text += f"{lang}: {text_after_colon}\n"
                    else:
                        combined_text += f"{lang}: {lines[line_number-1]}"
                else:
                    print(f"文件 {lang} 行号 {line_number} 超出文件范围")
    
    # 打印整合的文本
    print(combined_text)

# 指定文件夹路径和要提取的行号
folder_path = "E:/apex素材/subtitles"
line_number_to_extract = 22325

# 调用函数
extract_lines_from_txt(folder_path, line_number_to_extract)
