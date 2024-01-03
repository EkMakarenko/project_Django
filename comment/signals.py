from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from comment.models import Comment
from hotel.models import Hotel


@receiver(post_save, sender=Comment)
def post_save_comment(sender, instance, created, **kwargs):
    if created:
        print('Comment saved. Calculate new rating')
        recalculate_info_rating(instance_comment=instance.info_hotel)


@receiver(post_delete, sender=Comment)
def post_delete_comment(sender, instance, **kwargs):
    print('Comment deleted. Calculate new rating')
    recalculate_info_rating(instance_comment=instance.info_hotel)


def recalculate_info_rating(instance_comment: Hotel):
    comments = instance_comment.comments.all()
    total_rating = sum(comment.rating for comment in comments)
    instance_comment.rating = total_rating / len(comments) if comments else 0
    instance_comment.save()
