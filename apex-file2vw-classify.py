def convert_to_sections(input_text):
    lines = input_text.split('\n')
    output_text = ""

    current_section = ""
    for line in lines:
        if line.startswith('{{APEXAudio|'):
            # Extracting information from the line
            parts = line.strip('{}').split('|')
            name = parts[1].split('=')[1]
            audio_type = parts[2].split('=')[1]
            num = parts[3].split('=')[1]
            q = parts[4].split('=')[1]
            zh = parts[5].split('=')[1]

            # Checking if a new section is starting
            if current_section != audio_type:
                if current_section != "":
                    output_text += "=== 跳伞动作语音 ===\n"
                output_text += f"=== 我是{audio_type} ===\n"
                current_section = audio_type

            # Constructing the new line
            output_text += f"{{APEXAudio|name={name}|type={audio_type}|num={num}|q={q}|zh={zh}}}\n"

    # Adding the last section
    if current_section != "":
        output_text += "=== 跳伞动作语音 ===\n"

    return output_text.strip()

# 输入的文本
input_text = """
{{APEXAudio|name=ash|type=bc_imJumpmaster|num=01|q=2|zh=}}
{{APEXAudio|name=ash|type=bc_imJumpmaster|num=02|q=2|zh=}}
{{APEXAudio|name=ash|type=bc_imJumpmaster|num=03|q=2|zh=}}
{{APEXAudio|name=ash|type=bc_imJumpmaster|num=04|q=2|zh=}}
{{APEXAudio|name=ash|type=bc_imJumpmaster|num=05|q=3|zh=}}
{{APEXAudio|name=ash|type=bc_podLeaderLaunch|num=01|q=2|zh=}}      
{{APEXAudio|name=ash|type=bc_podLeaderLaunch|num=02|q=2|zh=}}      
{{APEXAudio|name=ash|type=bc_podLeaderLaunch|num=03|q=3|zh=}}      
{{APEXAudio|name=ash|type=bc_skydive|num=01|q=2|zh=}}
{{APEXAudio|name=ash|type=bc_skydive|num=02|q=2|zh=}}
{{APEXAudio|name=ash|type=bc_skydive|num=03|q=2|zh=}}
{{APEXAudio|name=ash|type=bc_skydive|num=04|q=2|zh=}}
{{APEXAudio|name=ballistic|type=bc_imJumpmaster|num=01|q=3|zh=}}   
{{APEXAudio|name=ballistic|type=bc_imJumpmaster|num=02|q=3|zh=}}   
{{APEXAudio|name=ballistic|type=bc_imJumpmaster|num=03|q=3|zh=}}   
{{APEXAudio|name=ballistic|type=bc_imJumpmaster|num=04|q=3|zh=}}   
{{APEXAudio|name=ballistic|type=bc_podLeaderLaunch|num=01|q=3|zh=}}
{{APEXAudio|name=ballistic|type=bc_podLeaderLaunch|num=02|q=2|zh=}}
{{APEXAudio|name=ballistic|type=bc_skydive|num=01|q=3|zh=}}
{{APEXAudio|name=ballistic|type=bc_skydive|num=02|q=3|zh=}}
"""

# 转换文本并打印输出
output_text = convert_to_sections(input_text)
print(output_text)
