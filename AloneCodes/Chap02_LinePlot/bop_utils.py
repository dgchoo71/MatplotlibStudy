# 샘플 데이터 다운로드 위치
# https://www.kaggle.com/mabusalah/brent-oil-prices

import os
import numpy as np
import csv


def bop_data_reader() -> np.array:
    month_list: list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # 'Jan': 1, 'Feb': 2 ...
    month_dict = {month_list[m_idx]: m_idx + 1 for m_idx in range(len(month_list))}
    dataset = list()
    
    # 현재 위치에 있는 파일을 읽는다. 패키지 내에서 실행될 수 있으므로
    file_name = os.path.join(os.path.dirname(__file__), 'BrentOilPrices.csv')
    with open(file_name, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)     # 헤더를 제외한다.
        
        for data in csvreader:
            date: str = data[0]
            price: float = float(data[-1])
            
            # Year, Month, Day 순으로 맞춘다.
            year: int
            month: int
            day: int
            if '-' in date:
                tokens = date.split('-')
                year = int(tokens[-1])
                # year가 두 자리이므로
                year = 1900 + year if year > 50 else 2000 + year
                month = month_dict.get(tokens[1])
                day = int(tokens[0])
            elif ',' in date:
                tokens = date.replace(',', ' ').split()
                year = int(tokens[-1])
                month = month_dict.get(tokens[0])
                day = int(tokens[1])
            else:
                continue
                
            dataset.append([year, month, day, price])
            
    # 전체 dataset을 float로 변환
    dataset: np.array = np.array(dataset).astype(np.float)
    return dataset


def get_year_data(dataset: np.array, t_year: float) -> np.array:
    # 지정한 년도의 데이터만 추출한다.
    t_idx: np.array = np.where(dataset[:, 0] == t_year)
    t_data: np.array = dataset[t_idx]
    return t_data


def main():
    dataset: np.array = bop_data_reader()
    
    # 90 년도의 데이터만 추출
    year90_data: np.array = get_year_data(dataset, 1990)
    
    
if __name__ == '__main__':
    main()
    
