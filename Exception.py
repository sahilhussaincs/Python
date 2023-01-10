from logging import exception


x=17
if x> 10:
raise exception('the value of x should not exceed 10, the value of x was:{}' format(x))