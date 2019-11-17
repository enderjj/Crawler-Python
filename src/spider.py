import requests
import re


class Spider():
    # 网页地址
    url = "https://coding.imooc.com/"

    # 匹配根结点的正则表达式
    root_pattern = '<div class="shizhan-intro-box">([\s\S]*?)</div>'

    # 匹配课程名称的正则表达式
    course_name_pattern = '<p .+?>([\s\S]*?)</p>'

    # 匹配课程人数的正则表达式
    course_num_pattern = '<i class="imv2-set-sns"></i>(\d+)'

    # 存放所有匹配的最终结果，每项都是一个字典
    courses = []

    # 获取网页内容
    def __fetch_contents(self):
        result = requests.get(Spider.url).text
        return result

    # 解析网页内容
    def __analysis(self, htmls):
        res_list = re.findall(Spider.root_pattern, htmls)
        for res in res_list:
            res_name = re.findall(Spider.course_name_pattern, res)[0]
            res_num = re.findall(Spider.course_num_pattern, res)[0]
            res_num = int(res_num) if res_num else res_num
            Spider.courses.append({
                'name': res_name,
                'num': res_num
            })

    # 入口函数
    def go(self):
        htmls = self.__fetch_contents()
        self.__analysis(htmls)


spider = Spider()
spider.go()
