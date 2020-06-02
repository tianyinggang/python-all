while True:
    try:
        x = int(input('请输入x:'))
        y = int(input('请输入y:'))
        value = x / y
        print('x / y is',value)
    except Exception as e: # 发生异常时执行
        print('不正确的输入：',e)
        print('请重新输入')
    else:  # 未发生异常时执行
        break
