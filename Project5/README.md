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
  
  
How to restart the service after a configuration change -  
sudo systemctl stop haproxy.service  
sudo systemctl start haproxy.service  
  
Resources used (websites) -  


4. Webserver 1 and 2 configuration and documentation requirements  

5. From the browser, when connecting to the proxy server, take two screenshots.  

6. (Optional) - link to your proxy  

