import os
import zipfile

def unzip_and_stat(raw_logs_path="logs"):
    for file in os.listdir(raw_logs_path):
        if file.endswith(".zip"):
            zip_path = os.path.join(raw_logs_path, file)
            folder_name = os.path.splitext(file)[0]
            extract_path = os.path.join(raw_logs_path, folder_name)

            # 解压 zip 文件
            if not os.path.exists(extract_path):
                os.makedirs(extract_path)
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_path)
                print(f"解压完成: {file} → {folder_name}/")
            else:
                print(f"已存在跳过解压: {folder_name}/")

            # 统计解压后的文件夹大小
            total_size = 0
            for root, dirs, files in os.walk(extract_path):
                for f in files:
                    fp = os.path.join(root, f)
                    total_size += os.path.getsize(fp)

            print(f"{folder_name} 解压后大小: {total_size / (1024 * 1024):.2f} MB\n")

if __name__ == "__main__":
    unzip_and_stat("logs")