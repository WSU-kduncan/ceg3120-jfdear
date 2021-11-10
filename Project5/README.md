1. Create an /etc/hosts file on each system that correlates hostnames to private IPs.  
![etcHosts_file](https://user-images.githubusercontent.com/77360294/141050305-a96b267e-15fc-4824-9ebf-073d40428cfd.PNG)  
linking private ips to hostnames to easily ssh
File is configured by correllating the private ips (our proxy and webserver) to their respective names  

2. Document how to SSH in between the systems utilizing their private IPs.  
First you would make sure you have a .ssh/config file  
in that file you would put the hosts and their details of how to connect as shown below  
![config_file](https://user-images.githubusercontent.com/77360294/141055755-edd7e914-e822-458b-a2c6-f773655f7f80.PNG)  
Make sure the private key is readable so that you are able to ssh  
Example of ssh between systems below  
![showing_how_to_ssh](https://user-images.githubusercontent.com/77360294/141055812-fb340ea8-acec-4fb0-9b33-0271b0d3673c.PNG)  

3. HAProxy configuration and documentation requirements  
How to install packages -  
sudo apt-get update  
apt-get install -y haproxy git python3 python3-pip  
  
what files were modified and location -  
file - hapee-lb.cfg  
location - /etc/haproxy/haproxy.cfg  
  
What configuration(s) were set -  
![haproxy_config](https://user-images.githubusercontent.com/77360294/141202499-916a0049-f17b-4a4b-addd-29a6bc6a86f8.PNG)    
  
How to restart the service after a configuration change -  
sudo systemctl stop haproxy.service  
sudo systemctl start haproxy.service  
or  
sudo systemctl restart haproxy.service  
  
Resources used (websites) -  
https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration/ - the four sections setup  


4. Webserver 1 and 2 configuration and documentation requirements  
How to install packages -  
apt-get update  
apt-get install -y apache2 git  

What file(s) where modified & their location -  
/var/www/html/index.html - where the html code is located  
  
What configuration(s) were set (if any) -   
webServer1 - ![webServer1_code](https://user-images.githubusercontent.com/77360294/141203792-45aa6336-40ce-44f5-aea1-221cc2053bd5.PNG)  
webServer2 - ![webServer2_code](https://user-images.githubusercontent.com/77360294/141203801-1308d102-b008-4697-a0cc-085ec640a2a8.PNG)  
  
How to restart the service after a configuration change -  
sudo systemctl stop apache2  
sudo systemctl start apache2  
or  
sudo systemctl restart apache2  
  
Resources used (websites) -  
https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04  
  

5. From the browser, when connecting to the proxy server, take two screenshots.  
![proxy_to_webServer1](https://user-images.githubusercontent.com/77360294/141204373-753a5c2a-b301-433e-97dd-47c8da0355e5.PNG)  

![proxy_to_webServer2](https://user-images.githubusercontent.com/77360294/141204385-13795d07-b2ae-4e39-827a-34a0a993455c.PNG)
  
6. (Optional) - link to your proxy  
http://3.231.35.94/

