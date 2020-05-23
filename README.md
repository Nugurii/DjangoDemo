# <font face="Consolas" size=7>说明文档</font>

<font face="Consolas">韩佳乐 PB16051152</font>

***

## <font face="Consolas" size=5>工具</font>

<font face="Consolas">

`python`==3.7<br>
`django`==2.2<br>
`djangorestframework`==3.11.0<br>
`djangorestframework-jwt`==1.11.0<br>
`mysqlclient`==1.4.6<br>
`mysql`==8.0.20<br>

</font>

## <font face="Consolas" size=5>部署</font>

<font face="Consolas">

1. 安装 `django`

```c
pip install django==2.2
```

2. 安装 `djangorestframework`

```c
pip install djangorestframework
```

3. 安装 `djangorestframework-jwt`

```c
pip install djangorestframework-jwt
```

4. 安装 `mysqlclient`

```c
pip install mysqlclient
```

5. 修改 `DjangoDemo\settings.py` 数据库配置。使用 `root` 账户登录 `mysql` ，新建数据库 `django_mysql`（数据库名可以修改，但应和 `NAME` 保持一致）。其次，将 `PASSWORD` 修改为你的数据库密码。`HOST` 和 `PORT` 无需改动。

```c
DATABASES = { 'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'django_mysql',  #  --> 新建数据库
    'USER': 'root',
    'PASSWORD': '',          #  --> 修改为你的密码
    'HOST': '127.0.0.1',
    'PORT': '3306',
    }
}
```

6. 数据库迁移。在根目录下执行

```c
python manage.py makemigrations
python manage.py migrate
```

7. 运行项目。在根目录下执行

```c
python manage.py runserver
```

</font>

## <font face="Consolas" size=5>代码风格约定</font>

<font face="Consolas">

`pylint`==2.5.0

</font>

## <font face="Consolas" size=5>后端接口说明</font>

1. `/api/home`，接受的参数为 `json` 字符串，返回格式为`json`。

    <table align="center">
        <tr>
            <td><center><img src="https://img-blog.csdnimg.cn/20200510120640461.PNG" width="400">登录前</center></td>
            <td><center><img src="https://img-blog.csdnimg.cn/20200510122040790.PNG" width="400">登录后</center></td>
        </tr>
    </table>

2. `/api/user/signin`，接受的参数为`json`字符串，返回格式为`json`。若登录失败，后端返回 `Incorrect username or password.`；若登录成功，后端通过 `jwt` 生成`token`，**有效期为3分钟**，并直接跳转至 `home` 页面，右上角显示用户信息。

    <table align="center">
        <tr>
            <td><center><img src="https://img-blog.csdnimg.cn/20200510120640465.PNG" width="400">登录页面</center></td>
            <td><center><img src="https://img-blog.csdnimg.cn/20200510122040804.PNG" width="400">登录失败</center></td>
        </tr>
    </table>

3. `/api/user/signup`，接受的参数为`json`字符串，返回格式为`json`。若注册失败，后端返回 `Username is already taken`；若注册成功，后端返回 `Sign up successfully!`。

    <table align="center">
        <tr>
            <td><center><img src="https://img-blog.csdnimg.cn/20200510122040792.PNG" width="400">注册成功</center></td>
            <td><center><img src="https://img-blog.csdnimg.cn/20200510122040795.PNG" width="400">注册失败</center></td>
        </tr>
    </table>

4. `/api/token-verify`，接受的参数为`json`字符串，返回格式为`json`。用于验证 token。
