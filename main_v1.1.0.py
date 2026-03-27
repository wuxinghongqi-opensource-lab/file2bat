import os
import sys


def file_to_bat(source_paths):
    bat_name = "还原文件.bat"
    work_path = os.getcwd()

    with open(bat_name, "w", encoding="utf-8") as bat:
        bat.write("@echo off\n")
        bat.write("chcp 65001 >nul\n")
        bat.write("setlocal enabledelayedexpansion\n")
        bat.write("title 文件还原工具（Base16/Hex版）\n")
        bat.write("echo 正在还原文件，请稍候...\n\n")

        file_count = 0
        file_info_list = []

        # 第一步：读取文件 → 转 HEX（Base16）
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
                    data = f.read()

                # ===================== 关键修改：Base16(Hex) 编码 =====================
                hex_str = data.hex().upper()  # 生成纯Hex，无空格
                # =====================================================================

                file_info_list.append((rel_path, hex_str))
                print(f"✅ 打包：{rel_path}")
                file_count += 1

        # 第二步：写入 还原逻辑（使用 certutil -decodehex）
        for i, (rel_path, hex_str) in enumerate(file_info_list, 1):
            folder = os.path.dirname(rel_path)
            if folder:
                bat.write(f'md "{folder}" 2>nul\n')

            tmp_file = f"%temp%\\hex_{i}.txt"
            bat.write(f"set \"tmp={tmp_file}\"\n")
            bat.write(f"del \"!tmp!\" 2>nul\n")

            # 拆分Hex行（每行64字符，无空格，纯Hex格式）
            lines = [hex_str[j:j + 64] for j in range(0, len(hex_str), 64)]
            for line in lines:
                # 转义CMD特殊字符
                line = line.replace("%", "%%").replace("^", "^^").replace("&", "^&")
                bat.write(f'>>"!tmp!" echo {line}\n')

            # ===================== 关键修改：decodehex =====================
            # type 4 格式：纯Hex、带空格/无空格都能正常解码
            bat.write(f'certutil -f -decodehex "!tmp!" "{rel_path}" 4 >nul 2>&1\n')
            # ==================================================================

            bat.write(f'del "!tmp!" >nul\n\n')

        bat.write("echo.\n")
        bat.write("echo ✅ 所有文件还原完成！\n")
        bat.write("exit /b\n")

    print(f"\n🎉 生成成功！共打包 {file_count} 个文件")
    print(f"生成文件：{os.path.abspath(bat_name)}")


if __name__ == "__main__":
    print("===== 纯 certutil -decodehex 版（Base16/Hex）=====")
    print("使用方法：直接拖拽 文件/文件夹 到本程序上\n")
    if len(sys.argv) < 2:
        print("❌ 请拖拽文件或文件夹到程序上！")
        os.system("pause")
        sys.exit()
    file_to_bat(sys.argv[1:])