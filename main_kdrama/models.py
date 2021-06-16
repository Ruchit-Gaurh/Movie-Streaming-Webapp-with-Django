from django.db import models
# Create your models here.
class main_poster(models.Model):
    mobile_title = models.TextField()


class upload_serie(models.Model):

    min_width1600 = models.URLField()
    min_width1440 = models.URLField()
    min_width960 = models.URLField()
    min_width600 = models.URLField()
    img = models.URLField()
    title = models.CharField(max_length=300)
    image_description = models.CharField(max_length=1000)
    url = models.CharField(max_length=200)
    year = models.IntegerField()
    genres = models.CharField(max_length=300)
    cast = models.CharField(max_length=300)
    episodes = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/series/{self.url}'


class episodesss(models.Model):
    Parent_serie = models.CharField(max_length=300)
    parent_url = models.CharField(max_length=300)
    # episode = models.URLField()
    episode_number = models.CharField(max_length=300)
    onlyepisodenumber = models.IntegerField()
    video_embed = models.CharField(max_length=600)

    def __str__(self):
        return self.Parent_serie + self.episode_number

    def get_absolute_url(self):
        return f'/series/{self.parent_url}/episode{self.onlyepisodenumber}'


class epi(models.Model):
    serie_url = models.CharField(max_length=300)
    epi_no = models.IntegerField()
    epi_url = models.URLField()

    def __str__(self):
        return self.serie_url + ' ep no ' + f'{self.epi_no}'

class category1_name(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return "category 1" + self.title

class category1(models.Model):
    serie_tittle = models.CharField(max_length=300)
    serie_img = models.URLField()
    url = models.CharField(max_length=300)

    def __str__(self):
        return "category 1" + self.serie_tittle


class category2_name(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return "category 2" + self.title

class category2(models.Model):
    serie_tittle = models.CharField(max_length=300)
    serie_img = models.URLField()
    url = models.CharField(max_length=300)

    def __str__(self):
        return "category 2" + self.serie_tittle


class category3_name(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return "category 3" + self.title

class category3(models.Model):
    serie_tittle = models.CharField(max_length=300)
    serie_img = models.URLField()
    url = models.CharField(max_length=300)

    def __str__(self):
        return "category 3" + self.serie_tittle


class category4_name(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return "category 4" + self.title

class category4(models.Model):
    serie_tittle = models.CharField(max_length=300)
    serie_img = models.URLField()
    url = models.CharField(max_length=300)

    def __str__(self):
        return "category 4" + self.serie_tittle
class category5_name(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return "category 5" + self.title

class category5(models.Model):
    serie_tittle = models.CharField(max_length=300)
    serie_img = models.URLField()
    url = models.CharField(max_length=300)

    def __str__(self):
        return "category 5" + self.serie_tittle


class category6_name(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return "category 6" + self.title

class category6(models.Model):
    serie_tittle = models.CharField(max_length=300)
    serie_img = models.URLField()
    url = models.CharField(max_length=300)

    def __str__(self):
        return "category 6" + self.serie_tittle


class category7_name(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return "category 7" + self.title

class category7(models.Model):
    serie_tittle = models.CharField(max_length=300)
    serie_img = models.URLField()
    url = models.CharField(max_length=300)

    def __str__(self):
        return "category 7" + self.serie_tittle

        
class category8_name(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return "category 8" + self.title

class category8(models.Model):
    serie_tittle = models.CharField(max_length=300)
    serie_img = models.URLField()
    url = models.CharField(max_length=300)

    def __str__(self):
        return "category 8" + self.serie_tittle


class category9_name(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return "category 9" + self.title

class category9(models.Model):
    serie_tittle = models.CharField(max_length=300)
    serie_img = models.URLField()
    url = models.CharField(max_length=300)

    def __str__(self):
        return "category 9" + self.serie_tittle


class category10_name(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return "category 10" + self.title

class category10(models.Model):
    serie_tittle = models.CharField(max_length=300)
    serie_img = models.URLField()
    url = models.CharField(max_length=300)

    def __str__(self):
        return "category 10" + self.serie_tittle


class usertracker(models.Model):
    user_ip = models.CharField(max_length=300, blank=True, null=True)
    episode_watching = models.CharField(max_length=300)
    img = models.URLField()
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.user_ip