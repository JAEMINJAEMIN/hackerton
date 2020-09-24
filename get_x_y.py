import requests
import json
import pandas as pd

def get_x_y(data) :
    url = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query='+data['소재지도로명']
    headers = {'X-NCP-APIGW-API-KEY-ID':'yia7wsfo8w','X-NCP-APIGW-API-KEY':'MjVL1dVlIMRkbpLBWT1XskehfpZIpmUsDNB4tzDa'}
    respons = requests.get(url, headers=headers)
    result = json.loads(respons.text)
    if result['addresses'] == [] :
        return 0
    x, y = result['addresses'][0]['x'], result['addresses'][0]['y']
    return {'location' : data['소재지도로명'],
            'date':[data['위반일자']],
            'content':[data['처분명']],
            'name' : data['업소명'],
            'x':x,
            'y':y}

def merge_data(new, old={}) :
    if new == 0 :
        return old
    if old.get(new['location']):
        old[new['location']]['date'] += new['date']
        old[new['location']]['content']+= new['content']
        old[new['location']]['name'] = new['name']
    else :
        old[new['location']] = new
    return old





f = pd.read_csv('동작구.csv')


dic = {} # 빈 딕셔너리
for i in f.iloc : #데이터프레임을 한줄씩 불러오기
    new = get_x_y(i) # x,y좌표와 처분내용, 업소명 주소 등 데이터 가져오기
    dic = merge_data(new,dic) # 이전 딕셔너리와 새로운 내용을 합치기위해
                              # 하는 이유 : 새로운 데이터가 마커를 찍을때 중복되는걸 방지하기위해
    
for _, i in dic.items() :
    x = i['x'] #x좌표
    y = i['y'] #y좌표
    name = i['name'] #상호명
    location = i['location'] #주소
    content = i['content'] #위반내용
    date = i['date']
    content_len = len(content)
    print(f'상호명 : {name}, 주소 : {location}')
    print(f'총 {content_len} 건의 위반내용이 있습니다.')
    print('*'*50)
    for a, b in zip(content, date) :
        print(f'일시 : {b}')
        print(f'처분 : {a}')
    print(f'x 좌표 : {x}, y 좌표 : {y}')
    print()
    print()
    print()
