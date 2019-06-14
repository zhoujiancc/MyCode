MyCode
======

参照
https://gitlab.com/gitlab-org/gitaly/issues/248

https://packages.gitlab.com/gitlab/gitlab-ce

curl -s https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | sudo bash
> sudo apt-get install gitlab-ce=10.3.2-ce.0

themes:
https://go.kieran.top/
http://fech.in/



https://www.ithome.com/0/412/779.htm



                           
for row in CapData:
#	TempData.append(row)
	print(row)

for row in csv_file:
	TempData.append(row)
	#print(row)
	
del TempData[34:35]
del TempData[0:33]

for i in range(len(TempData[0])):
        TempData[0][i] = TempData[0][i].replace('"', '')
        print(TempData[0][i])

for row in TempData:
	#TempData.append(row)
	print(row)

str3 = "Data Stores/EcuStartStop_Req"


if(TempData[0][2]==str3):
        print("ok")
else:
        print("NG")
        
