
# Given a JSON payload of books with the following structure:
# [  
#     {
#         "name": <string>,
#         "author": <string>,
#         "num_pages": <int>,
#         "is_used": <boolean>,
#         "price": <string> (ex. "10.98")
#     },
#     ...
# ]

# Write and test a function to return the average number of pages of used books that cost greater than $15.
 # used books 
 # cost greater than $15.
 # Calculate the average num_pages

# Example: 
data = [
    {
        "name": "The Republic",
        "author": "Plato",
        "num_pages": 138,
        "is_used": True,
        "price": "13.99"
    },
    {
        "name": "The Fire Next Time",
        "author": "James Baldwin",
        "num_pages": 184,
        "is_used": True,
        "price": "19.39"
    },
    {
        "name": "The Art of War",
        "author": "Sun Tzu",
        "num_pages": 67,
        "is_used": False,
        "price": "30.49"
    },
    {
        "name": "Ceremony",
        "author": "Leslie Marmon Silko",
        "num_pages": 291,
        "is_used": True,
        "price": "28.17"
    }
]

def calculateAverageNumPages(data):

    if not data:
        return 0

    books = []
    for json in data:

        if json['is_used'] and float(json['price']) > 15:
            books.append(json['num_pages'])
    
    return sum(books) / len(books) if len(books) != 0 else 0


print(calculateAverageNumPages(data))

assert calculateAverageNumPages(data) == 237.5