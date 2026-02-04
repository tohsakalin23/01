raw_intel=" Agent:007_Bond; Coords:(40,74); Items:gun,money,gun;Mission:2025-RESCUE-X "
cleaned_intel=raw_intel.replace(" ","")
parts=cleaned_intel.split(";")
intel_info={}
for part in parts:
    key_value=part.split(":",1)
    if len(key_value)==2:
        key=key_value[0]
        value=key_value[1]
        if key=="Agent":
            intel_info[key]=value
        elif key=="Coords":
            coords_without_brackets=value.strip("()")
            coord_parts=coords_without_brackets.split(",")
            x=int(coord_parts[0])
            y=int(coord_parts[1])
            coord_tuple=(x,y)
            intel_info[key]=coord_tuple
        elif key=="Items":
            items_list=value.split(",")
            items_set=set(items_list)
            unique_items=list(items_set)
            intel_info[key]=unique_items
        elif key=="Mission":
            mission_parts=value.split("-")
            core_mission=mission_parts[1]
            intel_info[key]=core_mission
            intel_info["FullMission"]=value
print("整理后的情报档案：")
for key in intel_info:
    print(f"{key}: {intel_info[key]}")