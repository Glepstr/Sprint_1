types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}


def get_unique_tickets(ticket_list, used_tickets):
    unique = []

    for ticket in ticket_list:
        if ticket not in used_tickets:
            unique.append(ticket)
            used_tickets.add(ticket)

    return unique


def merge_tickets(types_dict, tickets_dict):
    result = {}
    used_tickets = set()

    for priority in sorted(types_dict.keys()):
        bug_type = types_dict[priority]
        unique_tickets = get_unique_tickets(
            tickets_dict[priority],
            used_tickets
        )
        result[bug_type] = unique_tickets

    return result


tickets_by_type = merge_tickets(types, tickets)

print(tickets_by_type)