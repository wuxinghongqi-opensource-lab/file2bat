# file2bat
# file convert to bat ,if you replace lI0o,you can print it


## 工具简介 | Tool Introduction
一款轻量级脚本工具，可将任意文件（支持拖拽多个文件/文件夹）转换为BAT批处理可识别的Base64字符串格式。该工具输出的原始字符串可直接嵌入批处理脚本使用，无需额外处理；仅当需要将字符串打印至A4纸张进行纸质化保存时，需手动替换Base64中0/O、1/l/I等易混淆字符（避免OCR识别错误）。

BAT脚本支持直接打印输出内容，且转换后的BAT字符串可完整还原任意原文件，由此实现了**用纸保存任意文件**的独特方式。打印保存时推荐优先选择小文件（如短字符串、TXT、DOCX、PPTX等），这类文件转换后的字符串长度适配单张A4纸，不仅节省纸张，更能大幅提升OCR识别的准确率。

A lightweight script tool that converts any file (supports dragging multiple files/folders) into a Base64 string format recognizable by BAT batch processing. The original string output by the tool can be directly embedded into batch scripts for use without additional processing; only when it is necessary to print the string to A4 paper for paper-based storage, it is required to manually replace easily confused characters (such as 0/O, 1/l/I) in Base64 (to avoid OCR recognition errors).

BAT scripts support direct printing of output content, and the converted BAT strings can fully restore any original file, thus realizing a unique way of **saving any file with paper**. For paper storage via printing, it is recommended to prioritize small files (such as short strings, TXT, DOCX, PPTX, etc.), as the converted string length of such files fits a single A4 sheet, which not only saves paper but also greatly improves the accuracy of OCR recognition.

## 核心特性 | Core Features
- 📁 支持多文件/文件夹拖拽批量转换，无需逐个手动选择；
- 📁 Support batch conversion by dragging multiple files/folders (no need to select one by one);
- 🔧 日常使用：输出的原始Base64字符串可直接使用，无需任何字符替换；
- 🔧 Daily Use: The output original Base64 string can be used directly without any character replacement;
- 📄 纸质保存：BAT支持直接打印，手动替换易混淆字符后可打印至A4纸保存任意文件，适配OCR识别与还原；
- 📄 Paper Storage: BAT supports direct printing; after manually replacing easily confused characters, any file can be printed to A4 paper for storage, compatible with OCR recognition and restoration;
- 📑 小文件优选：推荐打印保存小文件（TXT/DOCX/PPTX/短字符串等），单张A4纸即可容纳，OCR识别更精准；
- 📑 Small File Preference: It is recommended to print and save small files (TXT/DOCX/PPTX/short strings, etc.), which can be contained in a single A4 sheet with more accurate OCR recognition;
- 💻 纯本地运行，无需联网，兼容Windows全版本；
- 💻 Run locally without network, compatible with all Windows versions;
- 📝 输出字符串格式规范，兼顾直接使用与纸质保存场景。
- 📝 Output string format is standardized, compatible with both direct use and paper storage scenarios.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# v1.1.0

- 本工具已从 Base64 改版为 Base16 (Hex) 模式，依靠系统原生 certutil 完成编解码，十六进制文本整洁换行、无多余字符，支持直接查看与打印，双击 BAT 即可无损还原所有文件。只包含了0-9,A-F。因此容易ocr。
- This tool has been upgraded from Base64 to Base16 (Hex). It uses Windows native certutil for encoding and decoding. The hex data is neatly wrapped without extra characters, can be viewed and printed directly. Double-click the BAT file to restore all files losslessly.Just contain 0-9,A-F.Therefore, it is easy for OCR.





--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# v1.0.0
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Base64易混淆字符替换清单（仅打印时使用） | Base64 Easily Confused Characters Replacement List (Only for Printing)
仅在需要打印字符串到A4纸时，手动替换以下易混淆字符（日常使用无需替换）：
Only manually replace the following easily confused characters when printing the string to A4 paper (no replacement required for daily use):

| 原始Base64字符 | 建议替换为 | 替换说明 |
|----------------|------------|----------|
| 0（数字零）| ㊀ | 避免与字母O混淆 |
| O（大写字母O） | ㊊ | 避免与数字0混淆 |
| 1（数字一）| ㊁ | 避免与小写字母l/大写字母I混淆 |
| l（小写字母L） | ㊑ | 避免与数字1/大写字母I混淆 |
| I（大写字母I） | ㊒ | 避免与数字1/小写字母l混淆 |
| +（加号）| ㊣ | 避免与数字7/字母t混淆 |
| /（斜杠）| ㊤ | 避免与反斜杠/数字1混淆 |

| Original Base64 Character | Recommended Replacement | Replacement Note |
|---------------------------|-------------------------|------------------|
| 0 (Number zero)           | ㊀                      | Avoid confusion with letter O |
| O (Uppercase letter O)    | ㊊                      | Avoid confusion with number 0 |
| 1 (Number one)            | ㊁                      | Avoid confusion with lowercase l/uppercase I |
| l (Lowercase letter L)    | ㊑                      | Avoid confusion with number 1/uppercase I |
| I (Uppercase letter I)    | ㊒                      | Avoid confusion with number 1/lowercase l |
| + (Plus sign)             | ㊣                      | Avoid confusion with number 7/letter t |
| / (Slash)                 | ㊤                      | Avoid confusion with backslash/number 1 |

