import pandas as pd
import random as r

db_df = pd.read_csv('tables/DBLS17.csv')
hard_df = pd.read_csv('tables/HARDS17.csv')
das_df = pd.read_csv('tables/SplitDASS17.csv')
ndas_df = pd.read_csv('tables/SplitNDASS17.csv')

def pick_table():
    while True:
        table = input('Select a table.\n1: Double S17\n2: Hard Hand S17\n3: Split DAS S17\n4: Split NDAS S17\n5: Exit\n')
        try:
            table = int(table)
            if table == 1:
                return db_df, 1
            elif table == 2:
                return hard_df, 2
            elif table == 3:
                return das_df, 3
            elif table == 4:
                return ndas_df, 4
            elif table == 5:
                return 'q', 'q'
            else:
                print('Please enter a valid number.')
        except:
            print('Please enter a valid number.')

def get_vals(df, count_min, count_max):
    rand_int_col = r.randint(1, len(df.columns)-1)
    rand_int_row = r.randint(0, len(df.index)-1)
    ran_val = df.iat[rand_int_row, rand_int_col]
    dealer_card = df.columns[rand_int_col]
    player_hand = df.iloc[rand_int_row, 0]
    count = r.randint(count_min, (count_max-1))
    return dealer_card, player_hand, ran_val, count, rand_int_col, rand_int_row

def what_should_you_do(df_num, value, count):
    try:
        value = int(value)
        if df_num == 1:
            if value <= count:
                return 1, 'double'
            elif value > count:
                return 2, 'not double'
        elif df_num == 2:
            if value <= count:
                return 2, 'stand'
            elif value > count:
                return (1, 'hit')
        elif df_num == 3 or df_num == 4:
            if value <= count:
                return 1, 'split'
            elif value > count:
                return 2, 'not split'
    except:
        if df_num == 1:
            if value == 'db':
                return 1, 'double'
            elif value == '-':
                return 2, 'not double'
        elif df_num == 2:
            if value == 'h':
                return 1, 'hit'
            elif value == '-':
                return 2, 'stand'
        elif df_num == 3 or df_num == 4:
            if value == 'spl':
                return 1, 'split'
            elif value == '-':
                return 2, 'not split'
            elif value == '8*':
                if count >= 8:
                    return 2, 'not split'
                elif count < 8:
                    return 1, 'split'
            elif value == '6*':
                if count >= 6:
                    return 2, 'not split'
                elif count < 6:
                    return 1, 'split'

def user_guess(dealer_card, player_hand, answer, count, df_num):
    
    while True:
        print("Dealer's Up Card: " + str(dealer_card))
        print("Player's Hand: " + str(player_hand))
        print("Count: " + str(count))
        if df_num == 1:
            guess = input('What should you do?\n1: Double\n2: Do not double\n3: Exit\n')
            try:
                guess = int(guess)
                if guess in [1,2,3]:
                    if guess == answer:
                        return True
                    elif guess == 3:
                        return 'q'
                    else:
                        return False
                else:
                    print('Please enter a valid number')
            except:
                print('Please enter a valid number')
        elif df_num == 2:
            guess = input('What should you do?\n1: Hit\n2: Stand\n3: Exit\n')
            try:
                guess = int(guess)
                if guess in [1,2,3]:
                    if guess == answer:
                        return True
                    elif guess == 3:
                        return 'q'
                    else:
                        return False
                else:
                    print('Please enter a valid number')
            except:
                print('Please enter a valid number')
        elif df_num == 3 or df_num == 4:
            guess = input('What should you do?\n1: Split\n2: Do not split\n3: Exit\n')
            try:
                guess = int(guess)
                if guess in [1,2,3]:
                    if guess == answer:
                        return True
                    elif guess == 3:
                        return 'q'
                    else:
                        return False
                else:
                    print('Please enter a valid number')
            except:
                print('Please enter a valid number')

