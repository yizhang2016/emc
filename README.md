# emc

This implementation is a web app using Django / Python (hope it's fine so far). 

The project was deployed on an AWS EC2 instance for simple test, the link is as followed (note the port number is 8123):
http://ec2-52-205-252-11.compute-1.amazonaws.com:8123/emc_tiny/

Since the need and demand for this project is not that specific (I'm not sure if this is intentional or kind of open-ended). Here is just little about what I thought to improve it on top of this baseline:

1. If you really need very large number as input, my idea is probably to cache some computation result (1000th, 10000th, 100000th num, etc) and do the computation in parallel in some ways. For example, if n = 20K, you may shard the computation and result to 0-10K and 10001-20K (you cached num[10000] and num[10001] in an initial process before), and you merge the result in some ways at the user end.

2. If you expect me to make it more robust and avoid some security problem, one of my current idea is to add proxy/load balancer and expand the web services into a small cluster with few nodes rather than just one. In this case, the traffic may be under control and once any node crash, you still have other nodes as a back-up.




To run the server on your localhost, execute the following command from inside the top directory (Django should be installed):

$ python manage.py runserver
