import tensorflow as tf

matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.],[2.]])
product = tf.matmul(matrix1, matrix2)

sess = tf.Session()
result = sess.run(product)
print (result)
'''
---------------------
作者：懒散的木木酱
来源：CSDN
原文：https://blog.csdn.net/weixin_44350307/article/details/87776080
版权声明：本文为博主原创文章，转载请附上博文链接！
'''