raw_data = ["85", "92", "ERROR", "105", "78", "WARNING", "99", "120"]
def clean_and_convert(value):
    try:
        return int(value)
    except(ValueError,TypeError):
        return None
def process_data(data):
    print("原始数据:",data)
    print("\n处理步骤:")
    cleaned_data=[]
    for item in data:
        converted=clean_and_convert(item)
        if converted is not None:
            cleaned_data.append(converted)
    print(f"1.清洗后(仅数字):{cleaned_data}")
    filtered_data=list(filter(lambda x: x>=80,cleaned_data))
    print(f"2.过滤后(≥80):{filtered_data}")
    normalized_data=list(map(lambda x:x/100,filtered_data))
    print(f"3.归一化后(除以100):{normalized_data}")
    print("\n4.最终结果与判断:")
    results=[]
    for value in normalized_data:
        if value>1.0:
            result=f"{value:.2f}:核心过载"
        else:
            result=f"{value:.2f}:运转正常"
        results.append(result)
    return results
final_results=process_data(raw_data)
for result in final_results:
    print(result)