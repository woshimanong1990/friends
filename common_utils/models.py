# coding:utf-8
from django.db import models


class CommonModel(models):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    enable = models.BooleanField(default=False, verbose_name="是否可用")
