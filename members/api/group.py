import graphene
from framework.api.user import UserBasicObj
from ..models import Group, MentorGroup
from django.db.models import F
from graphql_jwt.decorators import login_required
from django.contrib.auth.models import User
from attendance.models import Module
from status.models import Thread as StatusThread




class GroupObj(graphene.ObjectType):
    name = graphene.String()
    statusUpdateEnabled = graphene.Boolean()
    attendanceEnabled = graphene.Boolean()
    admins = graphene.List(UserBasicObj)
    members = graphene.List(UserBasicObj)
    membersCount = graphene.Int()

    def resolve_membersCount(self, info):
        return Group.objects.annotate(
            username=F('members__username')
        ).filter(id=self['id']).count()

    def resolve_admins(self, info):
        return Group.objects.values().annotate(
            username=F('admins__username'),
            first_name=F('admins__first_name'),
            last_name=F('admins__last_name'),
            date_joined=F('admins__date_joined'),
            is_active=F('admins__is_active'),
            is_admin=F('admins__is_superuser'),
        ).filter(id=self['id'])

    @graphene.resolve_only_args
    def resolve_members(self):
        return Group.objects.values().annotate(
            username=F('members__username'),
            first_name=F('members__first_name'),
            last_name=F('members__last_name'),
            date_joined=F('members__date_joined'),
            is_active=F('members__is_active'),
            is_admin=F('members__is_superuser'),
        ).filter(id=self['id'])


class Query(object):
    group = graphene.Field(
        GroupObj,
        id=graphene.Int(required=True)
    )
    groups = graphene.List(GroupObj)

    @login_required
    def resolve_group(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Group.objects.values().get(id=id)
        raise Exception('Group ID is a required parameter')

    @login_required
    def resolve_groups(self, info, **kwargs):
        return Group.objects.values().all()


class CreateGroup(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        admin_ids = graphene.List(graphene.Int)
        member_ids = graphene.List(graphene.Int)
        attendance_enabled = graphene.Boolean()
        status_update_enabled = graphene.Boolean()
        attendance_module_id = graphene.Int()
        thread_id = graphene.Int()
        telegram_bot = graphene.String()
        telegram_group = graphene.String()

    ok = graphene.Boolean()
    group = graphene.Field(GroupObj)

    @login_required
    def mutate(self, info, name, admin_ids=None, member_ids=None, attendance_enabled=False,
               status_update_enabled=False, attendance_module_id=None, thread_id=None,
               telegram_bot=None, telegram_group=None):
        group = Group.objects.create(
            name=name,
            attendanceEnabled=attendance_enabled,
            statusUpdateEnabled=status_update_enabled,
            telegramBot=telegram_bot or '',
            telegramGroup=telegram_group or '',
        )

        if attendance_module_id:
            try:
                group.attendanceModule = Module.objects.get(id=attendance_module_id)
            except Module.DoesNotExist:
                raise Exception('Attendance Module not found')

        if thread_id:
            try:
                group.thread = StatusThread.objects.get(id=thread_id)
            except StatusThread.DoesNotExist:
                raise Exception('Status thread not found')

        group.save()

        if admin_ids:
            admins = User.objects.filter(id__in=admin_ids)
            group.admins.set(admins)

        if member_ids:
            members = User.objects.filter(id__in=member_ids)
            group.members.set(members)

        return CreateGroup(ok=True, group=Group.objects.values().get(id=group.id))


class CreateMentorGroup(graphene.Mutation):
    class Arguments:
        mentor_id = graphene.Int(required=True)
        mentee_ids = graphene.List(graphene.Int)
        send_report = graphene.Boolean()
        forward_status = graphene.Boolean()

    ok = graphene.Boolean()
    mentor_group = graphene.Field(lambda: graphene.String)

    @login_required
    def mutate(self, info, mentor_id, mentee_ids=None, send_report=False, forward_status=False):
        try:
            mentor = User.objects.get(id=mentor_id)
        except User.DoesNotExist:
            raise Exception('Mentor user not found')

        mg = MentorGroup.objects.create(
            mentor=mentor,
            sendReport=bool(send_report),
            forwardStatusUpdates=bool(forward_status)
        )

        if mentee_ids:
            mentees = User.objects.filter(id__in=mentee_ids)
            mg.mentees.set(mentees)

        return CreateMentorGroup(ok=True, mentor_group=str(mg))


class Mutation(object):
    create_group = CreateGroup.Field()
    create_mentor_group = CreateMentorGroup.Field()
