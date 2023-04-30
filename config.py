TOKEN = 'MTA5OTI3MTcxMzc2MzYzNTI1MA.G39ajY.TIYlzKZKx8o0KvZjHl7qFO-ZqvnvZPdWR-Ll9g'

with open('words.txt', encoding='utf8') as ban_words:
    CENSORED_WORDS = [i.strip() for i in ban_words.readlines()]

ROLES = {
    'first bot': '905695911898914828',
    'vasiliy': '1097030925654691954',
    'новая роль': '1097453385910865980',
    'Звягенцев Александр': '1097453450603802644'
}
