from django.db import models


# Create your models here.
class Projects(models.Model):
    # Fields
    project_name = models.CharField(max_length=30,
                                    help_text="Enter the project name here")
    project_desc = models.TextField(
        help_text="Enter the project description here")
    project_stack = models.CharField(
        max_length=20, help_text="Enter programming languages here")
    project_url = models.URLField(help_text="Link to the project if any")

    # methods
    def __str__(self):
        return f'{self.project_name}'


class Education(models.Model):

    # Fields
    degree_type = models.CharField(max_length=50, help_text="Program of study")
    institute_name = models.CharField(max_length=50,
                                      help_text="Enter the institute name")
    start_year = models.IntegerField(
        help_text="Enter the course starting year")
    end_year = models.IntegerField(help_text="Enter the course ending year")
    score = models.FloatField(
        help_text="Enter your score, here for instance 9.8")

    # methods
    def convert_score(self):
        """Converts the score taken from the score field and appends a string value"""
        return None

    def __str__(self):
        return f'{self.institute_name}\t{self.start_year}\t{self.end_year}\t{self.score}'