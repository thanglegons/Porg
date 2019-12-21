# Project Porg

A **porg** is a tiny creature that appears in Star Wars movie.

![enter image description here](https://jedibusiness.com/images/actionFigures/Disney-Elite-Series-Die-Cast/Porg-2_Big_6.jpg)
# Description

This project contains: **Search engine** and **Recommender System** used for Book rental website ([FRONT-END](https://github.com/truongdo619/UET_BookRentalLibrary) , [BACK-END](https://github.com/dhphong/UET_BookRentalLibrary_Backend)) 

- **Porg** uses  **Elastic Search** and **Flask** for **Search Engine**
- For **Recommender System** Porg utilizes information about categories (genres) of each book for creating feature vector for them. Then **locality sensitive hashing** is adopted with **random projections** to generate hash value for books. Porg will suggest top related books for a particular one.

# Demo

Demo for full website: [http://3.1.80.54/](http://3.1.80.54/)
**Porg** is deployed at [http://3.1.80.54:1910/](http://3.1.80.54:1910/) 

Usage of **Porg**:
- **Search Engine**: [http://3.1.80.54:1910/search](http://3.1.80.54:1910/search)
params: (**q**: textual query,  **search_filter**: 2 option for *title* or *author_searchable*, **category**: id of category, **page**: page number)
- **Recommender System**: 
params: (**id**: id for book (we use isbn13 for book id here), **top**: top related books)

Example for:
- **Search Engine**: [http://3.1.80.54:1910/search?q=Thomas&search_filter=author_searchable](http://3.1.80.54:1910/search?q=Thomas&search_filter=author_searchable)
- **Recommender System**: [http://3.1.80.54:1910/recommend?id=9780297859383&top=10](http://3.1.80.54:1910/recommend?id=9780297859383&top=10)
