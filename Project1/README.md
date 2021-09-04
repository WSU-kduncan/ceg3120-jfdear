Setup:  
Add a user - adduser testuser  
Initialize a repo - git init --bare testreop3.git  
permission - Ensure that the private key is writable and readable using chmod  
On the local system make a config file in your .ssh folder to hold the private key information that can be used later on in the git clone command shown.  
keys - Make sure that the newly created user has the AWS instance public key in there authorized key folder.  



Usage:  
Clone - git clone testuser@aws-ceg3120:testrepo3.git  
Add - git add file  
Commit - git commit  
Push - git push  

Proof:  
existing on the AWS instance - ![awsInstance_project1](https://user-images.githubusercontent.com/77360294/132079054-1f45e285-dd24-4304-9dd3-e3663fbdaad2.PNG)  

being cloned to your local system - ![clone_project1](https://user-images.githubusercontent.com/77360294/132079087-4040518e-16e7-4034-9e2f-feba27bd3cb6.PNG)

