# I was given this code and asked to catch the exception given when the program searches for the likes on a post that has none.
# I added an exception handler for KeyError that simply passed in that case, meaning it could move on with no errors and continue to find the total.
facebook_posts = [{'Likes': 21, 'Comments': 2},
                  {'Likes': 13, 'Comments': 2, 'Shares': 1},
                  {'Likes': 33, 'Comments': 8, 'Shares': 3},
                  {'Comments': 4, 'Shares': 2},
                  {'Comments': 1, 'Shares': 1},
                  {'Likes': 19, 'Comments': 3}]
total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass

print(total_likes)