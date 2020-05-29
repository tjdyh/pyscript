from fabric import Connection
from fabric import task
from pprint import pprint
from fabric import transfer

@task
def hello_world(c):
    print("Hello world!")

@task
def test_host(c):
    con = Connection('192.168.88.75',user='root',connect_kwargs={'password':'123456'})
    con.run("uname -a")

@task
def remote_host(c):
    host = input("请输入主机参数：")
    port = input("请输入端口参数：")
    passwd = input("请输入密码参数：")
    pprint("%s,%s" %(host, port))
    con = Connection(host, user='root', port=port, connect_kwargs={'password': passwd})
    con.run("uname -a")
    tran = transfer.Transfer(con)
    tran.put("/tmp/Python-3.7.0.tgz", "/tmp")
    pprint("完成上传！")