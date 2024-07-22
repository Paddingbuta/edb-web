import ast
import pymysql
import os

# 连接数据库，user password database 都按照自己数据库实际名字更改
db = pymysql.connect(
    host="172.18.0.3", user="root", password="123456", database="poc", charset="utf8mb4"
)
print("数据库连接成功！")

# 存档所有CVE文件夹的目录路径
directory = "../poc"
# 遍历得到所有CVE文件夹的路径
folder_paths = [root for root, dirs, files in os.walk(directory)][1:]
for folder_path in folder_paths:
    folder_path = folder_path.replace("\\", "/")
    print(folder_path)

    other_information = ""
    test_platform = ""
    software_version = ""
    title = ""
    author = ""
    reference = ""
    time = ""
    CVE_ID = ""
    source = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                file_content = file.read()
                other_information += file_content + "\n"
        elif filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                file_content = file.read()
                data = ast.literal_eval(file_content)
                test_platform = data["os"]
                # software_version = data['product'] + '&' + data['hardware']
                software_version = data["product"]
                title = data["summary"]
                author = (
                    data.get("reported_date", "").split("by")[1]
                    if "reported_date" in data
                    else ""
                )
                reference = data["attachment"][0].strip("[]")  # attchment是个link列表
                time = data["reported_date"].split(" ")[0]
                CVE_ID = " ".join(data["cveid"])  # 将所有cve_id用空格连在一起
                # bugid = data['bugid'] # 该属性数据集用不到，用来作为unique防止重复
                source = "bugzilla.redhat"

    other_information = '"' + str(other_information) + '"'
    reference = str(reference)

    try:
        cursor = db.cursor()
        insert_str = "insert into poc_test(test_platform, software_version, title, author, reference, time, CVE_ID,  source, other_information) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        db.set_charset("utf8mb4")
        cursor.execute("SET NAMES utf8mb4;")
        cursor.execute("SET CHARACTER SET utf8mb4;")
        cursor.execute("SET character_set_connection=utf8mb4;")
        cursor.execute(
            insert_str,
            (
                test_platform,
                software_version,
                title,
                author,
                reference,
                time,
                CVE_ID,
                source,
                other_information,
            ),
        )
        db.commit()
        cursor.close()
        print("victory")
    except Exception as e:
        print(str(CVE_ID) + "发生错误" + str(e))
