from __future__ import absolute_import, division, print_function, unicode_literals

# !pip install -q tensorflow-gpu==2.0.0-rc1
import tensorflow as tf

tf.compat.v1.disable_eager_execution()

hello_constant = tf.constant('Hello, TensorFlow!')

with tf.compat.v1.Session() as ses:
    print(ses.run(hello_constant))
