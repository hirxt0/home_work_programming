def check_ticket(ticket: str) -> bool:
    try:
        if len(ticket) != 6 :
            return 'Invalid ticket'
        
        first_half = ticket[:3]
        second_half = ticket[3:]

        if sum([int(i) for i in first_half]) == sum([int(i) for i in second_half]):
            return 'Lucky ticket'
        
        return 'Unlucky ticket'
    except:
        return 'Invalid input'


print(check_ticket('101020'))
print(check_ticket(20020020))