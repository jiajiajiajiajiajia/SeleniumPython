#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   register_business.py
@Time    :   2019/8/29 17:35
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from poModel.handle.register_handle import RegisterHandle
from selenium import webdriver
from time import sleep
from config import setting

class RegisterBusiness(object):
    def __init__(self, driver):
        self.rh = RegisterHandle(driver)

    # 正常注册
    def common_register(self, nickname, register_email, password, re_password, captcha):
        self.rh.send_register_nickname(nickname)
        self.rh.send_register_email(register_email)
        self.rh.send_register_password(password)
        self.rh.send_register_re_password(re_password)
        self.rh.send_register_captcha(captcha)
        self.rh.click_register_btn()

    # 判断注册是否成功
    def success_or_fail(self):
        if self.rh.get_register_btn_text() is None:
            return True
        else:
            return False

    # ddt 通用注册方法
    def register_function(self, nickname, register_email, password, re_password, captcha, assert_code, assert_info):
        self.common_register(nickname, register_email, password, re_password, captcha)
        if self.rh.get_user_text(assert_code, assert_info) is None:
            return True
        else:
            return False
    # 用户名错误
    def register_nickname_error(self, nickname, register_email, password, re_password, captcha):
        self.common_register(nickname, register_email, password, re_password, captcha)
        if self.rh.get_user_text('register_nickname_error', '用户名是必须的') == None:
            print("用户名检验不成功")
            return True
        else:
            return False

    # 邮箱错误
    def register_email_error(self, nickname, register_email, password, re_password, captcha):
        self.common_register(nickname, register_email, password, re_password, captcha)
        if self.rh.get_user_text('register_email_error', "邮箱是必须的") == None:
            print("邮箱检验不成功")
            return True
        else:
            print(self.rh.get_user_text('register_email_error', "邮箱是必须的"))
            return False

    # 密码错误
    def register_password_error(self, nickname, register_email, password, re_password, captcha):
        self.common_register(nickname, register_email, password, re_password, captcha)
        if self.rh.get_user_text('register_password_error', "密码是必须的") == None:
            print("密码检验不成功")
            return True
        else:
            return False

    # 确认密码错误
    def register_re_password_error(self, nickname, register_email, password, re_password, captcha):
        self.common_register(nickname, register_email, password, re_password, captcha)
        if self.rh.get_user_text('register_re_password_error', "确认密码是必须的") == None:
            print("确认密码检验不成功")
            return True
        else:
            return False

    # 验证码错误
    def captcha_code_error(self, nickname, register_email, password, re_password, captcha):
        self.common_register(nickname, register_email, password, re_password, captcha)
        if self.rh.get_user_text('register_captcha_error', "验证码是必须的") == None:
            print("验证码检验不成功")
            return True
        else:
            return False

if __name__ == "__main__":
    register_url = 'https://www.showapi.com/auth/reg'
    driver = webdriver.Firefox()
    driver.get(register_url)
    rb = RegisterBusiness(driver)
    print(rb.register_email_error('vvv', '1586457@qq.com', '221111', '221111', setting.code_path))
    # rb.captcha_code_error('test@123','1243589@163.com', 'pass123', 'pass123', setting.code_path)

    sleep(3)
   # driver.close()
