# coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from common_utils.models import CommonModel
from .variables import GENDER, INCOME, MARRY_STATE, INDUSTRY, PROFESSION, THREE_STATE, BODY_SHAPE, STAR_SIGN, NATION, EDUCATION


class UserInfo(CommonModel):
    user = models.OneToOneField(User)
    gender = models.CharField(choices=GENDER, default="M", verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    height = models.SmallIntegerField(verbose_name="身高")
    birthday = models.DateField(verbose_name="出生日期")
    enable = models.BooleanField(default=True, verbose_name="是否可用")
    live_location = models.CharField(verbose_name="现居住地")
    birth_location = models.CharField(verbose_name="籍贯", default="")
    educational_background = models.CharField(verbose_name="学历", choices=EDUCATION, default="-1")
    industry = models.CharField(verbose_name="从事行业", choices=INDUSTRY, default="-1")
    occupation = models.CharField(verbose_name="职业", choices=PROFESSION, default="-1")
    year_income = models.CharField(verbose_name="年收入", choices=INCOME, default="-1")
    email = models.EmailField(blank=True, null=True, verbose_name="邮箱")
    marry_state = models.CharField(verbose_name="婚姻状况", choices=MARRY_STATE, default="-1")
    has_children = models.CharField(verbose_name="是否有小孩", choices=THREE_STATE, default='-1')
    has_house = models.CharField(verbose_name="是否有房", choices=THREE_STATE, default='-1')
    has_car = models.CharField(verbose_name="是否有车", choices=THREE_STATE, default='-1')
    weight = models.IntegerField(verbose_name='体重', default=0)
    shape = models.CharField(verbose_name='体型', choices=BODY_SHAPE, default='-1')
    is_smoking = models.CharField(verbose_name='是否吸烟', choices=THREE_STATE, default='-1')
    star_sigh = models.CharField(verbose_name='星座', choices=STAR_SIGN, default="-1")
    nation = models.CharField(verbose_name='民族', choices=NATION, default="-1")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"


class DesireCondition(CommonModel):
    user = models.OneToOneField(User)
    age = models.CharField(verbose_name="年龄", default='不限')
    height = models.CharField(verbose_name="身高", default='不限')
    enable = models.BooleanField(default=True, verbose_name="是否可用")
    live_location = models.CharField(verbose_name="现居住地", default='不限')
    birth_location = models.CharField(verbose_name="籍贯", default='不限')
    educational_background = models.CharField(verbose_name="学历", )
    industry = models.CharField(verbose_name="从事行业", choices=INDUSTRY, default="-1")
    occupation = models.CharField(verbose_name="职业", choices=PROFESSION, default="-1")
    year_income = models.CharField(verbose_name="年收入", choices=PROFESSION, default="-1")
    marry_state = models.CharField(verbose_name="婚姻状况", choices=MARRY_STATE, default="-1")
    has_children = models.CharField(verbose_name="是否有小孩", choices=THREE_STATE, default='-1')
    has_house = models.CharField(verbose_name="是否有房", choices=THREE_STATE, default='-1')
    has_car = models.CharField(verbose_name="是否有车", choices=THREE_STATE, default='-1')
    weight = models.IntegerField(verbose_name='体重', default=0)
    shape = models.CharField(verbose_name='体型', choices=BODY_SHAPE, default='-1')
    is_smoking = models.CharField(verbose_name='是否吸烟', choices=THREE_STATE, default='-1')
    star_sigh = models.CharField(verbose_name='星座', choices=STAR_SIGN, default="-1")
    nation = models.CharField(verbose_name='民族', choices=NATION, default="-1")

    class Meta:
        verbose_name = "婚恋理想条件"
        verbose_name_plural = "婚恋理想条件"


class UserImage(CommonModel):
    user = models.ForeignKey(User)
    enable = models.BooleanField(default=True, verbose_name="是否可用")
    url = models.URLField(verbose_name="图片路径")


class IDCard(CommonModel):
    user = models.OneToOneField(User)
    user_name = models.CharField(verbose_name="姓名", )
    number = models.CharField(verbose_name="身份证号")
    is_authenticated = models.BooleanField(default=False, verbose_name="是否认证")


class PhoneInfo(CommonModel):
    user = models.OneToOneField(User)
    phone_number = models.CharField(verbose_name="手机号")
    brand = models.CharField(verbose_name="手机品牌")
    phone_model = models.CharField(verbose_name="手机型号")
    system = models.CharField(verbose_name="手机系统")
    platform = models.CharField(verbose_name="手机平台")
    version = models.CharField(verbose_name="微信版本")
    SDKVersion = models.CharField(verbose_name="sdk版本")


class LoginToken(CommonModel):
    user = models.OneToOneField(User)
    token = models.CharField(verbose_name="口令")
    expire_time = models.DateTimeField(verbose_name="过期时间")


class WeChatInfo(CommonModel):
    user = models.OneToOneField(User)
    open_id = models.CharField(verbose_name="open_id")
    session_key = models.CharField(verbose_name="session_key")
    unionId = models.CharField(verbose_name="unionId")
    nick_name = models.CharField(verbose_name='昵称')

