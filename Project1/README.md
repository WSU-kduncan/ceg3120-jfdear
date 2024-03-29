Setup:  
  
Add a user - Command: adduser testuser, You can add a user to the AWS server by using the adduser command and then the name of the user.   

Initialize a repo - Command: git init --bare testrepo3.git, While logged in as the user you just created you can create git repository by using the command listed to create a bare repository with just the .git folder than you can clone from later.  

Permission - Ensure that the private key is writable and readable using chmod while logged in as the user. you can do this by doing chmod 600 key_name.pem.  

On the local system make a config file in your .ssh folder to hold the private key information that can be used later on in the git clone command shown.  

ssh keys - Make sure that the newly created user has the AWS instance public key in their .ssh/authorized_keys folder.  



Usage:  
  
Initialize a repo - Command: git init --bare testrepo3.git, this will make a git repository to store files and can run the commands mentioned later on.  

Clone - Command: git clone testuser@aws-ceg3120:testrepo3.git, If you don't want to create your own you can use git clone instead. git clone is used to essentially grab a existing repository and "copy" it to your current directory and can do the following commands mentioned next.  

status - Command: git status, git status shows if you made any changes in the repository and what you need to do next to commit those changes.  

Add - Command: git add file, on the git status screen it may tell you to "git add" a file to the commit without this you will not be able to commit changes on the file previously mentioned.     

Commit - git commit, this command will commit the changes that you added on the previous step and have you make a comment describing what changes you made so you can keep a record of your changes.  

Push - git push, this will finalize your changes to your git reposity and will show up now in your git repository.  

Proof:  
  
existing on the AWS instance - ![awsInstance_project1](https://user-images.githubusercontent.com/77360294/132079054-1f45e285-dd24-4304-9dd3-e3663fbdaad2.PNG)  

being cloned to your local system - ![clone_project1](https://user-images.githubusercontent.com/77360294/132079087-4040518e-16e7-4034-9e2f-feba27bd3cb6.PNG)

