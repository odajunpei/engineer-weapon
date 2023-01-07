import datetime
from django.shortcuts import redirect
from django.views import generic
from . import mixins
from .forms import BS4ScheduleForm
from .models import Schedule


class MyCalendar(mixins.MonthCalendarMixin, mixins.WeekWithScheduleMixin, generic.CreateView):
    """月間カレンダー、週間カレンダー、スケジュール登録画面のある欲張りビュー"""
    template_name = 'studytime/mycalendar.html'
    model = Schedule
    date_field = 'date'
    form_class = BS4ScheduleForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        week_calendar_context = self.get_week_calendar()
        month_calendar_context = self.get_month_calendar()
        context.update(week_calendar_context)
        context.update(month_calendar_context)
        return context

    def form_valid(self, form):
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        day = self.kwargs.get('day')
        if month and year and day:
            date = datetime.date(
                year=int(year), month=int(month), day=int(day))
        else:
            date = datetime.date.today()
        schedule = form.save(commit=False)
        schedule.date = date
        schedule.user = self.request.user
        schedule.save()
        return redirect('studytime:mycalendar', year=date.year, month=date.month, day=date.day)


class MyCalendarUpdate(mixins.MonthCalendarMixin, mixins.WeekWithScheduleMixin, generic.UpdateView):
    """月間カレンダー、週間カレンダー、スケジュール登録画面のある欲張りビュー"""
    template_name = 'studytime/mycalendar.html'
    model = Schedule
    date_field = 'date'
    form_class = BS4ScheduleForm
