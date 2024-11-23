'''
Author: jack ning github@bytedesk.com
Date: 2024-04-18 09:13:52
LastEditors: jack ning github@bytedesk.com
LastEditTime: 2024-09-02 06:50:02
FilePath: /MaxKB/apps/smartdoc/const.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# -*- coding: utf-8 -*-
#
import os

from .conf import ConfigManager

__all__ = ['BASE_DIR', 'PROJECT_DIR', 'VERSION', 'CONFIG']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(BASE_DIR)
VERSION = '1.0.0'
# CONFIG = ConfigManager.load_user_config(root_path=os.path.abspath('/opt/maxkb/conf'))
CONFIG = ConfigManager.load_user_config(root_path=os.path.abspath('.'))
