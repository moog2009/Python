# -*- coding: utf-8 -*-

#一共100辆车
cars=100
#一辆车的空闲数
space_in_a_car=4.0 #没必须，整数型亦可
#司机30人
drivers=30
#乘客90人
passengers=90
#没有人开的车数
cars_not_driven=cars-drivers
#有人开的车数
cars_driven=drivers
#平均每辆车的乘客数
avarage_passengers_per_car=carpool_capacity/passengers #carpool_capacity没有定义赋值
#可以使用车的总运力
carpool_capacity=cars_driven*space_in_a_car
#avarage_passengers_per_car=passengers/cars_driven


print "There are", cars,"cars available."
print "There are only",drivers,"drivers available."
print "There will be",cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "we need to put about",avarage_passengers_per_car,"in each car."