class urlManager():
    def __init__(self):
        '''
        初始化 url
        '''
        # 职位 url
        self.positon_url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city={}&needAddtionalResult=false'

    def get_position_url(self):
        '''
        返回职位 url
        :return:
        '''
        return self.positon_url




