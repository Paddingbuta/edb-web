import pymysql
from flask import Flask, request, jsonify, session, make_response
from flask_cors import CORS

# from flask_compress import Compress

app = Flask(__name__)
CORS(app)  # 启用 CORS
hostip = "127.0.0.1"
psd = "123456"


@app.route("/", methods=["GET", "POST"])
def select():
    # Get the data from the request payload
    data = request.get_json()

    # Access the selected option and other data
    input_value = data.get("inputValue")
    selected_option = data.get("selectedOption")
    if selected_option == "getdetails":
        select_str = (
            "SELECT other_information FROM poc_test WHERE own_ID='"
            + str(input_value)
            + "'"
        )
        print(select_str)
        db = pymysql.connect(
            host=hostip, user="root", password=psd, database="poc", charset="utf8mb4"
        )
        cursor = db.cursor()
        cursor.execute(select_str)
        columns = [desc[0] for desc in cursor.description]
        results = cursor.fetchall()
        cursor.close()
        db.close()
        data = []
        for row in results:
            data.append(dict(zip(columns, row)))
        print(jsonify(data))
        return jsonify(data)

    if input_value == "":
        select_str = "SELECT own_ID,test_platform,software_version,title,author,reference,time,CVE_ID,source FROM poc_test"
    elif selected_option == "cve-id":
        select_str = (
            "SELECT own_ID,test_platform,software_version,title,author,reference,time,CVE_ID,source FROM poc_test WHERE CVE_ID LIKE '%"
            + input_value
            + "%'"
        )
    elif selected_option == "software":
        select_str = (
            "SELECT own_ID,test_platform,software_version,title,author,reference,time,CVE_ID,source FROM poc_test WHERE software_version LIKE '%"
            + input_value
            + "%'"
        )
    elif selected_option == "platform":
        select_str = (
            "SELECT own_ID,test_platform,software_version,title,author,reference,time,CVE_ID,source FROM poc_test WHERE test_platform LIKE '%"
            + input_value
            + "%'"
        )
    else:
        select_str = (
            "SELECT own_ID,test_platform,software_version,title,author,reference,time,CVE_ID,source FROM poc_test WHERE "
            + selected_option
            + " LIKE '%"
            + input_value
            + "%'"
        )

    print(select_str)
    db = pymysql.connect(
        host=hostip, user="root", password=psd, database="poc", charset="utf8mb4"
    )

    # 创建游标对象
    cursor = db.cursor()
    # 执行SELECT查询
    cursor.execute(select_str)
    # 获取查询结果的属性信息
    columns = [desc[0] for desc in cursor.description]
    # 打印属性列
    print(columns)
    # 获取查询结果
    results = cursor.fetchall()
    print(f"find {len(results)} result(s)")
    # 关闭游标
    cursor.close()

    db.close()

    data = []
    columns = [desc[0] for desc in cursor.description]

    for row in results:
        data.append(dict(zip(columns, row)))

    return jsonify(data)


# 添加跨域支持
@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    return response


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
