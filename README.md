# ChtoProishodit

Лаба номер 1. Ну здесь в общем и целом всё просто. 
Был создан простейший узел. Чтобы его запустить, надо ввести в терминале:
rosrun cringe_robot_package first_node.py. Время отчитывается идеально. Дабы прервать выполнение
программы, достаточно нажать CTRL + C. 

Лаба номер 2. Это уже было посложнее. 
В одном терминале делаем rosrun cringe_robot_package talker.py
В другом rosrun cringe_robot_package listener.py
И в третьем rosrun cringe_robot_package listener_next.py

Один узел - хорошо, а три еще лучше. Но работает всё как и должно (вроде бы)


Лаба номер 3. Самое сложное испытание. 

Первая часть задания еще более-менее. 
Дабы всё запустилось, необходимо ввести в терминале roslaunch cringe_robot_package prikol.launch new_topic_name:="че хотим" 

С помощью параметра pass_all_args="true" делаем так, чтобы второй launch файл видел наш аргумент new_topic_name. Иначе ничего работать не будет. 

Вторая часть задания. Самое интересное.
Запускаем так:

roslaunch cringe_robot_package KAZAHSTAN.launch 

Тем самым у нас будут беспрерывно работать два узла: Полиноминальный и суммирующий. Ждут своего часа, так сказать

А уже командой roslaunch cringe_robot_package KIRGIZIA.launch мы запускаем основной request узел. Через аргументы one_arg, anotherone_arg и andanotherone_arg можем вбить любые числа, какие только пожелаем. Дальше всё должно пойти по накатанной - числа в зависимости от своей позиции возносятся в соответсвующую степень, а затем суммируются. Пришлось очень сильно заморочиться через MultiArray, ибо я не придумал иного способа передать через Publisher несколько данных одного типа (в моём случае float'овские числа). Наверняка всё можно было сделать гораздо проще, но проделанной работой я крайне горжусь :)
