from django.db import models

# Create your models here.


#
class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name="项目名称")
    description = models.TextField(verbose_name="描述")
    manager = models.ForeignKey("accounts.User", on_delete=models, verbose_name="负责人", related_name="managers",
                                default=None, null=True, blank=True)
    address = models.CharField(max_length=100, verbose_name="地址")

    def __str__(self):
        return self.name

#长期保洁
class LongProject(Project):
    pass

#开荒保洁
class DevProject(Project):
    pass


