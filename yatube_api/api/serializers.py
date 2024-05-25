from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for post's comments."""
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = Comment
        fields = (
            'id',
            'author',
            'post',
            'text',
            'created',
        )
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for groups."""

    class Meta:
        model = Group
        fields = (
            'id',
            'title',
            'slug',
            'description',
        )


class FollowSerializer(serializers.ModelSerializer):
    """Serializer for following."""
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Follow
        fields = (
            'user',
            'following',
        )
        validators = (
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message=('Вы уже подписаны на данного пользователя.')
            ),
        )

    def validate(self, data):
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError(
                'Подписка на самого себя невозможна'
            )
        return data


class PostSerializer(serializers.ModelSerializer):
    """Serializer for posts."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Post
        fields = '__all__'
