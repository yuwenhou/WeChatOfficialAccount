import requests, json
import city

def main(city_name):
    #api地址
    url = 'http://t.weather.sojson.com/api/weather/city/'

    #通过城市的中文获取城市代码
    city_code = city.citycode[city_name]

    #网络请求，传入请求api+城市代码
    response = requests.get(url + city_code)

    #将数据以json形式返回，这个d就是返回的json数据
    d = response.json()
    dd = "城市： "+ d["cityInfo"]["parent"]+d["cityInfo"]["city"] + \
         "\n时间： "+ d["time"]+ d["data"]["forecast"][0]["week"] + \
         "\n温度： "+ d["data"]["forecast"][0]["high"]+ d["data"]["forecast"][0]["low"] + \
         "\n天气： "+ d["data"]["forecast"][0]["type"] + \
         "\n注意： "+ d["data"]["forecast"][0]["notice"]
    print(dd)
    #当返回状态码为200，输出天气状况
    # if(d['status'] == 200):
    #     print("城市： "+ d["cityInfo"]["parent"]+d["cityInfo"]["city"])
    #     print("时间： "+ d["time"]+ d["data"]["forecast"][0]["week"])
    #     print("温度： "+ d["data"]["forecast"][0]["high"]+ d["data"]["forecast"][0]["low"])
    #     print("天气： "+ d["data"]["forecast"][0]["type"])
    #     print("注意： "+ d["data"]["forecast"][0]["notice"])


    return dd
if __name__ == '__main__':
    # city_name = input("请输入你要查询的城市：")
    city_name = '广州'
    main(city_name)


