## Config

### S1: Create the environment

condo env: lost_found

Python3.6.10, Django3.0.3



### S2: Git



### S3: 在project中建app

Tools->Run manage.py task->在console里面，`startapp appname` -> add app to settings.py , in INSTALLED_APPS



### S4: 配置mysql

* create database in mysql

````mysql
CREATE DATABASE <dbname> CHARACTER SET utf8;
````

* setting.py

Ref: https://stackoverflow.com/questions/19189813/setting-django-up-to-use-mysql

* 安装mysqlclient package

Ref: https://blog.csdn.net/u012343179/article/details/76146815

```
conda install --name lost_found mysqlclient
```



安装不存在conda中的包

在anaconda-navigator中打开虚拟环境terminal使用pip安装, 这里电话号码就是安装的额外的包https://github.com/stefanfoulis/django-phonenumber-field



## Model

### S5: 在models.py里面建表

创建model

Every time you changed model, you have to migrate that change.

```
makemigrations //db.sqlite3 appears
migrate
```

字段清单https://www.cnblogs.com/lhj588/archive/2012/05/24/2516040.html







### S6: 创建superuser

Username: tester

email: zhiyanr2@illinois.edu

Password:(secret)



### S7: register models in admin.py





## Template

https://courseinfo.ligent.net/2020sp/_illinois/is590wfo/week5.html

add template->create view->add the path in urls.py





### Side notes

you may consider Django views to be the “controllers” and Django templates to be the “views.”





## Controller

https://courseinfo.ligent.net/2020sp/_illinois/is590wfo/week6.html

#### S1:

Move url.py to the application

#### S2:

And in the past url.py, change the ones except the admin, use `include()`

#### S3: refactor the code in views.py from function-based to object-based

also, you need make changes in urls.py