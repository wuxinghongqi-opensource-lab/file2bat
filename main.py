import base64
import os
import sys


def file_to_bat(source_paths):
    bat_name = "还原文件.bat"
    work_path = os.getcwd()

    with open(bat_name, "w", encoding="utf-8") as bat:
        bat.write("@echo off\n")
        bat.write("chcp 65001 >nul\n")
        bat.write("setlocal enabledelayedexpansion\n")
        bat.write("title 文件还原工具\n")
        bat.write("echo 正在还原文件，请稍候...\n\n")

        file_count = 0
        all_b64_blocks = []

        # 第一步：收集所有文件信息和 Base64
        file_info_list = []
        for item in source_paths:
            item = os.path.abspath(item)
            if os.path.isfile(item):
                file_list = [item]
            elif os.path.isdir(item):
                file_list = []
                for root, _, files in os.walk(item):
                    for f in files:
                        file_list.append(os.path.join(root, f))
            else:
                continue

            for file_path in file_list:
                rel_path = os.path.relpath(file_path, work_path).replace("/", "\\")
                with open(file_path, "rb") as f:
                    b64_str = base64.b64encode(f.read()).decode("utf-8")
                file_info_list.append((rel_path, b64_str))
                print(f"✅ 打包：{rel_path}")
                file_count += 1

        # 第二步：写入还原逻辑（先写命令，再写数据）
        for i, (rel_path, b64_str) in enumerate(file_info_list, 1):
            folder = os.path.dirname(rel_path)
            if folder:
                bat.write(f'md "{folder}" 2>nul\n')

            # 将 Base64 写入临时文件（通过 echo 追加）
            tmp_file = f"%temp%\\b64_{i}.txt"
            bat.write(f"set \"tmp={tmp_file}\"\n")
            bat.write(f"del \"{tmp_file}\" 2>nul\n")

            # 分多行 echo 到临时文件（每行 <= 8191 字符）
            lines = [b64_str[j:j + 8000] for j in range(0, len(b64_str), 8000)]
            for line in lines:
                # 转义特殊字符（如 %, !, ^, &）
                line = line.replace("%", "%%").replace("^", "^^").replace("&", "^&").replace("<", "^<").replace(">",
                                                                                                                "^>")
                bat.write(f'>>"!tmp!" echo {line}\n')

            # 添加 PEM 头尾
            bat.write(f'(echo -----BEGIN CERTIFICATE-----)> "!tmp!.pem"\n')
            bat.write(f'type "!tmp!" >> "!tmp!.pem"\n')
            bat.write(f'(echo -----END CERTIFICATE-----)>> "!tmp!.pem"\n')
            bat.write(f'certutil -f -decode "!tmp!.pem" "{rel_path}" >nul 2>&1\n')
            bat.write(f'del "!tmp!" "!tmp!.pem" >nul\n\n')

        bat.write("echo.\n")
        bat.write("echo ✅ 所有文件还原完成！\n")
        bat.write("pause >nul\n")
        bat.write("exit /b\n")

    print(f"\n🎉 生成成功！共打包 {file_count} 个文件")
    print(f"生成文件：{os.path.abspath(bat_name)}")
    os.system("pause")


if __name__ == "__main__":
    print("===== 纯 certutil 版（无 PowerShell，100% 兼容）=====")
    print("使用方法：直接拖拽 文件/文件夹 到本程序上\n")
    if len(sys.argv) < 2:
        print("❌ 请拖拽文件或文件夹到程序上！")
        os.system("pause")
        sys.exit()
    file_to_bat(sys.argv[1:])