import most_retweets, top_users, top_days

if __name__ == "__main__":
	# Example: 1, 2 or 3 are valid inputs
    display = """
        ¿What information do you want to know?
        1. TOP 10 tweets with the most retweets
        2. TOP 10 users with most tweets
        3. TOP 10 days with the most tweets
        4. TOP 10 hashtags most used 
    """

    print(display)
    response = input("Enter your choice: ")

    try:
        if response == "1":
            result = most_retweets.top_retweets()
        elif response == "2":
            result = top_users.top_users_by_tweets()
        elif response == "3":
            result = top_days.top_days_by_tweets()
        elif response == "4":
            print("Top 10 hashtags most used")
    except ValueError:
        print("Invalid input or result")
    finally:
        print(result)
        exit()