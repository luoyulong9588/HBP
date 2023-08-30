# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import json
from rich import print

file = "before.json"
answer_list = []
with open(file, 'r', encoding='utf-8') as f:
    result = json.load(f)["data"]["moduleList"][0]["questionList"]
    for i in result:
        answer_dic = {}
        title = i['title']
        answer = i['answer']
        questionnumber = i["questionNum"]
        option_list = [f"{j['mark']}.{j['chooseContent']}" for j in i['optionalContent']]

        answer_dic["title"] = f"第{questionnumber}题 -- {title}"
        answer_dic["options"] = option_list
        answer_dic["answer"] = answer[0]
        answer_list.append(answer_dic)
    print(answer_list)
    with open("学习前测试题.json", 'w', encoding='utf-8') as fp:
        fp.write(json.dumps(answer_list, ensure_ascii=False))
