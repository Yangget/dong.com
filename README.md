  # Dong.com
  ------------------------------------------------------------------------
  ## - Install it:
  
  ```python
      # 克隆该项目
      git clone https://github.com/Yangget/dong.com.git
      # 进入项目目录
      cd dong.com/PeoFlow
      # 安装依赖(建议创建虚拟环境,可以[参考](https://flask-appbuilder.readthedocs.io/en/latest/installation.html],不创建虚拟环境影响不大)
      pip install requirements.txt
  ```
  
  ## - Run it 
  -使用初始化好的密码可用:
  ```python
      fabmanager run
  ```
  然后在浏览器查看http://0.0.0.0:8080/
  账号:yangdd
  密码:11111111
  
  -重新创建管理员可用(在当前目录下使用命令行):
  ```python
      fabmanager create-admin      
  ```
  按照提示输入,录入Sql库中,接下来同上操作
  
  __________________________________________________________________________
  
  ## - Read it
  
  -同目录下有doc文档,对自带的api,jinjia引擎有大概的介绍,详细的文档移步[flask-appbuilder](https://flask-appbuilder.readthedocs.io/en/latest/intro.html)
  
  -张小羽多负责前端api得书写(记得要熟悉fkask,还有jinjia),常小乐负责具体视图层的业务,主要为图表,张小然负责前端整体的UI布局.请前端的小朋友给张小羽书写所需的完整的api文档(不用过于复杂,描述清楚需要后端西游提供什么即可),可参考如下:
  
-------------------------------------------------------------------
接口名称 （这个接口是干什么用的）

接口描述

简单的描述一下这个接口提供什么样的服务，主要是针对哪个功能

接口参数

此处标明接口输出参数类型和描述

 序号         |  变量名称	     | 类型	         | 描述
:----------- | :-----------: | -----------: | -----------:
1	           |   space	     | String	      | domain 的名称
2	           |   userId      | Integer      | 用户ID
3	           |   name	       | String	      | 查询的名称

接口请求地址

http://192.168.1.26/company/search/

接口请求 方式 GET/POST/DELETE/PUT/

##响应数据

###成功时返回数据

{
     success:true,
     result:{
        msg:'',
        data:[]
     }
}
###失败时返回数据

{
    success:false,
    result:{
        msg:'',
        data:[]
    }
}
____________________________________________________________________________
## Look it
我选了几个不错的开源web软件,可以供张小然,常小乐参考
图表类:
- https://github.com/mher/chartkick.py 实现过程非常简单,
- 

整体UI:

- https://github.com/osroom/osroom 界面风格好看,有需要我们可以增加Mongd来支持
- https://github.com/521xueweihan/hellogithub.com 重要参考对象,界面简单,代码公开
- https://github.com/grupydf/malt 可以参考主界面,页脚等

视频流处理:

- https://github.com/log0/video_streaming_with_flask_example

其他方面:

- https://github.com/hack4impact/flask-base 基于flask的其他项目
____________________________________________________________________________
## Do it
后端已经实现用户注册,以及用户权限和控制,前端页面设计待再整合一下资源后同意商量决定.
实现功能如下(按重要型排序):
 
1.可以实时的PLC

2.可以预测,展示下一时间段内的PLC情况

3.可以自定义阀值,超过阀值预警.

4.统计PLC异常情况,并形成历史记录

5.P的动态跟踪,以及轨迹预测

6.情境数据存库,如地点信息,天气,安保

7.多适配摄像头

8.边云协作

____________________________________________________________________________

## Insist it

精彩还未开始......