def alter_table():
    df, df_num = pick_table()
    x=0
    dict_to_del = {}
    for i in df["Player’s Hand"]:
        print(i)
        dict_to_del[str(i)] = x
        x += 1
    while True:
        to_drop = input('Please enter the hand you would like to remove.(q to quit)\n')
        to_drop = str(to_drop)
        if to_drop in dict_to_del.keys():
            if df_num == 1:
                df.drop(dict_to_del[to_drop], inplace=True)
                df.reset_index(drop=True, inplace=True)
                df.to_csv('tables/DBLS17.csv')
                print('Table updated succesfully.')
                break
            elif df_num == 2:
                df.drop(dict_to_del[to_drop], inplace=True)
                df.reset_index(drop=True, inplace=True)
                df.to_csv('tables/HARDS17.csv')
                print('Table updated succesfully.')
                break
            elif df_num == 3:
                df.drop(dict_to_del[to_drop], inplace=True)
                df.reset_index(drop=True, inplace=True)
                df.to_csv('tables/SplitDASS17.csv')
                print('Table updated succesfully.')
                break
            elif df_num == 4:
                df.drop(dict_to_del[to_drop], inplace=True)
                df.reset_index(drop=True, inplace=True)
                df.to_csv('tables/SplitNDASS17.csv')
                print('Table updated succesfully.')
                break
            else:
                print('How did we get here')
                break
        elif to_drop.startswith('q'):
            break
        else:
            print('Error: Hand not found in table.')

def reset_table():
    while True:
        all_or_one = input('Would you like to reset all tables?(yes, no, or q to quit)\n')
        if all_or_one.lower().startswith('y'):
            db_df = pd.read_csv('OGData/DBLS17.csv')
            hard_df = pd.read_csv('OGData/HARDS17.csv')
            das_df = pd.read_csv('OGData/SplitDASS17.csv')
            ndas_df = pd.read_csv('OGData/SplitNDASS17.csv')
            db_df.to_csv('tables/DBLS17.csv', index=False)
            hard_df.to_csv('tables/HARDS17.csv', index=False)
            das_df.to_csv('tables/SplitDASS17.csv', index=False)
            ndas_df.to_csv('tables/SplitNDASS17.csv', index=False)
            print('All tables reset successfully.')
            break
        elif all_or_one.lower().startswith('n'):
            df, df_num = pick_table()
            if df_num == 1:
                db_df = pd.read_csv('OGData/DBLS17.csv')
                db_df.to_csv('tables/DBLS17.csv', index=False)
                print('Table updated successfully')
                break
            elif df_num == 2:
                hard_df = pd.read_csv('OGData/HARDS17.csv')
                hard_df.to_csv('tables/HARDS17.csv', index=False)
                print('Table updated successfully')
                break
            elif df_num == 3:
                das_df = pd.read_csv('OGData/SplitDASS17.csv')
                das_df.to_csv('tables/SplitDASS17.csv', index=False)
                print('Table updated successfully')
                break
            elif df_num == 4:
                ndas_df = pd.read_csv('OGData/SplitNDASS17.csv')
                ndas_df.to_csv('tables/SplitNDASS17.csv', index=False)
                print('Table updated successfully')
                break
        elif all_or_one.lower().startswith('q'):
            break
        else:
            print('Error: Please enter a valid command.')

def reset_stats():
    while True:
        all_or_one = input('Would you like to reset all tables?(yes, no, or q to quit)\n')
        if all_or_one.lower().startswith('y'):
            db_df = pd.read_csv('OGData/DBLS17.csv')
            hard_df = pd.read_csv('OGData/HARDS17.csv')
            das_df = pd.read_csv('OGData/SplitDASS17.csv')
            ndas_df = pd.read_csv('OGData/SplitNDASS17.csv')
            db_df.to_csv('Stats/DBLS17Stat.csv', index=False)
            hard_df.to_csv('Stats/HARDS17Stat.csv', index=False)
            das_df.to_csv('Stats/SplitDASS17Stat.csv', index=False)
            ndas_df.to_csv('Stats/SplitNDASS17Stat.csv', index=False)
            print('All tables reset successfully.')
            break
        elif all_or_one.lower().startswith('n'):
            df, df_num = pick_table()
            if df_num == 1:
                db_df = pd.read_csv('OGData/DBLS17.csv')
                db_df.to_csv('Stats/DBLS17Stat.csv', index=False)
                print('Table updated successfully')
                break
            elif df_num == 2:
                hard_df = pd.read_csv('OGData/HARDS17.csv')
                hard_df.to_csv('Stats/HARDS17Stat.csv', index=False)
                print('Table updated successfully')
                break
            elif df_num == 3:
                das_df = pd.read_csv('OGData/SplitDASS17.csv')
                das_df.to_csv('Stats/SplitDASS17Stat.csv', index=False)
                print('Table updated successfully')
                break
            elif df_num == 4:
                ndas_df = pd.read_csv('OGData/SplitNDASS17.csv')
                ndas_df.to_csv('Stats/SplitNDASS17Stat.csv', index=False)
                print('Table updated successfully')
                break
        elif all_or_one.lower().startswith('q'):
            break
        else:
            print('Error: Please enter a valid command.')

