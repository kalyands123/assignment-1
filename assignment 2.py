#!/usr/bin/env python
# coding: utf-8

# In[10]:


pip install requests beautifulsoup4
# Leonardo DiCaprio


# In[18]:


pip install IMDbPY


# In[20]:


from imdb import IMDb

def get_filmography(actor_name):
    ia = IMDb()
    
    people = ia.search_person(actor_name)

    if not people:
        print("Actor not found!")
        return
    
    actor = people[0]
    
    ia.update(actor)
    filmography = actor.get('filmography', [])
    
    films = []
    for movie in filmography.get('actor', []):
        title = movie.get('title')
        year = movie.get('year')
        films.append((title, year))

    films.sort(key=lambda x: (x[1] is None, x[1]), reverse=True)

    print(f"Films done by {actor_name} in descending order:")
    for title, year in films:
        year_display = year if year is not None else "N/A"
        print(f"{title} ({year_display})")

actor_name = input("Enter actor's name: ")
get_filmography(actor_name)


# In[ ]:




