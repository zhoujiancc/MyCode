##encoding:utf-8
import os
import csv

##读取csv文件
rd_file = os.getcwd() + '\CsvData\\capture.csv'
rd_file = rd_file.replace('\\', '/')
input_file = open(rd_file,'r', newline='')
csv_file = csv.reader(input_file)
print("读取文件：",rd_file)

##添加newline可以避免一行之后的空格,这样需要在python3环境下运行
wt_file = os.getcwd() + '\CsvData\\TestLog.csv'
wt_file = wt_file.replace('\\', '/')
out = open(wt_file,'w', newline='')
csv_write = csv.writer(out,dialect='excel')
TempData = []
HeadData = []
HeadDictData = []

column_time=[]

column_ign = []
column_CR = []
column_VPC = []
column_EO = []
column_PER = []

column_MODE = []
column_E_OFF_R = []
column_C_lamp_R = []

column_cur1 = []
test_cur1 = []
column_cur2 = []
test_cur2 = []
column_cur3 = []
test_cur3 = []
column_cur4 = []
test_cur4 = []

column_th1 = []
column_th2 = []
column_th3 = []
column_th4 = []
column_th5 = []

test_time = []
test_th1 = []
test_th2 = []
test_th3 = []
test_th4 = []
test_th5 = []

column_vol1 = []
column_vol2 = []
column_vol3 = []
column_vol4 = []
column_vol5 = []
column_vol6 = []
column_vol7 = []
column_vol8 = []
column_vol9 = []
column_vol10 = []
column_vol11 = []
column_vol12 = []
column_vol13 = []
column_vol14 = []
column_vol15 = []
column_vol16 = []
column_vol17 = []
column_vol18 = []
test_vol1 = []
test_vol2 = []
test_vol3 = []
test_vol4 = []
test_vol5 = []
test_vol6 = []
test_vol7 = []
test_vol8 = []
test_vol9 = []
test_vol10 = []
test_vol11 = []
test_vol12 = []
test_vol13 = []
test_vol14 = []
test_vol15 = []
test_vol16 = []
test_vol17 = []
test_vol18 = []

column_ChargePower_Short = []
column_DischargePower_Short = []
column_ChargePower_Long = []
column_DischargePower_Long = []
test_ChargePower_Short = []
test_DischargePower_Short = []
test_ChargePower_Long = []
test_DischargePower_Long = []

column_upper_lower1 = []
column_upper_lower2 = []
column_upper_lower3 = []
column_upper_lower4 = []
column_upper_lower5 = []

column_ChargeCurrent = []
test_ChargeCurrent = []
column_upper_lower6 = []
column_upper_lower7 = []

column_SOH_C = []
test_SOH_C = []
column_upper_lower8 = []

column_SOH_CR = []
test_SOH_CR = []
column_upper_lower9 = []

column_SOH_DR = []
test_SOH_DR = []
column_upper_lower10 = []

column_SOC= []
test_SOC = []
column_upper_lower11 = []

column_ChargePower_Short_expected = []
column_DischargePower_Short_expected = []
column_ChargePower_Long_expected = []
column_DischargePower_Long_expected = []
column_ChargeCurrent_expected = []
column_SOH_C_expected = []
column_SOH_CR_expected = []
column_SOH_DR_expected = []
column_SOC_expected = []
column_MODE_expected = []
column_C_lamp_R_expected = []
column_E_OFF_R_expected = []

column_Permit_Coldstart_DischgPwr_Short = []
column_Permit_DischargePower_VeryShort = []

column_ChargePower_Short_2 = []
column_DischargePower_Short_2 = []
column_ChargePower_Long_2 = []
column_DischargePower_Long_2 = []
column_ChargeCurrent_2 = []
column_SOH_C_2 = []
column_SOH_CR_2 = []
column_SOH_DR_2 = []
column_SOC_2 = []

column_Permit_Coldstart_DischgPwr_Short_2 = []
column_Permit_DischargePower_VeryShort_2 = []

column_Permit_Coldstart_DischgPwr_Short_expected = []

column_SOF_HighSP_RateReq = []
column_SOF_HighSP_RateReq_expected = []

