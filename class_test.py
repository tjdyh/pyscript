#!/usr/bin/env python

from fabric import Connection
from pprint import pprint

class AloneCon:
    def __init__(self,host,port,username,password):
        self.host = host
        self.port = host
        self.username = username
        self.password = password
    def a_conn(self):
        conn = Connection(host=self.host,port=self.port,user=self.username,connect_kwargs={'password':self.password})
        pprint("test")
        return conn

if __name__ == '__main__':
    # abc = AloneCon('192.168.88.75',22,'root','123456')
    abc = AloneCon()
    aaa = abc.a_conn()
    pprint(type(aaa))