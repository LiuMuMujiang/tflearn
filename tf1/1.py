import tensorflow as tf

sess = tf.Session()

a = tf.placeholder("float")
b = tf.placeholder("float")
c = tf.constant(6.0)
d = tf.multiply(a, b)
y = tf.multiply(d, c)
print(sess.run(y, feed_dict={a: 3, b: 3}))

A = [[1.1, 2.3], [3.4, 4.1]]
Y = tf.matrix_inverse(A)
print(sess.run(Y))
'''
---------------------
作者：拾柴者
来源：CSDN
原文：https: // blog.csdn.net / qq_38404440 / article / details / 79893454
版权声明：本文为博主原创文章，转载请附上博文链接！
作者：懒散的木木酱
来源：CSDN
原文：https://blog.csdn.net/weixin_44350307/article/details/87776080
版权声明：本文为博主原创文章，转载请附上博文链接！
'''