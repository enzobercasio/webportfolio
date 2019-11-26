from django.db import models


# Create a blog model
# Add the blog app to the settings
# Create migration 
# Migrate
# add to the admin

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body =  models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
        
    def summary(self):
        return self.body[:100]

    def pub_date_short(self):
        return self.pub_date.strftime('%b %d %Y')