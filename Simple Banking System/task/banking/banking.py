# Write your code here
import random
from random import sample
import sys
import sqlite3


def create_database():
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS card(
                id INTEGER,
                number text,
                pin text,
                balance INTEGER DEFAULT 0
            )""")
    conn.commit()
    conn.close()


my_card_list = []

card_pin_matrix = []

user_balance_list = []

user_counter = 0

card_number = []

card_pin = []

j = 0

doubled_number_list = []

sum_total = 0

calculated_checksum = 0


def generate_numbers() -> tuple:
    while True:
        random_card = '400000' + ''.join([str(n) for n in sample(range(8), 8)]) + '7'
        random_card2 = ''.join([str(n) for n in sample(range(8), 8)]) + '7'
        random_PIN = ''.join([str(n) for n in sample(range(9), 4)])
        return (random_card)


# test_number = generate_numbers()
#
# test_variable = test_number
#
# test_number = list(test_number)

def generate_validated_card_number():
    sum_total = 0
    global test_variable

    test_number = generate_numbers()

    test_variable = test_number

    test_number = list(test_number)

    variable = ''
    for i in range(len(test_number)):
        test_number[i] = int(test_number[i])

    doubled_number_list = test_number

    for i in range(len(doubled_number_list)):  # Multiply odd digits by 2 - pero no me convence
        if i % 2 == 0:
            doubled_number_list[i] = doubled_number_list[i] * 2
        sum_total = sum_total + test_number[i]

    sum_total = 0

    for i in range(len(doubled_number_list)):  # Substract 9 to numbers over 9
        if doubled_number_list[i] > 9:
            doubled_number_list[i] -= 9
        sum_total = sum_total + test_number[i]

    # Calculate checksum number which must be a multiple of 10, and then add it to test number to get the credit card num

    if (sum_total + 1) % 10 == 0:
        calculated_checksum = (sum_total + 1) - sum_total
    elif (sum_total + 2) % 10 == 0:
        calculated_checksum = (sum_total + 2) - sum_total
    elif (sum_total + 3) % 10 == 0:
        calculated_checksum = (sum_total + 3) - sum_total
    elif (sum_total + 4) % 10 == 0:
        calculated_checksum = (sum_total + 4) - sum_total
    elif (sum_total + 5) % 10 == 0:
        calculated_checksum = (sum_total + 5) - sum_total
    elif (sum_total + 6) % 10 == 0:
        calculated_checksum = (sum_total + 6) - sum_total
    elif (sum_total + 7) % 10 == 0:
        calculated_checksum = (sum_total + 7) - sum_total
    elif (sum_total + 8) % 10 == 0:
        calculated_checksum = (sum_total + 8) - sum_total
    elif (sum_total + 9) % 10 == 0:
        calculated_checksum = (sum_total + 9) - sum_total
    elif (sum_total + 0) % 10 == 0:
        calculated_checksum = (sum_total + 0) - sum_total

    test_variable = str(test_variable)

    test_variable = test_variable + str(calculated_checksum)

    test_variable = int(test_variable)

    variable = test_variable

    test_variable = ''

    # print("Card number without checksum = ", variable)

    return variable


def print_instructions():
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")


def print_logged_in_menu():
    print("1. Balance")
    print("2. Add income")
    print("3. Do transfer")
    print("4. Close account")
    print("5. Log out")
    print("0. Exit")


create_database()

while True:
    print_instructions()
    user_input = int(input())

    if user_input == 1:
        print("\nYour card has been created")
        print("Your card number:")
        # print card number
        card_number.append(generate_validated_card_number())
        card_number.append(format(random.randint(0000, 9999), '04d'))
        if card_number not in my_card_list:
            card_pin_matrix.append(card_number)
            print(card_pin_matrix[user_counter][j])
        elif card_number in my_card_list:
            card_number = random.randint(4000000000000001, 4000009999999999)
            card_pin_matrix.append(card_number)
            card_pin_matrix[user_counter].append(card_pin)
        print("Your card PIN:")
        print(card_pin_matrix[user_counter][j + 1])

        card_number2 = card_number

        card_number = []
        user_counter += 1

        conn = sqlite3.connect('card.s3db')

        cur = conn.cursor()

        cur.execute("insert into card (id, number, pin) values(?,?,?)", (user_counter, card_number2[j],
                                                                         card_number2[j + 1]))

        conn.commit()

        conn.close()

    elif user_input == 2:
        print("\nEnter your card number:")
        card_number_input = str(input())
        print("\nEnter your PIN:")
        pin_number_input = str(input())

        conn = sqlite3.connect('card.s3db')

        cur = conn.cursor()

        cur.execute("SELECT number, pin FROM card WHERE number=? AND pin=?", (card_number_input, pin_number_input))

        rows = cur.fetchall()

        card_pin_matrix = rows

        if len(card_pin_matrix) > 0:

            for i in range(len(card_pin_matrix)):
                if card_number_input == card_pin_matrix[i][j] and pin_number_input == card_pin_matrix[i][j + 1]:
                    print("\nYou have successfully logged in!\n")

                    while True:

                        print_logged_in_menu()

                        second_input = int(input())

                        if second_input == 1:

                            # Code that selects balance from database balance field according to card number and returns it

                            conn = sqlite3.connect('card.s3db')

                            cur = conn.cursor()

                            cur.execute("SELECT balance FROM card WHERE number=?", (card_number_input,))

                            rows = cur.fetchall()

                            conn.close()

                            for row in rows:
                                print("Balance:", row[0])

                        if second_input == 2:
                            print("\nEnter income: \n")

                            add_income = int(input())

                            conn = sqlite3.connect('card.s3db')

                            cur = conn.cursor()

                            cur.execute("UPDATE card SET balance=balance+? WHERE number=?",
                                        (add_income, card_number_input))

                            conn.commit()

                            conn.close()

                            print("\nIncome was added!\n")

                        if second_input == 3:
                            print("\nTransfer\n")

                            print("\nEnter card number:\n")

                            transfer_card_number_input = str(input())

                            conn = sqlite3.connect('card.s3db')

                            cur = conn.cursor()

                            cur.execute("SELECT number FROM card WHERE number=?", (transfer_card_number_input,))

                            validate_card_number = cur.fetchall()

                            conn.close()

                            if len(validate_card_number) <= 0:
                                print("\nSuch a card does not exist.\n")
                                print("\nProbably you made mistake in card number. Please try again!\n")

                            if len(validate_card_number) > 0:

                                print("\nEnter how much money you want to transfer:\n")

                                transfer_income = int(input())

                                # Code that updates database balance field from user 1 (substracts)
                                # And updates database balance field from user 2 (adds)

                                conn = sqlite3.connect('card.s3db')

                                cur = conn.cursor()

                                cur.execute("SELECT balance FROM card WHERE number=?", (card_number_input,))

                                balance_check = cur.fetchall()

                                if balance_check[0][0] > 0:
                                    cur.execute("UPDATE card SET balance=balance-? WHERE number=?", (transfer_income,
                                                                                                     card_number_input))

                                    cur.execute("UPDATE card SET balance=balance+? WHERE number=?", (transfer_income,
                                                                                                     transfer_card_number_input))

                                    conn.commit()

                                    conn.close()

                                    print("\nSuccess!\n")

                                elif balance_check[0][0] <= 0:
                                    conn.close()
                                    print("Not enough money!")

                        if second_input == 4:

                            # Code that deletes row from database where account number = card number

                            conn = sqlite3.connect('card.s3db')

                            cur = conn.cursor()

                            cur.execute("SELECT number FROM card WHERE number=?", (card_number_input,))

                            deleted_card_number = cur.fetchall()

                            if deleted_card_number[0][0] is not None:

                                cur.execute("DELETE FROM card WHERE number=?", (card_number_input,))
                                conn.commit()
                                conn.close()

                                print("\nThe account has been closed!\n")

                            elif deleted_card_number[0][0] is None:
                                conn.close()
                                print("\nThis account does not exist!\n")

                            break

                        if second_input == 5:
                            print("\nYou have successfully logged out!\n")
                            break

                        if second_input == 0:
                            print("\nBye!")
                            sys.exit()

        elif len(card_pin_matrix) <= 0:
            conn.close()
            print("\nWrong card number or PIN!\n")

    elif user_input == 0:
        print("\nBye!")
        sys.exit()
