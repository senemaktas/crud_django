from django.db import models

# declare a new model with a name "prodaftModel"
class userModel(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    name = models.TextField(max_length = 50)
    email = models.TextField(max_length = 50)
    phone = models.CharField(max_length = 20) #define max_length for dcharfield

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title
           