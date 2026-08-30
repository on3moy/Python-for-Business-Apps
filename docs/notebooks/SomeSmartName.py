def get_taxable_income(income):
    # Federal tax bracket ranges for single
    # (Base Range, (Base Pay, Rate Pay))
    federal_tax_bracket = (
        (0, (0, .10))
        ,(11000, (1100, .12))
        ,(44725, (5147, .22))
        ,(95375, (16290, .24))
        ,(182100, (37104, .32))
        ,(231250, (52832, .35))
        ,(578125, (174238.25, .37))
    )

    # California State tax brackets for single
    state_tax_bracket = ( 
        (0, (0, .01))
        ,(10412, (104.12, .02))
        ,(24684, (389.56, .04))
        ,(38959, (960.56, .06))
        ,(54081, (1867.88, .08))
        ,(68350, (3009.4, .093))
        ,(349137, (29122.59, .103))
        ,(418961, (36314.46, .113))
        ,(698271, (67876.49, .123))
    )

    # Calculate federal tax
    fed_range = None
    for inc, rate in federal_tax_bracket:
        if income >= inc:
            fed_range = (inc, rate)
    
    fed_base_range = fed_range[0]
    fed_base_pay = fed_range[1][0]
    fed_rate_pay = fed_range[1][1]
    federal_tax = fed_base_pay + fed_rate_pay * (income - fed_base_range)

    # Calculate state tax
    state_range = None
    for inc, rate in federal_tax_bracket:
        if income >= inc:
            state_range = (inc, rate)
    
    state_base_range = state_range[0]
    state_base_pay = state_range[1][0]
    state_rate_pay = state_range[1][1]
    state_tax = state_base_pay + state_rate_pay * (income - state_base_range)
    
    total_taxed = federal_tax + state_tax

    if total_taxed == 0:
        percent_taxed = 0
    else:
        percent_taxed = total_taxed / income
    
    print(f'Income: {income}')
    print(f'You get taxed ${total_taxed:,.2f}, which is {percent_taxed :.0%}')
    print(f'Which means you really earn ${income - (total_taxed):,.2f}')
    print(f'Monthly: {(income - (total_taxed)) / 52 * 4:,.2f}')
    return total_taxed

def main():
    '''Main program'''

    user_input = input('What is your annual salary? ')

    try:
        income = int(user_input.replace(',',''))

        return get_taxable_income(income)
    except:
        print('Please enter a number')
    

if __name__ == '__main__':
    main()