def stats(rand_int_col, rand_int_row, value, df_num, answer_bool):
    #stored as value/amount right/amount wrong
    if df_num == 1:
        
        df = pd.read_csv('Stats/DBLS17Stat.csv')
        stat = df.iloc[rand_int_row, rand_int_col]
        try:
            val, right, wrong = stat.split('/')
            right, wrong = int(right), int(wrong)
            if val != value:
                print('Values do not match')
                return None
        except:
            val, right, wrong = (0,0,0)
        
        if answer_bool == True:
            right += 1
        elif answer_bool == False:
            wrong += 1
        else:
            print('Error in stats answer_bool if')
            
        new_value = str(val) + '/' + str(right) + '/' + str(wrong)
        df.iloc[rand_int_row, rand_int_col] = new_value
        df.to_csv('Stats/DBLS17Stat.csv', index=False)
        
    elif df_num == 2:
        
        df = pd.read_csv('Stats/HARDS17Stat.csv')
        stat = df.iloc[rand_int_row, rand_int_col]
        try:
            val, right, wrong = stat.split('/')
            right, wrong = (int(right), int(wrong))
            if val != value:
                print('Values do not match')
                return None
        except:
            val, right, wrong = (value,0,0)
            
        if answer_bool == True:
            right += 1
        elif answer_bool == False:
            wrong += 1
        else:
            print('Error in stats answer_bool if')
            
        new_value = str(val) + '/' + str(right) + '/' + str(wrong)
        df.iloc[rand_int_row, rand_int_col] = new_value
        df.to_csv('Stats/HARDS17Stat.csv', index=False)
        
    elif df_num == 3:
        
        df = pd.read_csv('Stats/SplitDASS17Stat.csv')
        stat = df.iloc[rand_int_row, rand_int_col]
        
        try:
            val, right, wrong = stat.split('/')
            right, wrong = (int(right), int(wrong))
            if val != value:
                print('Values do not match')
                return None
        except:
            val, right, wrong = (value,0,0)
        
        if answer_bool == True:
            right += 1
        elif answer_bool == False:
            wrong += 1
        else:
            print('Error in stats answer_bool if')
            
        new_value = str(val) + '/' + str(right) + '/' + str(wrong)
        df.iloc[rand_int_row, rand_int_col] = new_value
        df.to_csv('Stats/SplitDASS17Stat.csv', index=False)
        
    elif df_num == 4:
        
        df = pd.read_csv('Stats/SplitNDASS17Stat.csv')
        stat = df.iloc[rand_int_row, rand_int_col]
        
        try:
            val, right, wrong = stat.split('/')
            right, wrong = (int(right), int(wrong))
            if val != value:
                print('Values do not match')
                return None
        except:
            val, right, wrong = (value,0,0)
        
        if answer_bool == True:
            right += 1
        elif answer_bool == False:
            wrong += 1
        else:
            print('Error in stats answer_bool if')
            
        new_value = str(val) + '/' + str(right) + '/' + str(wrong)
        df.iloc[rand_int_row, rand_int_col] = new_value
        df.to_csv('Stats/SplitNDASS17Stat.csv', index=False)
        

