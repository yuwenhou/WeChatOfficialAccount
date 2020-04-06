import json
import jsonpath


class parseData():
    '''
    解析提取数据模块
    '''
    def get_info(self,response_txt):
        '''
        提取 json 中的数据
        :param response_txt: json 格式的数据
        :return:
        '''
        try: # 防止某些页编码失败
            json_txt = json.loads(response_txt)
            results = jsonpath.jsonpath(json_txt,'$..result')[0]
            data = []
            for result in results:
                postion_info = (
                    result['positionName'], # 职位名
                    result['companyFullName'], # 公司名
                    result['companySize'], # 公司规模
                    result['industryField'], # 公司主要业务
                    result['financeStage'], # 融资情况

                    ','.join(result['companyLabelList']) +
                            result['positionAdvantage'], # 公司待遇福利

                    result['firstType'] + result['secondType'] +
                            result['thirdType'], # 职位类型

                    ','.join(result['skillLables']), # 技能要求
                    result['createTime'], # 职位发布时间
                    result['district'], # 行政区
                    result['salary'], # 薪水
                    result['workYear'], # 工作经验
                    result['jobNature'], # 工作性质
                    result['education'], # 学历要求
                )
                data.append(postion_info)
            return data
        except:
            return