test_ChargePower_Short_2 = []
test_DischargePower_Short_2 = []
test_ChargePower_Long_2 = []
test_DischargePower_Long_2 = []
test_ChargeCurrent_2 = []
test_SOH_C_2 = []
test_SOH_CR_2 = []
test_SOH_DR_2 = []
test_SOC_2 = [] 

csv_write.writerow(["Time","IGN","VehiclePowerCondition_xEV","Contactor_Request","Contactor_EO_Open_Request","Plm_Extension_Request",\
                    "cs_out_low_0","cs_out_low_1","cs_out_low_2","cs_out_low_3","cs_out_low_4","cs_out_low_5",\
                    "cs_out_low_6","cs_out_low_7","cs_out_low_8","cs_out_low_9",\
                    "cs_out_high_0","cs_out_high_1","cs_out_high_2","cs_out_high_3","cs_out_high_4","cs_out_high_5",\
                    "cs_out_high_6","cs_out_high_7","cs_out_high_8","cs_out_high_9",\
                    "tem_raw_0","tem_raw_1","tem_raw_2","tem_raw_3","tem_raw_4","tem_raw_5","tem_raw_6","tem_raw_7","tem_raw_8",\
                    "tem_raw_9","tem_raw_10","tem_raw_11","tem_raw_12","tem_raw_13","tem_raw_14","tem_raw_15","tem_raw_16",\
                    "tem_raw_17","tem_raw_18","tem_raw_19","tem_raw_20","tem_raw_21","tem_raw_22","tem_raw_23","tem_raw_24",\
                    "V_cell_0","V_cell_1","V_cell_2","V_cell_3","V_cell_4","V_cell_5","V_cell_6","V_cell_7","V_cell_8","V_cell_9","V_cell_10",\
                    "V_cell_11","V_cell_12","V_cell_13","V_cell_14","V_cell_15","V_cell_16","V_cell_17","V_cell_18","V_cell_19","V_cell_20",\
                    "V_cell_21","V_cell_22","V_cell_23","V_cell_24","V_cell_25","V_cell_26","V_cell_27","V_cell_28","V_cell_29","V_cell_30",\
                    "V_cell_31","V_cell_32","V_cell_33","V_cell_34","V_cell_35","V_cell_36","V_cell_37","V_cell_38","V_cell_39","V_cell_40",\
                    "V_cell_41","V_cell_42","V_cell_43","V_cell_44","V_cell_45","V_cell_46","V_cell_47","V_cell_48","V_cell_49","V_cell_50",\
                    "V_cell_51","V_cell_52","V_cell_53","V_cell_54","V_cell_55","V_cell_56","V_cell_57","V_cell_58","V_cell_59","V_cell_60",\
                    "V_cell_61","V_cell_62","V_cell_63","V_cell_64","V_cell_65","V_cell_66","V_cell_67","V_cell_68","V_cell_69","V_cell_70",\
                    "V_cell_71","V_cell_72","V_cell_73","V_cell_74","V_cell_75","V_cell_76","V_cell_77","V_cell_78","V_cell_79","V_cell_80",\
                    "V_cell_81","V_cell_82","V_cell_83","V_cell_84","V_cell_85","V_cell_86","V_cell_87","V_cell_88","V_cell_89","V_cell_90",\
                    "V_cell_91","V_cell_92","V_cell_93","V_cell_94","V_cell_95",\
                    "Permit_ChargePower_Short_measured","Permit_ChargePower_Short","Permit_ChargePower_Short_upper","Permit_ChargePower_Short_lower",\
                    "Permit_DischargePower_Short_measured","Permit_DischargePower_Short","Permit_DischargePower_Short_upper","Permit_DischargePower_Short_lower",\
                    "Permit_ChargePower_Long_measured","Permit_ChargePower_Long","Permit_ChargePower_Long_upper","Permit_ChargePower_Long_lower",\
                    "Permit_DischargePower_Long_measured","Permit_DischargePower_Long","Permit_DischargePower_Long_upper","Permit_DischargePower_Long_lower",\
                    "Permit_ChargeCurrent_measured","Permit_ChargeCurrent","Permit_ChargeCurrent_upper","Permit_ChargeCurrent_lower",\
                    "SOH_C_measured","SOH_C","SOH_C_upper","SOH_C_lower",\
                    "SOH_CR_measured","SOH_CR","SOH_CR_upper","SOH_CR_lower",\
                    "SOH_DR_measured","SOH_DR","SOH_DR_upper","SOH_DR_lower",\
                    "SOC_measured","SOC","SOC_upper","SOC_lower",\
					"Permit_Coldstart_DischgPwr_Short_measured","Permit_Coldstart_DischgPwr_Short_2_measured","Permit_Coldstart_DischgPwr_Short",\
					"SOF_HighSP_RateReq_measured","SOF_HighSP_RateReq",\
                    "Mode_measured","Mode",\
                    "Caution Lamp Request_measured","Caution Lamp Request",\
                    "Emergency Off Request_measured","Emergency Off Request",\
                    "Permit_DischargePower_VeryShort",\
                    "Permit_ChargePower_Short_2",\
                    "Permit_DischargePower_Short_2",\
                    "Permit_ChargePower_Long_measured_2",\
                    "Permit_DischargePower_Long_measured_2",\
                    "Permit_ChargeCurrent_2",\
                    "SOH_C_2",\
                    "SOH_CR_2",\
                    "SOH_DR_2",\
                    "SOC_2",\
                    "Permit_DischargePower_VeryShort_2"])
