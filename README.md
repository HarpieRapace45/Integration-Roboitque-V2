# Integration-Roboitque-V2

## Installation

en premier lieu, vous devez cloner le dépot dans le dossier que vous désirez : 
  - https://github.com/HarpieRapace45/Integration-Roboitque-V2.git
  
par le suite vous devez configurer ros sur votre machine, si il n'est pas installer, suivez le tuto suivant : http://wiki.ros.org/noetic/Installation/Ubuntu
Sinon, vous pouvez exécuter là commande suivante : 
  - . /opt/ros/noetic/setup.bash
  
ensuite déplacer vous dons le dossier créer avec le git clone : 
  - cd Integration-Roboitque-V2/catkin_ws

ensuite, vous devez netoyer tout les fichier indésirable puis build le projet graçe à la commande suivante :
   - catkin clean
   - catkin build
   
 vous pouvez ensuite sourcer le fichier du projet : 
   - . devel/setup.bash
   
Et vous disposer maintenant d'un projet installer et configurer !

## block de commande pour l'installation :

https://github.com/HarpieRapace45/Integration-Roboitque-V2.git
. /opt/ros/noetic/setup.bash
 cd Integration-Roboitque-V2/catkin_ws
catkin clean
catkin build
. devel/setup.bash

## création du package 
en premier, dans un nouveau terminal, vous devez avoir un roscore qui tourne pendant l'ensemble de vos manipulation sur ce projet : 
   - . /opt/ros/noetic/setup.bash
   - roscore

vous pouvez creer un package ou utiliser celui déjà dans le dossier pour la planification de trajectoire, tout dabord, vous pouvez lancer Moveit :
  - roslaunch moveit_setup_assistant setup_assistant.launch
  
ensuite, vous pouvez soit editer le package déjà existant avec "Edit Existing Moveit Configuration Package" et allez selection le dossier ./src/hc10_moveit_config  ou alors vous pouvez créer un nouveau package en cliquant sur le bouton "Create New Moveilt Configuration Package" et en allant chercher le fichier urdf à cette emplacement :  ./src/motoman/motoman_hc10_support/urdf/hc10.xacro

une fois le package modifier ou créer, vous devez rebuild le projet avec cette serie de commande à réalisé à la racine du projet ros ( ./catkin_ws ) : 
  catkin clean
  catkin build
  . devel/setup.bash
  
  
## planifiaction grâce à python 

configurer 2 terminal avec ces commande à la racine du projet ros :
  . /opt/ros/noetic/setup.bash
  . devel/setup.bash
  
dans le premier, vous pouvez ouvrir Rviz avec la commande suivant :
  - roslaunch hc10_moveit_config demo.launch
dans le second il vous suffit de d'éxécuter le code python qui est dans le projet avec la comande suivant ;
  - python3 hcPy.py
  
## Simulation dans Gazebo (non terminer) 

Pour cette parti, il vous suffit d'éxécuter cette commande pour que Rviz et Gazebo se lance :
  - roslaunch hc10_moveit_config demo_gazebo.launch
  
