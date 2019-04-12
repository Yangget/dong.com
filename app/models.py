# -*- coding: utf-8 -*-
"""
 @Time    : 19-4-5 下午1:34
 @Author  : yangzh
 @Email   : 1725457378@qq.com
 @File    : forms.py
"""
import datetime
from sqlalchemy import Table,Column,Integer,String,Boolean,ForeignKey,DateTime,Text
from sqlalchemy.orm import relationship
from flask_appbuilder import Model

# 地点信息表
class Address(Model):
    id = Column(Integer,primary_key=True)
    full_name = Column(String(100),nullable=False)
    introduction = Column(Text(250),nullable=False)
    location = Column(Text(250),nullable=False)
    route = Column(Text(250),nullable=False)

    def __repr__(self):
        return self.full_name

# 人流量表
class Traffic(Model):
    id = Column( Integer , ForeignKey( 'address.id' ) , nullable=False )
    address = relationship( 'Address' )
    time = Column(DateTime,nullable=False,primary_key=True)
    count = Column(Integer,nullable=False)
    map = Column(Text(1000),nullable=False)
    scatter = Column(Text(1000),nullable=True)

    def __repr__(self):
        return str(self.count)


# 异常事件表
class Event(Model):
    id = Column( Integer , ForeignKey( 'address.id' ) , nullable=False )
    address = relationship( 'Address' )
    number = Column(Integer,primary_key=True)
    time_ = Column(DateTime,ForeignKey('traffic.time'),nullable=False)
    traffic = relationship( 'Traffic' )
    # count = Column(Integer,ForeignKey('traffic.count'),nullable=False)
    # traffic = relationship( 'Traffic' )
    message = Column(Text(500),nullable=False)
    deal = Column(Boolean,nullable=False)

    def __repr__(self):
        return str(self.time)

class Security(Model):
    number = Column(Integer,primary_key=True)
    id = Column( Integer , ForeignKey( 'address.id' ) )
    name = Column(String(50))

    def __repr__(self):
        return self.number



