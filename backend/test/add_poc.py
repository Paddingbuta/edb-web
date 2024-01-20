import ast
import pymysql
import os

# 连接数据库，user password database 都按照自己数据库实际名字更改
db = pymysql.connect(host='localhost', user='root', password='20030507oy', database='poc', charset='utf8mb4')
print('数据库连接成功！')

# 存档所有CVE文件夹的目录路径
directory = '../poc'
# 遍历得到所有CVE文件夹的路径
folder_paths = [root for root, dirs, files in os.walk(directory)][1:]
for folder_path in folder_paths:
    folder_path = folder_path.replace('/', '\\')
    print(folder_path)

    other_information = ""
    trigger_method = ""
    test_platform = ""
    software_version = ""
    record = ""
    title = ""
    author = ""
    code_language = ""
    reference = ""
    time = ""
    tag = ""
    CVE_ID = ""
    source = ""
    bugid = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding='utf-8') as file:
                file_content = file.read()
                other_information += file_content + "\n"
        elif filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding='utf-8') as file:
                file_content = file.read()
                data = ast.literal_eval(file_content)
                trigger_method = ""
                test_platform = data['os']
                software_version = data['product'] + '&' + data['hardware']
                record = ""
                title = data['summary']
                author = data.get('reported_date', '').split('by')[1] if 'reported_date' in data else ''
                code_language = ""
                reference = data['attachment']  # attchment是个link列表
                time = data['reported_date'].split(' ')[0]
                tag = ""
                CVE_ID = ' '.join(data['cveid'])  # 将所有cve_id用空格连在一起
                bugid = data['bugid'] # 该属性数据集用不到，用来作为unique防止重复
                source = "bugzilla.redhat"

    other_information = '"' + str(other_information) + '"'
    reference = '"' + str(reference) + '"'

    try:
        cursor = db.cursor()
        insert_str = "insert into poc_test(trigger_method, test_platform, software_version, record, title, author, code_language, reference, time, tag, CVE_ID, bugid, source, other_information) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        db.set_charset('utf8mb4')
        cursor.execute("SET NAMES utf8mb4;")
        cursor.execute("SET CHARACTER SET utf8mb4;")
        cursor.execute("SET character_set_connection=utf8mb4;")
        cursor.execute(insert_str, (
            trigger_method, test_platform, software_version, record, title, author, code_language, reference, time, tag,
            CVE_ID, bugid,
            source, other_information.encode))
        db.commit()
        cursor.close()
        print('victory')
    except Exception as e:
        print(str(CVE_ID) + "发生错误" + str(e))
