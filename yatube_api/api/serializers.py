from rest_framework import serializers


from posts.models import Comment, Group, Follow, Post


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
        read_only=True,
    )

    class Meta:
        model = Follow
        fields = (
            'user',
            'following',
        )


class PostSerializer(serializers.ModelSerializer):
    """Serializer for posts."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Post
        fields = (
            'id',
            'text',
            'author',
            'image',
            'group',
            'pub_date',
        )
