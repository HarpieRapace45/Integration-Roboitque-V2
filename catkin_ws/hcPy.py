from re import I
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import sys
from math import pi
import copy


moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node("robot_controlleur", anonymous=False)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "hc10_arm"
move_group = moveit_commander.MoveGroupCommander(group_name)

rospy.sleep(2)

joint_goal = move_group.get_current_joint_values()
joint_goal[0] = 0
joint_goal[1] = 0
joint_goal[2] = 0
joint_goal[3] = 0
joint_goal[4] = 0
joint_goal[5] = 0  

move_group.go(joint_goal, wait=True)
move_group.stop()

waypoint = [] 
pos_start = move_group.get_current_pose().pose
box_pose = geometry_msgs.msg.PoseStamped()
box_pose.header.frame_id = "world"

nom_box_1 = "box utile"
nom_box_2 = "box utile 2"

box_pose.pose = copy.deepcopy(pos_start)

waypoint.append(copy.deepcopy(pos_start))
pos_start.position.y += 1
waypoint.append(copy.deepcopy(pos_start))
pos_start.position.z += 1
waypoint.append(copy.deepcopy(pos_start))

box_pose.pose.position.y += 0.5
box_pose.pose.position.z += 0.25
scene.add_box(nom_box_1, copy.deepcopy(box_pose), size=(0.175, 0.175, 0.175))
box_pose.pose.position.y += 0.4
box_pose.pose.position.z += 0.5
scene.add_box(nom_box_2, copy.deepcopy(box_pose), size=(0.175, 0.175, 0.175))

rospy.sleep(2)

while len(scene.get_known_object_names())<3: 
    pass

( plan, fraction) = move_group.compute_cartesian_path(waypoint, 0.01, 0.0)
print(plan)
move_group.execute(plan, wait=True)

scene.remove_world_object(nom_box_1)
scene.remove_world_object(nom_box_2)

print(scene.get_known_object_names())
rospy.sleep(2)





