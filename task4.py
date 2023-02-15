# based on ros2 doc tutorial: https://docs.ros.org/en/eloquent/Tutorials/Writing-A-Simple-Py-Publisher-And-Subscriber.html#write-the-publisher-node

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscriber_ = self.create_subscription(String, '/turtle1/color_sensor', self.sub_callback, 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def sub_callback(self, data):
        self.get_logger().info(f'Received color sensor msg: {data.data}')

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 1.0
        msg.angular.z = 1.0
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing Twist msg')
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()