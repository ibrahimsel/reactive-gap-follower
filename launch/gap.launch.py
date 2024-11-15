from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
import socket


def generate_launch_description():
    ld = LaunchDescription()
    hostname = socket.gethostname()
    config_file = os.path.join(
        get_package_share_directory("reactive_gap_follower"), "config", "params.yaml"
    )

    gap_follower_node = Node(
        package="reactive_gap_follower",
        executable="cass_gap_follower",
        name=f"cass_gap_follower_{hostname}",
        parameters=[config_file],
    )
    ld.add_action(gap_follower_node)
    return ld
