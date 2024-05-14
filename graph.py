import networkx as nx

G = nx.Graph()
G.add_nodes_from(['Cherkasy', 'Chernivtsi', 'Dnipro', 'IFrank', 'Kherson', 'Khmelnytskyi', 'Kropyvnytskyi',
'Kyiv', 'Lutsk', 'Lviv', 'Mykolaiv', 'Odessa', 'Rivne', 'Ternopil', 'Uzhhorod', 'Vinnytsia', 'Zaporizhzhia',
'Zhytomyr'])

G.add_weighted_edges_from([
    ("Kyiv", "Zhytomyr", 140),
    ("Kyiv", "Odessa", 475),
    ("Kyiv", "Cherkasy", 192),
    ("Kyiv", "Kropyvnytskyi", 320),
    ("Vinnytsia", "Khmelnytskyi", 136),
    ("Vinnytsia", "Kropyvnytskyi", 202),
    ("Vinnytsia", "Zhytomyr", 128),
    ("Vinnytsia", "Chernivtsi", 202),
    ("Vinnytsia", "Odessa", 318),
    ("Zhytomyr", "Rivne", 131),
    ("Zhytomyr", "Khmelnytskyi", 159),
    ("Rivne", "Lutsk", 70),
    ("Rivne", "Lviv", 211),
    ("Rivne", "Ternopil", 159),
    ("Rivne", "Khmelnytskyi", 194),
    ("Lutsk", "Lviv", 154),
    ("Lutsk", "Ternopil", 219),
    ("Lviv", "Ternopil", 130),
    ("Lviv", "Uzhhorod", 187),
    ("Lviv", "IFrank", 141),
    ("Uzhhorod", "IFrank", 120),
    ("IFrank", "Ternopil", 131),
    ("IFrank", "Chernivtsi", 261),
    ("Ternopil", "Chernivtsi", 179),
    ("Ternopil", "Khmelnytskyi", 68),
    ("Khmelnytskyi", "Chernivtsi", 215),
    ("Odessa", "Mykolaiv", 133),
    ("Odessa", "Kropyvnytskyi", 294),
    ("Mykolaiv", "Kherson", 66),
    ("Mykolaiv", "Kropyvnytskyi", 222),
    ("Mykolaiv", "Dnipro", 302),
    ("Kropyvnytskyi", "Dnipro", 252),
    ("Dnipro", "Zaporizhzhia", 85),
    ("Cherkasy", "Kropyvnytskyi", 222),
    ("Cherkasy", "Dnipro", 218)
])