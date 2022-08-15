from tabnanny import verbose
from django.db import models


class Task(models.Model):
    EH_LEVEL = "eh"
    LOW_LEVEL = "low"
    MEDIUM_LEVEL = "medium"
    HIGH_LEVEL = "high"
    LIFE_DEPEND = "life_depend"
    priority_level = [
        (EH_LEVEL, "If I Had Time I Will Do That"),
        (LOW_LEVEL, "Need My Attention"),
        (MEDIUM_LEVEL, "Better Be Done In Time"),
        (HIGH_LEVEL, "It Has To Be Done On Time"),
        (LIFE_DEPEND, "It Has To Be Done Or I Lose Something In My Life."),
    ]
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="title", max_length=255)
    start_date = models.DateField(
        verbose_name="Start Date",
    )
    end_date = models.DateField(
        verbose_name="End Date",
    )
    start_time = models.TimeField(
        verbose_name="Start Time",
    )
    end_time = models.TimeField(
        verbose_name="End Time",
    )
    description = models.TextField(
        verbose_name="Description",
        blank=True,
        help_text="Describe Your Task Here.",
    )
    priority = models.CharField(
        verbose_name="Priority",
        choices=priority_level,
        default=MEDIUM_LEVEL,
        max_length=255,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
