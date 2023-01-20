def main():

    # The list below will be used for all of the exercises below:
    names = ["Abigail", "Brenda", "Chad", "Doug", "Emma", "Francis", "George", "Harold", "Imogen”",
    "Jackie", "Kurt", "Linda"]
    print(names[0:3])
    print(names[5:12])
    print(names[5:])
    print(names[11])
    print(names[-1])








    # 3. [‘Francis’, ‘George’, ‘Harold’, ‘Imogen’, ‘Jackie’, ‘Kurt’, ‘Linda’] (using two numbers in the slice)


    # 4. [‘Francis’, ‘George’, ‘Harold’, ‘Imogen’, ‘Jackie’, ‘Kurt’, ‘Linda’] (using one number in the slice)



    # 5. [‘Linda’] (using a positive number)


    # 6. [‘Linda’] (using a negative number)



    # 7. [‘Brenda’, ‘Doug’, ‘Francis’, ‘Harold’]
    print(names[1:8:2])


    # 8. [‘Abigail’, ‘Chad’, ‘Emma’, ‘George’, ‘Imogen’, ‘Kurt’]
    print(names[0:11:2])



    # 9. [‘Abigail’, ‘Chad’, ‘Emma’, ‘George’, ‘Imogen’, ‘Kurt’] (using a different way than above.
    # HINT: If you leave a slice number blank, the default is either the beginning or the end of the list,
    # depending on which side of the colon is blank.
    print(names[0::2])


    # 10. [‘Linda’, ‘Kurt’, ‘Jackie’]
    print(names[9:12:-1])

    # 11. ['Linda', 'Kurt', 'Jackie', 'Imogen', 'Harold', 'George', 'Francis', 'Emma', 'Doug', 'Chad', 'Brenda', 'Abigail']



    # 12. ['Linda', 'Kurt', 'Jackie', 'Imogen', 'Harold', 'George', 'Francis', 'Emma', 'Doug', 'Chad', 'Brenda', 'Abigail']
    # (in a different way than 11. See hint for 9 for help.)





if __name__ == '__main__':
    main()