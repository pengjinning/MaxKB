<!--
 * @Author: jack ning github@bytedesk.com
 * @Date: 2024-09-02 11:02:47
 * @LastEditors: jack ning github@bytedesk.com
 * @LastEditTime: 2024-09-04 12:54:54
 * @FilePath: /MaxKB/Readme.zh.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# readme

```bash
# python main.py start all -d
# 生成虚拟环境
python -m venv .venv
# 激活虚拟环境
source .venv/bin/activate
# deactivate
which python
# 
pip install poetry
poetry config virtualenvs.prefer-active-python true
# 
poetry run which python
# poetry add fastapi, uvicorn
poetry install --no-root
# 
python main.py dev
# 用户名: admin
# 密码: MaxKB@123..
```
