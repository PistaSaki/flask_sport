import tensorflow as tf

class Model:
    def __init__(self):
        self.floatX = tf.float32
        self.graph = tf.Graph()
        with self.graph.as_default():
            self.a = tf.placeholder(dtype=self.floatX, shape=[], name="a")
            self.b = tf.placeholder(dtype=self.floatX, shape=[], name="b")
            self.result = self.a + self.b
            
    def __call__(self, a:float, b:float) -> float:
        with self.graph.as_default(), tf.Session() as sess:
            feed_dict = {self.a: a, self.b: b}
            return sess.run(self.result, feed_dict)