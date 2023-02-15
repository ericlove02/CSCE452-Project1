import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ColorSensorSubscriber(Node):
    def __init__(self):
        super().__init__('color_sensor_subscriber')
        self.subscription = self.create_subscription(String, '/turtle1/color_sensor', self.callback, 10)
        self.subscription  # prevent unused variable warning

    def callback(self, msg):
        self.get_logger().info("Received message: '%s'" % msg.data)

def main(args=None):
    rclpy.init(args=args)
    color_sensor_subscriber = ColorSensorSubscriber()
    rclpy.spin(color_sensor_subscriber)
    color_sensor_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
