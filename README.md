系统分为两个个子系统：门禁人脸识别系统与用户管理系统.门禁人脸识别系统：分为大门和单元门两个部分。大门门禁系统会检测来访者是否是该小区的住户，而单元门门禁系统会检测来访者是否为该单元门住户。该系统可通过人脸识别，将来访者的信息与数据库中的人员信息进行比对，若匹配成功则放行进入，并记录进入时间。若匹配失败，则让来访者输入要去的单元号，并将来访者的来访请求上传到用户自主管理系统中，通过调用邮箱api给户主发送邮箱提醒户主处理请求，由户主确认方可进行放行操作。
用户管理系统：
用户可使用账号密码或刷脸方式登录该系统。用户分为两种身份：小区管理员和住户。
其中小区管理员可以查看所有用户的信息，并可以修改，删除用户信息。同时还可以查看小区用户进出的所有记录与统计数据。此外，小区管理员可以管理用户的人脸录入数据，查看所有用户的人脸录入数据情况，并可以对其进行删除。
住户可以进行人脸录入，处理外来人员来访请求，还可以查看自家未成年人进出记录。
