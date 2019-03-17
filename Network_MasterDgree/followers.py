#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pylab import *
from networkx import *
import twitter

#コンシューマーキーやアクセストークンの情報を入力
api = twitter.Api(consumer_key = 'fmtF0Ob78CoC1lYmyV0YGtHNe',
		consumer_secret = 'YlWiScJR6MMnKHVaWaA2QF3rm6YFne7fUIRfLGU9SXdvHzYNhV', 
		access_token_key = '890607426-40KLR3dJFGdtJ2YPAVjPR7FWKxpxJAs2tJ6AC9HI', 
		access_token_secret = 'EdyrrMLFotvfjNQtZtlqC1aYJmnkxRFQ3EfgoyH6jEy7V', 
		input_encoding = "UTF-8",
        sleep_on_rate_limit=True)

#twitterからフォローしてる人のリストを取得
friends = api.GetFriends()

G = networkx.Graph()

#自分と自分がフォローしている人の間にエッジを張る
for friend in friends:
    G.add_edge('T_I_SHOW' ,friend.screen_name)

#自分がフォローしてる人と、その人がフォローしてる人との間にエッジを張る
for friend in friends:
    for user in api.GetFriends(friend.id):
    	if user in friends:
            G.add_edge(friend.screen_name,user.screen_name)

#バネ指向モデルというアルゴリズムで各ノードを見易いように配置
pos = spring_layout(G)

#ノードやエッジの見た目調整
draw_networkx_nodes(G, pos, node_size = 100, node_color = 'b')
draw_networkx_edges(G, pos, width = 1)
draw_networkx_labels(G, pos, font_size = 12, font_family = 'sans-serif', font_color = 'r')

xticks([])
yticks([])
savefig("egonetwork.png") 
show()