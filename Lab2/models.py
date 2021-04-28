from django.db import models
from django.http import Http404
from django.urls import reverse


class Category(models.Model):
    category = models.CharField(u'Категорія', max_length=250, help_text=u'Максимум 250 символів')
    slug = models.SlugField(u'Слаг')
    objects = models.Manager()

    class Meta:
        verbose_name = u'Категорія для публікації'
        verbose_name_plural = u'Категорії для публікацій'

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        try:
            url = reverse('articles-category-list', kwargs={'slug': self.slug})
        except:
            url = "/"
        return url


class Image(models.Model):
    image = models.ImageField('Image', upload_to='images')
    description = models.CharField(max_length=200)

    def all(self):
        return Image.objects.all()


class Article(models.Model):
    pub_date = models.DateField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    main_page = models.BooleanField()
    slug = models.SlugField(u'Слаг')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    images = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        try:
            # url = reverse('news-detail', kwargs={'item': self})
            # url = reverse('articles-category-list', kwargs={'slug': self.slug})
            url = reverse('news-detail', kwargs={'year': self.pub_date.year, 'month': self.pub_date.month, 'day': self.pub_date.day, 'slug': self.slug})
        except:
            raise Http404("Page not found")
        return url
