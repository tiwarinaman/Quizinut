from django import template

from quiz.models import Result

register = template.Library()


@register.simple_tag(name='is_job_already_applied')
def is_job_already_applied(quiz_id, student):
    attempt = Result.objects.filter(student__uname=student, quiz__id=quiz_id)
    if attempt:
        return True
    else:
        return False
