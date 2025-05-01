def generate_serial(username):
    if not username:
        return "用户名不能为空"

    length = len(username)
    first_char = username[0]
    serial = ((length * 88888 + ord(first_char) + 2) * 3 - 2) + 15
    return str(serial)

# 测试
name = input("请输入用户名：")
print("生成的注册码是：", generate_serial(name))
