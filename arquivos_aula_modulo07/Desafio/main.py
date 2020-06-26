from api.models import User, Agent, Event, Group
from datetime import datetime, timedelta


def get_active_users() -> User:
    """Traga todos os usuários ativos, seu último login deve ser
        menor que 10 dias """
    time_since_last_login = (datetime.today() - timedelta(days=10))
    users = User.objects.filter(
        last_login__gte=time_since_last_login
    )
    return users


def get_amount_users() -> User:
    """Retorne a quantidade total de usuarios do sistema """
    count_users = User.objects.count()
    return count_users


def get_admin_users() -> User:
    """Traga todos os usuarios com grupo = 'admin"""
    users = User.objects.filter(group__name='admin')
    return users


def get_all_debug_events() -> Event:
    """Traga todos os eventos com tipo debug"""
    events = Event.objects.filter(level='debug')
    return events


def get_all_critical_events_by_user(agent) -> Event:
    """Traga todos os eventos do tipo critico de um usuário específico"""
    events = Event.objects.filter(level='critical', agent=agent)
    return events


def get_all_agents_by_user(username) -> Agent:
    """Traga todos os agentes de associados a um usuário
        pelo nome do usuário"""
    agents = Agent.objects.filter(user__name=username)
    return agents


def get_all_events_by_group() -> Group:
    """Traga todos os grupos que contenham alguem que possua um agente
        que possuem eventos do tipo information"""
    groups = Group.objects.filter(
        user__agent__event__level='information'
    )
    return groups