## 使用方法 | Usage
### 场景1：日常直接使用（无需替换字符） | Scenario 1: Daily Direct Use (No Character Replacement)
1. 将需要转换的**单个/多个文件**或**文件夹**直接拖拽到脚本文件上；
2. 脚本自动运行，生成包含原始Base64字符串的 `.bat` 文件；
3. 直接将生成的 `.bat` 文件中的字符串嵌入批处理脚本，无需任何修改。

1. Directly drag **single/multiple files** or **folders** to the script file;
2. The script runs automatically and generates a `.bat` file containing the original Base64 string;
3. Directly embed the string in the generated `.bat` file into the batch script without any modification.

### 场景2：打印到A4纸保存（需手动替换字符） | Scenario 2: Print to A4 Paper for Storage (Need Manual Character Replacement)
1. 按「场景1」步骤生成包含原始Base64字符串的 `.bat` 文件；
2. 打开 `.bat` 文件，对照「易混淆字符替换清单」手动替换所有易混淆字符；
3. 利用BAT直接打印功能，将替换后的字符串完整打印至A4纸张（优先选择小文件，单张纸即可保存）；
4. 如需还原文件：
   - 步骤1：通过OCR识别纸张上的字符串；
   - 步骤2：对照替换清单反向还原字符（如㊀→0、㊁→1）；
   - 步骤3：将还原后的Base64字符串解码，即可恢复原文件。

1. Generate a `.bat` file containing the original Base64 string according to the steps in "Scenario 1";
2. Open the `.bat` file and manually replace all easily confused characters with reference to the "Base64 Easily Confused Characters Replacement List";
3. Use the direct printing function of BAT to print the replaced string completely to A4 paper (prioritize small files that can be saved on a single sheet);
4. To restore the file:
   - Step 1: Recognize the string on the paper via OCR;
   - Step 2: Reverse restore the characters with reference to the replacement list (e.g., ㊀→0, ㊁→1);
   - Step 3: Decode the restored Base64 string to recover the original file.

## 注意事项 | Notes
1. 转换大文件（＞100MB）时可能耗时较长，请耐心等待；
1. Converting large files (>100MB) may take a long time, please wait patiently;
2. 文件夹转换会递归处理内部所有文件，生成整合后的BAT字符串；
2. Folder conversion will recursively process all internal files and generate integrated BAT strings;
3. 日常使用无需替换任何字符，仅打印纸质保存时需手动替换易混淆字符；
3. No character replacement is required for daily use, only manual replacement of easily confused characters is needed for paper storage via printing;
4. 打印推荐：优先选择小文件（TXT/DOCX/PPTX/短字符串等）打印，单张A4纸即可容纳，易于OCR识别；
4. Printing Recommendation: Prioritize printing small files (TXT/DOCX/PPTX/short strings, etc.), which can be contained in a single A4 sheet and are easy for OCR recognition;
5. 打印A4纸时请确保字符清晰、无模糊/缺印，推荐分辨率≥300DPI；
5. Ensure characters are clear and free of blurring/missing prints when printing on A4 paper, recommended resolution ≥300DPI;
6. 生成的BAT字符串仅为文本格式转换，不修改原文件内容；
6. The generated BAT string is only text format conversion and does not modify the original file content;
7. OCR识别纸质内容后，需严格对照替换清单反向还原字符，否则无法准确解码恢复原文件。
7. After OCR recognition of paper content, characters must be reversely restored in strict accordance with the replacement list, otherwise the original file cannot be accurately decoded and recovered.

## 兼容性 | Compatibility
- 操作系统：Windows 7/8/10/11（32/64位）；
- Operating System: Windows 7/8/10/11 (32/64-bit);
- 依赖：无需安装额外软件，系统自带CMD/PowerShell即可运行；
- Dependencies: No additional software installation required, runs with the system's built-in CMD/PowerShell;
- 输出编码：UTF-8（确保中英文及特殊替换字符兼容）；
- Output Encoding: UTF-8 (Ensure compatibility with Chinese, English and special replacement characters);
- 打印适配：支持所有可打印A4纸的打印机，BAT可直接触发打印，无特殊硬件要求。
- Printing Compatibility: Supports all printers that can print A4 paper; BAT can directly trigger printing with no special hardware requirements.

### 总结
1. 核心规则：日常使用时，工具输出的Base64字符串可直接使用无需替换；仅打印纸质保存时，需手动替换易混淆字符；
2. 核心价值：借助BAT直接打印能力，实现“用纸保存任意文件”，推荐打印小文件（TXT/DOCX/PPTX等），单张A4纸即可保存且易OCR识别；
3. 双场景流程：日常使用→拖拽转换→直接用；纸质保存→转换→手动替换字符→打印（优选小文件）→OCR识别→反向还原→解码恢复。
