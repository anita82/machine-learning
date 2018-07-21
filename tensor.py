# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 23:30:21 2018

@author: Anita
"""

import tensorflow as tf

# Create TensorFlow object called tensor
hello_constant = tf.constant('Hello World!')

with tf.Session() as sess:
    # Run the tf.constant operation in the session
    hello_constant.add('d')
    output = sess.run(hello_constant)
    print(output)