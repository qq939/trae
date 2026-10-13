# 用户规则

1. .trae/reference/ref.txt（如果没有请新建）里面是需要参考的github地址或接口文档
2. 通过notebooklm-skill找类似参考给出可行性分析，补充到该文件.trae/reference/ref.txt
3. global参数前置到py文件最上边，并在注释中给出具体使用位置（精确到行）
4. 完成所有任务清单，完成之前不要退出
5. TDD模式，每个任务开始前先写测试脚本，测试必须有超时机制，脚本必须通过测试才算完成任务
6. 将user_rules.md文件中的所有规则都保存在：.trae/rules/user_rules.md中
7. 如果有git仓库，先暂存本地修改，然后git pull，然后再继续下面的步骤
8. 确保python的import不缺失，requirements.txt里的模块不缺失，requirements.txt里面不要写版本号，requirements_{python version}.txt里面是带版本号的模块
9. 每次对话后都要git commit，commit内容就是我说的那句话
10. 如果是python项目，需要使用micromamba的portable的python环境，放到用户目录Downloads下，命名示例py311-xxxx项目
