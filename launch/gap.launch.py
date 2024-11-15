from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
import os
import socket


def generate_launch_description():
    ld = LaunchDescription()
    hostname = socket.gethostname()
    config_file = os.path.join(
        get_package_share_directory("reactive_gap_follower"), "config", "params.yaml"
    )
    racecar_namespace_arg = DeclareLaunchArgument(
        "racecar_namespace",
        default_value=f"{os.getenv('racecar_ns', 'racecar')}",
        description="Racecar Namespace",
    )

    gap_follower_node = Node(
        package="reactive_gap_follower",
        executable="cass_gap_follower",
        name=f"cass_gap_follower_{hostname}",
        parameters=[
            config_file,
            {"racecar_namespace": LaunchConfiguration("racecar_namespace")},
        ],
    )
    ld.add_action(racecar_namespace_arg)
    ld.add_action(gap_follower_node)
    return ld
