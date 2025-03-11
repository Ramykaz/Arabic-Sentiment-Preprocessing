import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def build_retweet_network(df):
    G = nx.DiGraph()
    for _, row in df.iterrows():
        user = row['user']
        retweeted_user = row['retweeted_user']
        if pd.notnull(retweeted_user):
            G.add_edge(user, retweeted_user)
    return G

if __name__ == "__main__":
    df = pd.read_csv("../data/raw_data.csv")
    G = build_retweet_network(df)
    
    # Draw the network
    plt.figure(figsize=(12, 8))
    nx.draw(G, node_size=50, edge_color='gray', alpha=0.6)
    plt.title("Retweet Network Graph")
    plt.show()
    
    print("Network analysis complete.")
