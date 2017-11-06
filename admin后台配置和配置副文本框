#数据库相关
## 1.指定验证模式
```
setting.py      文件中

# 自定义用户model
AUTH_USER_MODEL = 'blog.User'
```


## 2.需要设置mysql的字符集
```
mysql> create database blog character set utf8;
```

## 3.需要安装pillow
```
pip install Pillow
```


## 4.创建超级用户
```
python manage.py createsuperuser
```


# 后台配置
## 1.注册显示在后台-admin.py
```
from django.contrib import admin
from blog.models import *

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'desc', 'click_count',)
    list_display_links = ('title', 'desc', )
    list_editable = ('click_count',)

    fieldsets = (
        (None, {
            'fields': ('title', 'desc', 'content', 'user', 'category', 'tag', )
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields': ('click_count', 'is_recommend',)
        }),
    )


admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)
```


# 配置副文本编辑器
## 1.使用django自带的第三方库
```
django-ckeditor
```

## 2.在admin中定义wigdet

## 3.自定义
### 1.下载kindeditor
1.下载
2.解压放在
```
/home/xiongzhibiao/github/myblog/static/js/kindeditor-4.1.10
```

### 2.配置kindediter-大小外观
```
cat /home/xiongzhibiao/github/myblog/static/js/kindeditor-4.1.10/config.js

KindEditor.ready(function(K) {
        #这儿就是选择要让那个tag显示为副文本框
        K.create('textarea[name=content]',{
                                    width:'800px',
                                    height:'200px',
                                    uploadJson: '/admin/upload/kindeditor',
                      });
});

```


### 3.定义ModelAdmin-admin.py
```
# -*- coding:utf-8 -*-
from django.contrib import admin
from models import *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'desc', 'click_count',)
    list_display_links = ('title', 'desc', )
    list_editable = ('click_count',)

    fieldsets = (
        (None, {
            'fields': ('title', 'desc', 'content', 'user', 'category', 'tag', )
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields': ('click_count', 'is_recommend',)
        }),
    )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )
```




### 3.修改编辑器配置


