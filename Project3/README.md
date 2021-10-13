Part 1  
VPC - It is the Virtual Private Cloud, it is the virtual network dedicated to your AWS account and can have multiple of these. It includes the Subnet, Internet gateway, Route Table, Security groups, and CIDR block. It is all that working together.  
![image](https://user-images.githubusercontent.com/77360294/137032092-2ea3124f-05ca-4650-a61c-55a01b401248.png)  
Subnet - A range of IP addresses in your VPC  
![image](https://user-images.githubusercontent.com/77360294/137032296-167eae5d-c02c-4ab5-a19c-40b82bb7e9f7.png)  
Internet gateway - Gateway to attach to the VPC to enable communications between the VPC(and resources in the VPC) and the internet  
![image](https://user-images.githubusercontent.com/77360294/137032725-8f673fa8-b940-4da5-95de-08bb011397e7.png)  
Route table - Set of rules (routes) that determine where network traffic is directed  
![image](https://user-images.githubusercontent.com/77360294/137033385-6fdbe4c7-61a7-4cf5-b6b1-992844b8efa6.png)  
Security group - Basically network firewall that says what traffic can come inbound and outbound of the network  
![image](https://user-images.githubusercontent.com/77360294/137033206-5f71d896-f1b9-4bfc-8d39-cb6efcee4b41.png)  
  
Part 2  
1. AMI - Ubuntu Server 20.04 LTS (HVM), SSD Volume Type - ami-09e67e426f25ce0d7 (64-bit x86) / ami-00d1ab6b335f217cf (64-bit Arm)  
default username is ubuntu  
Instance type is t2.micro  
![image](https://user-images.githubusercontent.com/77360294/137034793-9d08d217-56c0-45dd-bf53-b0a80fbd741a.png)  
  
2. How to attach instance to VPC  
![image](https://user-images.githubusercontent.com/77360294/137034984-3f96567f-bb55-4442-af8e-8c1fe4fd372e.png)  
  
3. Do not auto-assign Public IP address because we want an elastic IP address that will stay the same and not change on us.  
![image](https://user-images.githubusercontent.com/77360294/137035088-cfa86840-d7de-4c08-9e8b-fb9a97db4f3d.png)  
  
4. How to create and attach storage volume to instance? You would do all this using the gui below  
![image](https://user-images.githubusercontent.com/77360294/137035444-5f55a067-1bf6-4c47-b70c-b1ccf105bb62.png)  
  
5. How to tag instance with a Name?  
![image](https://user-images.githubusercontent.com/77360294/137035516-b5873cb3-ceba-44e5-aacf-8daa84d6a01f.png)  
  
6. How to associate security groups?  
![image](https://user-images.githubusercontent.com/77360294/137035632-5a1d7bca-3a1a-470e-adcc-2beaa5e778f6.png)  
  
7. Create/reserve and associate Elastic IP address with instance? You would get the elastic IP and then associate it with your instance. Screenshots below.  
![image](https://user-images.githubusercontent.com/77360294/137035917-e26f0300-b4ef-4b3e-be8b-d248d7b887bd.png)  
![image](https://user-images.githubusercontent.com/77360294/137036077-4c7bd7a3-db3d-46a3-a5a9-9013264d419e.png)  
![image](https://user-images.githubusercontent.com/77360294/137036175-6d2c78df-1c62-433e-bc7c-ce9d50437463.png)  
  
8. Instance details  
![image](https://user-images.githubusercontent.com/77360294/137062644-38ed9b79-3c5b-43aa-a2a4-c5499f8f9841.png)   
  
9. How to change hostname?  
You have to first sudo vim /etc/hostname and put your new hostname in there.  
then sudo vim /etc/hosts and replace any instance of old hostname with new hostname  
then reboot.  
![image](https://user-images.githubusercontent.com/77360294/137036912-d853301f-dd6a-4feb-8b0c-15d6979aaa19.png)  
![image](https://user-images.githubusercontent.com/77360294/137037111-4758c3bb-2001-42f0-8102-5459347531f8.png)  
  
10. Screenshot of successful SSH  
![image](https://user-images.githubusercontent.com/77360294/137037393-d1210b5b-f9b0-4395-995a-cada0db392d9.png)
