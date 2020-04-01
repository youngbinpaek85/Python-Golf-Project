from django.db import models
import re



class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        print(postData)
        if len(postData['firstinput']) < 2:
            errors["first"] = "First name should be at least 2 characters"
        if len(postData['lastinput']) < 2:
            errors["last"] = "Last name should be at least 2 characters"
        if len(postData['emailinput']) < 3:
            errors["email"] = "email should be at least 1 characters"
        if len(postData['pwinput']) < 1:
            errors["pw"] = " Password should be at least 1 characters"
        if len(postData['confpwinput']) < 1:
            errors["confpw"] = "Confirmation PW should be at least 5 characters"
        if postData['pwinput'] != postData['confpwinput']:
            errors['match']="Password doesn't match"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['emailinput']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        return errors

    def login_validator(self, postData):
        errors = {}
        print(postData)
        if len(postData['loginname']) < 3:
            errors["login"] = "email should be at least 3 characters"
        if len(postData['loginpass']) < 1:
            errors["loginpw"] = " Password should be at least 5 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['loginname']):    # test whether a field matches the pattern            
            errors['login'] = "Invalid email address!"
        return errors

class User(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email =models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    objects = UserManager()

class Message(models.Model):
    message = models.TextField()
    message_creator = models.ForeignKey(User, related_name="created_messages", on_delete = models.CASCADE)
    liking_users = models.ManyToManyField(User, related_name="liked_messages")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment= models.TextField()
    parent_message = models.ForeignKey(Message, related_name="related_comments", on_delete = models.CASCADE)
    comment_creator = models.ForeignKey(User, related_name="created_comments", on_delete = models.CASCADE)
    liking_users = models.ManyToManyField(User, related_name="liked_comments")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)