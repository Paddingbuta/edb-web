import pymysql
from flask import Flask, request, jsonify, session, make_response 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 启用 CORS

@app.route('/', methods=["GET","POST"])
def select():
    # Get the data from the request payload
    data = request.get_json()

    # Access the selected option and other data
    input_value = data.get('inputValue')
    selected_option = data.get('selectedOption')

    if input_value == '':
        select_str = "SELECT * FROM poc_test"
    elif selected_option == 'cve-id':
        select_str = "SELECT * FROM poc_test WHERE CVE_ID = '" + input_value +"'"
    else: 
        select_str = "SELECT * FROM poc_test WHERE "+ selected_option+" LIKE '%" + input_value + "%'"
    
    print(select_str)
    db = pymysql.connect(host='localhost', user='root', password='20030507oy', database='poc', charset='utf8mb4')

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

    # 打印每一行数据
    for row in results:
        print(row)

    # 关闭游标
    cursor.close()

    db.close()

    data = []
    columns = [desc[0] for desc in cursor.description]

    for row in results:
        data.append(dict(zip(columns, row)))

    return jsonify(data)

if __name__ == '__main__':
    app.run()