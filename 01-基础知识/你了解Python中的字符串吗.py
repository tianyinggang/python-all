# 题目1：同时输出单引号和双引号

print('hello "world"')
print("hello 'world'")

print('"hello" \'world\'')

# 题目2：让转义符失效（3种方法： r、repr和\）

print(r'Let \'s go!')

print(repr('hello\nworld'))

print('hello\\nworld')

# 题目3：保持原始格式输出字符串

print("""
   hello 
           world
                  I love you.
""")