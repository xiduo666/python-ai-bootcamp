import json
PATH=r"C:\Users\LSQ07\Desktop\schedule.json"

with open(PATH,"r",encoding="utf-8") as f:
    schedule=json.loads(f.read())

while True:
    inst=input("请输入指令(查询 修改 退出):").strip()

    if inst=="退出":
        print("成功退出！")
        break

    if inst=="查询":
        inst_querys=input("请输入需要查询的日期(周一到周日):").strip().split()
        for inst_query in inst_querys:
            print(schedule.get(inst_query,"今天没有课程安排"))

    if inst=="修改":
        insts=input("请提出你的修改(键值请用空格隔开):").strip().split()

        if len(insts)%2!=0:
            print("输入格式不符合！请保持键值对的形式出现！")
        else :
            for i in range(0,len(insts),2):
                key=insts[i]
                value=insts[i+1]
                schedule[key]=value

            with open(PATH,"w",encoding="utf-8") as f:
                schedule_write=json.dumps(schedule,ensure_ascii=False)
                f.write(schedule_write)
                print("修改成功！")
