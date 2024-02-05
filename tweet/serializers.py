from rest_framework import serializers

from tweet.models import Tweet, Comment


class TweetSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    last_update = serializers.DateTimeField(read_only=True)
    comments = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Tweet
        fields = ['id', 'text', 'last_update', 'comments']


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    # tweet = serializers.HyperlinkedRelatedField(
    #     'tweet-detail', queryset=Tweet.objects.all()
    # )
    # tweet = TweetSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'comment', 'commented_time', 'tweet']
