# -*- coding: UTF-8 -*-

# 引入tensorflow
import tensorflow as tf

# 创建两个常量 Tensor
const1 = tf.constant([[2, 2]])
const2 = tf.constant([[4],
                      [4]])

multiple = tf.matmul(const1, const2)

# 尝试用print输出multiple的值
print(multiple)

# 创建了 Session（会话）对象
sess = tf.Session()

# 用Session的run方法来实际运行multiple这个矩阵乘法操作
# 并把操作执行的结果赋值给 result
result = sess.run(multiple)

# 用print打印矩阵乘法的结果
print(result)

if const1.graph is tf.get_default_graph():
    print("const1所在的图（Graph）是当前上下文默认的图")

# 关闭已用完的Session（会话）
sess.close()

# 第二种方法来创建和关闭Session
with tf.Session() as sess:
    result2 = sess.run(multiple)
    print("Multiple的结果是 %s " % result2)
