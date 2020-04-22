#coding:utf-8
import xlrd
import os
import numpy as np




def openfile(file):
    # 打开文件
    workbook = xlrd.open_workbook(file)

    #打开工作薄
    sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始

    #读取数据
    data_danju_nos = sheet1.col_values(2,14) #单据编号序号
    data_danju_types = sheet1.col_values(4,14)#单据类型
    data_yewus = sheet1.col_values(5,14) #业务员
    data_companys = sheet1.col_values(8,14)  #交易单位
    data_descriptions = sheet1.col_values(25,14) #交易说明
    data_amounts = sheet1.col_values(27,14)  # 交易金额

    dates_norepeat = set()
    for riqi,leixing,yewu,gongsi,desc,amount in zip(data_danju_nos,data_danju_types,data_yewus,data_companys,data_descriptions,data_amounts):
        if gongsi=="科技市场":
            continue
        riqi = riqi[5:15]
        dates_norepeat.add(riqi)
        #print(riqi,leixing,yewu,gongsi,desc,amount)
    money_per_days = []
    dates_norepeat = list(dates_norepeat)
    dates_norepeat.sort()
    moneys_per_day=[0 for i in range(31)] #设置每天


    for d in dates_norepeat:
        money_per_day = 0
        for riqi, amount in zip(data_danju_nos, data_amounts):
            riqi = riqi[5:15]
            if d == riqi:
                if type(amount) == str:
                    amount = amount.replace(',', '')
                money_per_day = money_per_day + float(amount)
        else:
            n = int(d.split('-')[-1])
            moneys_per_day[n-1]=int(money_per_day)

    return moneys_per_day




def other_pay():
    other_list = [0 for x in range(31)]  # 其他费用
    other_list[19] = -28800 #基本工资
    other_list[4] = -25000 #公积金社保
    other_list[29] = -10000 #运费
    other_list[15] = -20000 #房租物业水电
    return other_list

if __name__ == '__main__':

    payment_file = "C:\\Users\Administrator\Desktop\支出.xls"
    cost_file = "C:\\Users\Administrator\Desktop\费用.xls"
    collect_file = "C:\\Users\Administrator\Desktop\收款.xls"

    collect_list = openfile(collect_file) #收入列表
    payment_list = [-1 * x for x in openfile(payment_file)] #支付货款列表
    cost_list = [-1 * x for x in openfile(cost_file)] #费用列表
    other_list = other_pay()

    total_list = [0 for i in range(31)] #每日收支统计
    current_list = [0 for i in range(31)] #当前金额
    sum  = 0
    for i in range(31):
        total_list[i] = collect_list[i]+payment_list[i]+cost_list[i]+other_list[i]
        sum = sum + total_list[i]
        current_list[i] = current_list[i]+sum
    current_list = np.array(current_list)+50000
    #print(total_list)
    #print(current_list)
    if not os.path.exists('I:/data/'):
        os.mkdir('I:/data')
    with open('I:/data/json.txt', 'w') as w:
        str = '[\n{name:"收入",data:'+str(collect_list)+'},\n{name:"货款",data:'+ \
              str(payment_list)+'},\n{name:"费用",data:'+str(cost_list)+'},\n{name:"固定支出",data:'+ \
              str(other_list)+'},\n{name:"合计",data:'+str(total_list)+'},\n{name:"账户余额",data:'+\
              str(current_list.tolist())+'}\n]'
        w.write(str)