### 文件处理
for row in csv_file:
	TempData.append(row)
	#print(row)

HeadData = TempData[33:34]
#print(HeadData)
del TempData[0:35]

### 读取Capture信号
for i in range(len(HeadData[0])):
        HeadData[0][i] = HeadData[0][i].replace('"','')

with open('Config/Capture_data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
                HeadDictData.append(row)

if(len(HeadDictData)!=len(HeadData[0])-2):
        print('*' * 50)
        print("        Warning Message Number Different!!!")
        print("        Conf Message Num is",len(HeadDictData))
        print("        Caupture Message Num is",len(HeadData[0])-2)
        print("        Please Check File !!!")
        print('*' * 50)
#        os._exit(1)

### 获取信号顺序
for i in range(len(HeadDictData)):
        #print(i)
        HeadDictData[i]["Path"]=HeadDictData[i]["Path"].rstrip("\n")
        for j in range(len(HeadData[0])):
                #print(HeadData[0][j])
                #print(HeadDictData[j]["Path"])
                if (HeadData[0][j] == HeadDictData[i]["Path"]):
                        HeadDictData[i]["FindOutIndex"]=j
                        globals().update({HeadDictData[i]["Name"]:HeadDictData[i]["FindOutIndex"]})
                        
### 找到Index的内容重新存取 备用
with open("Config/Capture_data_Out.csv","w", newline='') as csvfile:
        Capwriter = csv.DictWriter(csvfile,fieldnames=["Index","Name","Path","FindOutIndex"])
        #写入列标题，即DictWriter构造方法的fieldnames参数
        Capwriter.writeheader()
        for data in HeadDictData:
                Capwriter.writerow(data)
                
print("处理文件...")
###处理并写输出文件
for i in range(len(TempData)):

        for item in TempData[i][1:2]:
                a = float(item)*1000.0
                test_time.append(a)
        column_time.append(test_time)

        column_ign.append(TempData[i][ign:ign+1])
        column_VPC.append(TempData[i][VehiclePowerCondition:VehiclePowerCondition+1])
        column_CR.append(TempData[i][Contactor_Request:Contactor_Request+1])
        column_EO.append(TempData[i][EO_Open_Rq:EO_Open_Rq+1])
        column_PER.append(TempData[i][Plm_Extension_Request:Plm_Extension_Request+1])
		
		#curr low 0-8
        for j in TempData[i][curr_low_0:curr_low_0+9]:
                a = float(j)*1000.0
                test_cur1.append(a)
        column_cur1.append(test_cur1)
        
		#curr low 9
        for j in TempData[i][curr_low_9:curr_low_9+1]:
                a = float(j)*1000.0
                test_cur2.append(a)
        column_cur2.append(test_cur2)
        
		#curr high 0-8
        for j in TempData[i][curr_high_0:curr_high_0+9]:
                a = float(j)*1000.0
                test_cur3.append(a)
        column_cur3.append(test_cur3)
        
		#curr high 9
        for j in TempData[i][curr_high_9:curr_high_9+1]:
                a = float(j)*1000.0
                test_cur4.append(a)
        column_cur4.append(test_cur4)
		
        #th0
        for item in TempData[i][th0:th0+1]:
                a = float(item)*10.0
                test_th1.append(a)
        column_th1.append(test_th1)
		#th1
        for item in TempData[i][th1:th1+1]:
                a = float(item)*10.0
                test_th2.append(a)
        column_th2.append(test_th2)
		#th2~7
        for item in TempData[i][th2:th2+7]:
                a = float(item)*10.0
                test_th3.append(a)
        column_th3.append(test_th3)
		#th9~18
        for item in TempData[i][th9:th9+10]:
                a = float(item)*10.0
                test_th4.append(a)
        column_th4.append(test_th4)
		#th29~25
        for item in TempData[i][th19:th19+6]:
                a = float(item)*10.0
                test_th5.append(a)
        column_th5.append(test_th5)

		#vol1
        for item in TempData[i][Vol1:Vol1+1]:
                a = float(item)*1000.0
                test_vol1.append(a)
        column_vol1.append(test_vol1)
		#vol2~9
        for item in TempData[i][Vol2:Vol2+8]:
                a = float(item)*1000.0
                test_vol2.append(a)
        column_vol2.append(test_vol2)
		#vol10~18
        for item in TempData[i][Vol10:Vol10+9]:
                a = float(item)*1000.0
                test_vol3.append(a)
        column_vol3.append(test_vol3)
		#vol19
        for item in TempData[i][Vol19:Vol19+1]:
                a = float(item)*1000.0
                test_vol4.append(a)
		#vol20~27
        column_vol4.append(test_vol4)
        for item in TempData[i][Vol20:Vol20+8]:
                a = float(item)*1000.0
                test_vol5.append(a)
        column_vol5.append(test_vol5)
		#vol28~30
        for item in TempData[i][Vol28:Vol28+3]:
                a = float(item)*1000.0
                test_vol6.append(a)
        column_vol6.append(test_vol6)
		#vol31
        for item in TempData[i][Vol31:Vol31+1]:
                a = float(item)*1000.0
                test_vol7.append(a)
        column_vol7.append(test_vol7)
		#vol32~39
        for item in TempData[i][Vol32:Vol32+8]:
                a = float(item)*1000.0
                test_vol8.append(a)
        column_vol8.append(test_vol8)
		#vol40~48
        for item in TempData[i][Vol40:Vol40+9]:
                a = float(item)*1000.0
                test_vol9.append(a)
        column_vol9.append(test_vol9)
		#vol49
        for item in TempData[i][Vol49:Vol49+1]:
                a = float(item)*1000.0
                test_vol10.append(a)
        column_vol10.append(test_vol10)
		#vol50~57
        for item in TempData[i][Vol50:Vol50+8]:
                a = float(item)*1000.0
                test_vol11.append(a)
        column_vol11.append(test_vol11)
		#vol58~66
        for item in TempData[i][Vol58:Vol58+9]:
                a = float(item)*1000.0
                test_vol12.append(a)
        column_vol12.append(test_vol12)
		#vol67
        for item in TempData[i][Vol67:Vol67+1]:
                a = float(item)*1000.0
                test_vol13.append(a)
        column_vol13.append(test_vol13)
		#vol68~75
        for item in TempData[i][Vol68:Vol68+8]:
                a = float(item)*1000.0
                test_vol14.append(a)
        column_vol14.append(test_vol14)
		#vol76~78
        for item in TempData[i][Vol76:Vol76+3]:
                a = float(item)*1000.0
                test_vol15.append(a)
        column_vol15.append(test_vol15)
		#vol79
        for item in TempData[i][Vol79:Vol79+1]:
                a = float(item)*1000.0
                test_vol16.append(a)
        column_vol16.append(test_vol16)
		#vol80~87
        for item in TempData[i][Vol80:Vol80+8]:
                a = float(item)*1000.0
                test_vol17.append(a)
        column_vol17.append(test_vol17)
		#vol88~96
        for item in TempData[i][Vol88:Vol88+9]:
                a = float(item)*1000.0
                test_vol18.append(a)
        column_vol18.append(test_vol18)

        for item in TempData[i][ChargePower_Short:ChargePower_Short+1]:
                a = float(item)*1000.0
                test_ChargePower_Short.append(a)
        column_ChargePower_Short.append(test_ChargePower_Short)
        for item in TempData[i][DischargePower_Short:DischargePower_Short+1]:
                a = float(item)*1000.0
                test_DischargePower_Short.append(a)
        column_DischargePower_Short.append(test_DischargePower_Short)
        for item in TempData[i][ChargePower_Long:ChargePower_Long+1]:
                a = float(item)*1000.0
                test_ChargePower_Long.append(a)
        column_ChargePower_Long.append(test_ChargePower_Long)
        for item in TempData[i][DischargePower_Long:DischargePower_Long+1]:
                a = float(item)*1000.0
                test_DischargePower_Long.append(a)
        column_DischargePower_Long.append(test_DischargePower_Long)
        
		#Permit_ChargePower_Short_upper
        column_upper_lower1.append(TempData[i][ChargePower_Short_upper:ChargePower_Short_upper+1])
		#Permit_ChargePower_Short_lower
        column_upper_lower2.append(TempData[i][ChargePower_Short_lower:ChargePower_Short_lower+1])
		#"Permit_DischargePower_Short_upper","Permit_DischargePower_Short_lower"
        column_upper_lower3.append(TempData[i][DischargePower_Short_upper:DischargePower_Short_upper+2])
		#"Permit_ChargePower_Long_upper","Permit_ChargePower_Long_lower"
        column_upper_lower4.append(TempData[i][ChargePower_Long_upper:ChargePower_Long_upper+2])
		#"Permit_DischargePower_Long_upper","Permit_DischargePower_Long_lower"
        column_upper_lower5.append(TempData[i][DischargePower_Long_upper:DischargePower_Long_upper+2])

        column_ChargePower_Short_expected.append(TempData[i][ChargePower_Short_expected:ChargePower_Short_expected+1])
        column_DischargePower_Short_expected.append(TempData[i][DischargePower_Short_expected:DischargePower_Short_expected+1])
        column_ChargePower_Long_expected.append(TempData[i][ChargePower_Long_expected:ChargePower_Long_expected+1])
        column_DischargePower_Long_expected.append(TempData[i][DischargePower_Long_expected:DischargePower_Long_expected+1])

        for item in TempData[i][ChargeCurrent:ChargeCurrent+1]:
                a = float(item)
                test_ChargeCurrent.append(a)
        column_ChargeCurrent.append(test_ChargeCurrent)
		
		#Permit_ChargeCurrent_upper
        column_upper_lower6.append(TempData[i][ChargeCurrent_upper:ChargeCurrent_upper+1])
		#Permit_ChargeCurrent_lower
        column_upper_lower7.append(TempData[i][ChargeCurrent_lower:ChargeCurrent_lower+1])
        
        column_ChargeCurrent_expected.append(TempData[i][ChargeCurrent_expected:ChargeCurrent_expected+1])

        for item in TempData[i][SOHC:SOHC+1]:
                a = float(item)
                test_SOH_C.append(a)
        column_SOH_C.append(test_SOH_C)
		
		#"SOH_C_upper","SOH_C_lower"
        column_upper_lower8.append(TempData[i][SOH_C_upper:SOH_C_upper+2])
        
        column_SOH_C_expected.append(TempData[i][SOH_C_expected:SOH_C_expected+1])
        
        for item in TempData[i][SOHR:SOHR+1]:
                a = float(item)
                test_SOH_CR.append(a)
        column_SOH_CR.append(test_SOH_CR)
		
		#"SOH_CR_upper","SOH_CR_lower"
        column_upper_lower9.append(TempData[i][SOH_CR_upper:SOH_CR_upper+2])

        column_SOH_CR_expected.append(TempData[i][SOH_CR_expected:SOH_CR_expected+1])
        
        for item in TempData[i][SOHR:SOHR+1]:
                a = float(item)
                test_SOH_DR.append(a)
        column_SOH_DR.append(test_SOH_DR)
		
		#"SOH_DR_upper","SOH_DR_lower"
        column_upper_lower10.append(TempData[i][SOH_DR_upper:SOH_DR_upper+2])

        column_SOH_DR_expected.append(TempData[i][SOH_DR_expected:SOH_DR_expected+1])
        
        for item in TempData[i][SOC:SOC+1]:
                a = float(item)
                test_SOC.append(a)
        column_SOC.append(test_SOC)
		
		#"SOC_upper","SOC_lower"
        column_upper_lower11.append(TempData[i][SOC_upper:SOC_upper+2])

        column_SOC_expected.append(TempData[i][SOC_expected:SOC_expected+1])
        
        column_MODE.append(TempData[i][mode:mode+1])
        column_MODE_expected.append(TempData[i][mode_expected:mode_expected+1])

        column_C_lamp_R.append(TempData[i][Caution_lamp_Request:Caution_lamp_Request+1])
        column_C_lamp_R_expected.append(TempData[i][Caution_lamp_Request:Caution_lamp_Request+1])
        
        
        column_E_OFF_R.append(TempData[i][Emergency_Off_Request:Emergency_Off_Request+1])
        column_E_OFF_R_expected.append(TempData[i][Emergency_Off_Request:Emergency_Off_Request+1]) ##??


        column_Permit_Coldstart_DischgPwr_Short.append(TempData[i][Coldstart_DischgPwr_Short:Coldstart_DischgPwr_Short+1])
        column_Permit_DischargePower_VeryShort.append(TempData[i][DischargePower_VeryShort:DischargePower_VeryShort+1])

        for item in TempData[i][ChargePower_Short_2:ChargePower_Short_2+1]:
                a = float(item)*100.0
                test_ChargePower_Short_2.append(a)
        column_ChargePower_Short_2.append(test_ChargePower_Short_2)
        for item in TempData[i][DischargePower_Short_2:DischargePower_Short_2+1]:
                a = float(item)*100.0
                test_DischargePower_Short_2.append(a)
        column_DischargePower_Short_2.append(test_DischargePower_Short_2)
        for item in TempData[i][ChargePower_Long_2:ChargePower_Long_2+1]:
                a = float(item)*100.0
                test_ChargePower_Long_2.append(a)
        column_ChargePower_Long_2.append(test_ChargePower_Long_2)
        for item in TempData[i][DischargePower_Long_2:DischargePower_Long_2+1]:
                a = float(item)*100.0
                test_DischargePower_Long_2.append(a)
        column_DischargePower_Long_2.append(test_DischargePower_Long_2)
                   
        for item in TempData[i][ChargeCurrent_2:ChargeCurrent_2+1]:
                a = float(item)*1000.0
                test_ChargeCurrent_2.append(a)
        column_ChargeCurrent_2.append(test_ChargeCurrent_2)

        for item in TempData[i][SOHC_2:SOHC_2+1]:
                a = float(item)*10.0
                test_SOH_C_2.append(a)
        column_SOH_C_2.append(test_SOH_C_2)
        
        for item in TempData[i][SOHR_2:SOHR_2+1]:
                a = float(item)*10.0
                test_SOH_CR_2.append(a)
        column_SOH_CR_2.append(test_SOH_CR_2)
        
        for item in TempData[i][SOHR_2:SOHR_2+1]:
                a = float(item)*10.0
                test_SOH_DR_2.append(a)
        column_SOH_DR_2.append(test_SOH_DR_2)
        
        for item in TempData[i][SOC_2:SOC_2+1]:
                a = float(item)*10.0
                test_SOC_2.append(a)
        column_SOC_2.append(test_SOC_2)
        
        column_Permit_Coldstart_DischgPwr_Short_2.append(TempData[i][Coldstart_DischgPwr_Short_2:Coldstart_DischgPwr_Short_2+1])
        column_Permit_DischargePower_VeryShort_2.append(TempData[i][DischargePower_VeryShort_2:DischargePower_VeryShort_2+1])

        column_Permit_Coldstart_DischgPwr_Short_expected.append(TempData[i][Coldstart_DischgPwr_Short_expected:Coldstart_DischgPwr_Short_expected+1])
		
        column_SOF_HighSP_RateReq.append(TempData[i][SOF_HighSP_RateReq:SOF_HighSP_RateReq+1])
        column_SOF_HighSP_RateReq_expected.append(TempData[i][SOF_HighSP_RateReq_expected:SOF_HighSP_RateReq_expected+1])
      
        csv_write.writerow(column_time[i]+column_ign[i]+column_VPC[i]+column_CR[i]+column_EO[i]+column_PER[i]\
                           +column_cur1[i]+column_cur2[i]+column_cur3[i]+column_cur4[i]\
                           +column_th1[i]+column_th2[i]+column_th3[i]+column_th4[i]+column_th5[i]\
                           +column_vol1[i]+column_vol2[i]+column_vol3[i]+column_vol4[i]+column_vol5[i]+column_vol6[i]\
                           +column_vol7[i]+column_vol8[i]+column_vol9[i]+column_vol10[i]+column_vol11[i]+column_vol12[i]\
                           +column_vol13[i]+column_vol14[i]+column_vol15[i]+column_vol16[i]+column_vol17[i]+column_vol18[i]\
                           +column_ChargePower_Short[i]+column_ChargePower_Short_expected[i]+column_upper_lower1[i]+column_upper_lower2[i]\
                           +column_DischargePower_Short[i]+column_DischargePower_Short_expected[i]+column_upper_lower3[i]\
                           +column_ChargePower_Long[i]+column_ChargePower_Long_expected[i]+column_upper_lower4[i]\
                           +column_DischargePower_Long[i]+column_DischargePower_Long_expected[i]+column_upper_lower5[i]\
                           +column_ChargeCurrent[i]+column_ChargeCurrent_expected[i]+column_upper_lower6[i]+column_upper_lower7[i]\
                           +column_SOH_C[i]+column_SOH_C_expected[i]+column_upper_lower8[i]\
                           +column_SOH_CR[i]+column_SOH_CR_expected[i]+column_upper_lower9[i]\
                           +column_SOH_DR[i]+column_SOH_DR_expected[i]+column_upper_lower10[i]\
                           +column_SOC[i]+column_SOC_expected[i]+column_upper_lower11[i]\
						   +column_Permit_Coldstart_DischgPwr_Short[i]+column_Permit_Coldstart_DischgPwr_Short_2[i]+column_Permit_Coldstart_DischgPwr_Short_expected[i]\
						   +column_SOF_HighSP_RateReq[i]+column_SOF_HighSP_RateReq_expected[i]\
                           +column_MODE[i]+column_MODE_expected[i]\
                           +column_C_lamp_R[i]+column_C_lamp_R_expected[i]\
                           +column_E_OFF_R[i]+column_E_OFF_R_expected[i]\
                           +column_Permit_DischargePower_VeryShort[i]\
                           +column_ChargePower_Short_2[i]\
                           +column_DischargePower_Short_2[i]\
                           +column_ChargePower_Long_2[i]\
                           +column_DischargePower_Long_2[i]\
                           +column_ChargeCurrent_2[i]\
                           +column_SOH_C_2[i]\
                           +column_SOH_CR_2[i]\
                           +column_SOH_DR_2[i]\
                           +column_SOC_2[i]\
                           +column_Permit_DischargePower_VeryShort_2[i])

        test_time.clear()
        test_cur1.clear()
        test_cur2.clear()
        test_cur3.clear()
        test_cur4.clear()
        test_th1.clear()
        test_th2.clear()
        test_th3.clear()
        test_th4.clear()
        test_th5.clear()
        test_vol1.clear()
        test_vol2.clear()
        test_vol3.clear()
        test_vol4.clear()
        test_vol5.clear()
        test_vol6.clear()
        test_vol7.clear()
        test_vol8.clear()
        test_vol9.clear()
        test_vol10.clear()
        test_vol11.clear()
        test_vol12.clear()
        test_vol13.clear()
        test_vol14.clear()
        test_vol15.clear()
        test_vol16.clear()
        test_vol17.clear()
        test_vol18.clear()
        test_ChargePower_Short.clear()
        test_DischargePower_Short.clear()
        test_ChargePower_Long.clear()
        test_DischargePower_Long.clear()
        test_ChargeCurrent.clear()
        test_SOH_C.clear()
        test_SOH_CR.clear()
        test_SOH_DR.clear()
        test_SOC.clear()
        test_ChargePower_Short_2.clear()
        test_DischargePower_Short_2.clear()
        test_ChargePower_Long_2.clear()
        test_DischargePower_Long_2.clear()
        test_ChargeCurrent_2.clear()
        test_SOH_C_2.clear()
        test_SOH_CR_2.clear()
        test_SOH_DR_2.clear()
        test_SOC_2.clear()        
	
print("写入文件：",wt_file)
print("写入完成")
input_file.close()
out.close()




