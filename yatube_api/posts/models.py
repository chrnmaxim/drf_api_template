from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

CHARS_LIMIT: int = 30
MAX_LENGTH: int = 256


class Group(models.Model):
    """Model for groups."""
    title = models.CharField(
        'Название',
        max_length=MAX_LENGTH
    )
    slug = models.SlugField(
        'Идентификатор',
        unique=True
    )
    description = models.TextField(
        'Описание'
    )

    class Meta:
        """Inner Meta class of Group model."""
        verbose_name = 'группа'
        verbose_name_plural = 'Группы'
        ordering = ('id',)

    def __str__(self):
        """Displays Group title in admin panel."""
        return self.title[:CHARS_LIMIT]


class Post(models.Model):
    """Model for posts."""
    text = models.TextField(
        'Текст'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    image = models.ImageField(
        'Изображение',
        upload_to='posts/',
        blank=True
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Группа'
    )

    class Meta:
        """Inner Meta class of Post model."""
        verbose_name = 'пост'
        verbose_name_plural = 'Посты'
        ordering = ('pub_date',)
        default_related_name = 'posts'

    def __str__(self):
        """Displays Post text in admin panel."""
        return self.text[:CHARS_LIMIT]


class Comment(models.Model):
    """Model for post's comments."""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Пост'
    )
    text = models.TextField(
        'Текст'
    )
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        """Inner Meta class of Comment model."""
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('id',)
        default_related_name = 'comments'

    def __str__(self):
        """Displays Comment text in admin panel."""
        return self.text[:CHARS_LIMIT]


class Follow(models.Model):
    """"Model for user following."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followers',
        verbose_name='Пользователь'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followings',
        verbose_name='Подписан'
    )

    class Meta:
        """Inner Meta class of Follow model."""
        verbose_name = 'подписка'
        verbose_name_plural = 'Подписка'
        ordering = ('id',)
        constraints = [
            models.UniqueConstraint(
                name='unique_following',
                fields=['user', 'following']
            )
        ]

    def __str__(self):
        """Displays user's following in admin panel."""
        return f'{self.user} подписан(а) на {self.following}'
