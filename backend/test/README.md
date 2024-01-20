数据库的创建指令：
# poc_test为数据库名字，自己更改即可
CREATE TABLE poc_test (
    own_ID INT AUTO_INCREMENT PRIMARY KEY,
    trigger_method TEXT,
    test_platform VARCHAR(1000),
    software_version VARCHAR(1000),
    record VARCHAR(1000),
    title VARCHAR(3000),
    author VARCHAR(1000),
    code_language VARCHAR(1000),
    reference VARCHAR(3000),
    time DATE,
    tag VARCHAR(10),
    CVE_ID VARCHAR(1000),
    bugid VARCHAR(1000) UNIQUE,
    source VARCHAR(1000),
    other_information LONGTEXT
);

文件一 add_poc.py:向数据库插入数据
    own_ID  主键 每个CVE的序号
    trigger_method  暂时为空
    test_platform   json中的os属性 
    software_version    内容为product和hardware 用&连接
    record  暂时为空
    title   json中Summary属性
    author  作者名字
    code_language   暂时为空
    reference   attachment属性的列表
    time    时间
    tag 暂时为空
    CVE_ID  json中cveid属性
    bugid   该属性数据集用不到，用来作为unique防止插入数据重复
    source  全部填充为bugzilla.redhat
    other_information   txt所有内容 用空行连接

文件二 select_test.py:用来查询
详细见注释