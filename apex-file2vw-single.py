import os

def get_file_names(folder_path):
    try:
        # 获取文件夹下所有文件名
        file_names = os.listdir(folder_path)
        return file_names
    except FileNotFoundError:
        print(f"指定的文件夹路径不存在: {folder_path}")
        return []

def compare_and_count(file_names):
    count_dict = {}
    last_condition_name = None
    last_character_name = None

    for file_name in file_names:
        # 使用下划线 "_" 分割文件名
        parts = file_name.split('_')

        # 获取条件名和人物名
        if parts[-3]==parts[5]:
            condition_name = parts[4] +'_'+ parts[-3]  # 取到倒数第四个下划线之前的部分
        else:
            condition_name = parts[4] +'_' + parts[5] +'_'+ parts[-3]  # 取到倒数第四个下划线之前的部分
        character_name = parts[2]

        # 获取关键部分
        key = f"{condition_name}_{character_name}"

        # 统计文件个数
        count_dict[key] = count_dict.get(key, 0) + 1

        # 更新最后一次的条件名和人物名
        last_condition_name = condition_name
        last_character_name = character_name

    return count_dict, last_condition_name, last_character_name  # 将condition_name和character_name一起返回

if __name__ == "__main__":
    # 指定文件夹路径
    folder_path = "E:/apex素材/sounds"

    # 获取文件名列表
    file_names = get_file_names(folder_path)

    # 比较文件名并统计
    count_result, last_condition_name, last_character_name = compare_and_count(file_names)

    # 输出结果
    for key, count in count_result.items():
        condition_name, character_name = key.rsplit('_', 1)  # 从key中提取condition_name和character_name
        type = condition_name[:-3]
        num = condition_name.split('_')[-1]
        if num == '01':
            if type == 'imJumpmaster':
                title = '{{Back|（APEX英雄）|}}\n== 跳伞 ==\n=== 我是跳伞指挥官 ===\n'
            elif type == 'podLeaderLaunch':
                title = '=== 作为跳伞指挥官跳伞 ===\n'
            elif type == 'skydive':
                title = '=== 跳伞动作语音 ===\n'
            else:
                title = ''
        else:
            title = ''

        if count == 2:
            print(f"{title}{{{{APEXAudio|name={character_name}|type=bc_{type}|num={num}|q=2|zh=}}}}")
        elif count == 1:
            print(f"{title}{{{{APEXAudio|name={character_name}|type=bc_{type}|num={num}|q=1|zh=}}}}")
        elif count == 4:
            print(f"{title}{{{{APEXAudio|name={character_name}|type=bc_{type}|num={num}|q=4|zh=}}}}")
        elif count == 6:
            print(f"{{{{APEXAudio|name={character_name}|type=bc_{type}|num={num}|q=3|zh=}}}}\n{{{{APEXAudio|name={character_name}|type=bc_{type}|num={num}|q=6|zh=}}}}")
        else:
            print(f"{title}{{{{APEXAudio|name={character_name}|type=bc_{type}|num={num}|q=3|zh=}}}}")
    
    # 在循环之外输出最后一次的条件名和人物名
    print(f"Last Condition Name: {last_condition_name}")
    print(f"Last Character Name: {last_character_name}")
