import pickle

color = 'red'
pickle.dump(color, open('color.p', 'wb'))
fav_color = pickle.load(open('color.p', 'rb'))
print(fav_color)