def show_stats():
    
    df, df_num = pick_table()
    
    if df_num == 1:
        df = pd.read_csv('Stats/DBLS17Stat.csv')
        print(df)
    elif df_num == 2:
        df = pd.read_csv('Stats/HARDS17Stat.csv')
        print(df)
    elif df_num == 3:
        df = pd.read_csv('Stats/SplitDASS17Stat.csv')
        print(df)
    elif df_num == 4:
        df = pd.read_csv('Stats/SplitNDASS17Stat.csv')
        print(df)

def alter_count_min_max():
    og_count_min = [str(x) for x in range(-10,1)]
    og_count_max = [str(x) for x in range(0, 11)]
    
    with open('count_min_max.txt', 'r+') as f:
        count_min_max = f.read()
        current_count_min, current_count_max = count_min_max.split(',')
        
    while True:
        print('Count minimum: ' + current_count_min)
        print('Count maximum: ' + str(int(current_count_max)-1))
        to_alter = input('Select an option:\n1: Edit count minimum\n2: Edit count maximum\n3: Reset count range\n4: Exit\n')
        if to_alter in ['1','2','3']:
            while True:
                if to_alter == '1':
                    
                    new_count_min = input('Please enter the minimum count you would like to use from -10 to 0.(q to quit)\n')
                    
                    if new_count_min in og_count_min:
                        
                        print('Minimum count has been change to ' + new_count_min)
                        current_count_min = new_count_min
                        break
                        
                    elif new_count_min == 'q':
                        break
                        
                    else:
                        print('Please enter a valid count minimum.')
                        
                elif to_alter == '2':
                    
                    new_count_max = input('Please enter the maximum count you would like to use from 0 to 10.(q to quit)\n')
                    
                    if new_count_max in og_count_max:
                        
                        print('Maximum count has been changed to ' + new_count_max)
                        current_count_max = str(int(new_count_max)+1)
                        break
                        
                    elif new_count_max == 'q':
                        break
                        
                    else:
                        
                        print('Please enter a valid count minimum.')
                        
                elif to_alter == '3':
                    
                    current_count_min = '-10'
                    current_count_max = '11'
                    print('Count reset successfully.')
                    break
        
        elif to_alter == '4':
            min_max_str = current_count_min + ',' + current_count_max
            with open('count_min_max.txt', 'w') as f:
                f.write(min_max_str)
            break
            
        else:
            print('Please enter a valid number.')
            
        

#if __name__ == "__main__":
print('Welcome to blackjack counting trainer!')
while True:
    
    what_do = input('Please select an option.\n1: Start Training\n2: View tables\n3: Alter tables\n4: Reset tables\n5: View your statistics\n6: Reset statistics\n7: Alter count minimum or maximum\n8: Quit\n')
    db_df = pd.read_csv('tables/DBLS17.csv')
    hard_df = pd.read_csv('tables/HARDS17.csv')
    das_df = pd.read_csv('tables/SplitDASS17.csv')
    ndas_df = pd.read_csv('tables/SplitNDASS17.csv')
    with open('count_min_max.txt', 'r') as f:
        count_min, count_max = f.read().split(',')
    
    if what_do == '1':
        
        df, df_num = pick_table()
        if isinstance(df, str):
            continue
        while True:
            dealer_card, player_hand, ran_val, count, rand_int_col, rand_int_row = get_vals(df, int(count_min), int(count_max))
            correct_answer, correct_answer_string = what_should_you_do(df_num, ran_val, count)
            guess = user_guess(dealer_card, player_hand, correct_answer, count, df_num)

            if guess == 'q':
                break
            elif guess == True:
                print('\n'*100)
                print('Correct!')
            else:
                print('\n'*100)
                print('Incorrect! The correct answer was to ' + correct_answer_string)
            
            stats(rand_int_col, rand_int_row, ran_val, df_num, guess)
    
    elif what_do == '2':
        df, df_num = pick_table()
        print(df)
    elif what_do == '3':
        alter_table()
    elif what_do == '4':
        reset_table()
    elif what_do == '5':
        show_stats()
    elif what_do == '6':
        reset_stats()
    elif what_do == '7':
        alter_count_min_max()
    elif what_do == '8':
        print('Thanks for playing!')
        break
    else:
        print('Please select a valid number.')