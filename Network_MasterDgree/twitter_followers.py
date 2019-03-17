from pylab import *
from networkx import *
import twitter

api = twitter.Api(consumer_key = 'fmtF0Ob78CoC1lYmyV0YGtHNe',
		consumer_secret = 'YlWiScJR6MMnKHVaWaA2QF3rm6YFne7fUIRfLGU9SXdvHzYNhV', 
		access_token_key = '890607426-40KLR3dJFGdtJ2YPAVjPR7FWKxpxJAs2tJ6AC9HI', 
		access_token_secret = 'EdyrrMLFotvfjNQtZtlqC1aYJmnkxRFQ3EfgoyH6jEy7V', 
		input_encoding = "UTF-8",
        sleep_on_rate_limit=True)

friends = api.GetFriends()

G = networkx.Graph()

for i in min(5, len(friends)): 
   G.add_edge("T_I_SHOW",friends[i].screen_name)
   for user in api.GetFriends(friends[i].id):
        if user in friends[:min(5, len(friends))]:
            G.add_edge(friend.screen_name,user.screen_name)

pos = spring_layout(G)

draw_networkx_nodes(G, pos, node_size = 100, node_color = 'b')
draw_networkx_edges(G, pos, width = 1)
draw_networkx_labels(G, pos, font_size = 12, font_family = 'sans-serif', font_color = 'r')

xticks([])
yticks([])
savefig("egonetwork.png") 
show()