from django.db import models

# declare a new model with a name "prodaftModel"
class userModel(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    name = models.TextField(max_length = 30)
    email = models.TextField(max_length = 30)
    phone = models.TextField(max_length = 20) #define max_length for dcharfield

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title
           