'*******************************************************************'

'程序名称：最完美的利用EXCEL自动批量发送邮件
'经测试在OUTLOOK 2000中不会显示警告窗口.
'引用：Microseft Outlook *.0 Object Library
'需要注意一点 , 邮件的标题, 否则不能自动放送!

'**********************************************************************

Sub 批量发送邮件()

'要能正确发送并需要对Microseft Outlook进行有效配置

'    Dim SigString As String
'    Dim Signature As String
'  ''
'    'Use the second SigString if you use Vista or Win 7 as operating system
'    'SigString = "C:\Documents and Settings\" & Environ("username") & "\Application Data\Microsoft\Signatures\Mysig.txt"
'    SigString = "C:\Users\" & Environ("username") & "\AppData\Roaming\Microsoft\Signatures\汽电.htm"
'    If Dir(SigString) <> "" Then
'        Signature = GetBoiler(SigString)
'    Else
'        Signature = ""
'    End If

    On Error Resume Next

    Dim rowCount, endRowNo
    Dim arr
    Dim Signature

    '要正常运行下面这句,要将工具/引用中的Microseft Outlook *.0 Object Library(其中*为你Microseft Outlook的版本号)选上
    Dim objOutlook As New Outlook.Application

    Dim objMail As MailItem

    '取得当前工作表与Cells(1,1)相连的数据区行数
    endRowNo = Cells(1, 1).CurrentRegion.Rows.Count

    '创建objOutlook为Outlook应用程序对象
    Set objOutlook = New Outlook.Application

    '开始循环发送电子邮件
    For rowCount = 2 To endRowNo

        '创建objMail为一个邮件对象
        Set objMail = objOutlook.CreateItem(olMailItem)

        With objMail

            '设置收件人地址（从通讯录表的'E-mail地址'字段中获得）
            .To = Cells(rowCount, 1)
            
            .CC = Cells(rowCount, 2).Value      '"抄送"
            '设置邮件主题
            .Subject = Cells(rowCount, 3)

            '设置邮件内容（从通讯录表的'内容'字段中获得）
            Signature = Cells(rowCount, 6).Value
            
            .Body = Cells(rowCount, 4) & vbNewLine & vbNewLine & Signature
            '.HTMLBody = Cells(rowCount, 4) & vbNewLine & vbNewLine & Signature
            
            '设置附件（从通讯录表的'附件'字段中获得）
            arr = Split(Cells(rowCount, 5).Value, ";")
                For n = LBound(arr) To UBound(arr)
                    .Attachments.Add (arr(n))      '邮件的附件
                Next

            '自动发送邮件
            .Send

        End With

        '销毁objMail对象
        Set objMail = Nothing

    Next

    '销毁objOutlook对象
    Set objOutlook = Nothing
    '所有电子邮件发送完成时提示
    MsgBox (rowCount - 2) & "邮件发送成功！可以到发件箱查看！"
    
    If Application.Workbooks.Count = 1 Then
        Application.Quit
    Else
        Workbooks("自动发送邮件.xls").Close
    End If
    
End Sub

Function GetBoiler(ByVal sFile As String) As String
Dim fso As Object
Dim ts As Object
Set fso = CreateObject("Scripting.FileSystemObject")
Set ts = fso.GetFile(sFile).OpenAsTextStream(1, -2)
GetBoiler = ts.readall
ts.Close
End Function
