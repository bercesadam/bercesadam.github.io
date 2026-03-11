from pyvis.network import Network
import pandas as pd
import numpy as np

# Load data from CSV
n = pd.read_csv('nodes.csv', delimiter='|')
e = pd.read_csv('edges.csv', delimiter='|')

# Create a Pyvis Network instance
net = Network(height="100%", width="100%", notebook=False, neighborhood_highlight=True)
net.barnes_hut(gravity=-950,central_gravity=0.5,spring_length=150,spring_strength=0.001,damping=0.09,overlap=0.8)

# Add nodes and edges from the DataFrame
for _, row in n.iterrows():
    net.add_node(row['node_id'], label=row['label'], title=row['html_content']+'<br><img src="'+row['image']+'.jpg"><br><audio src="'+row['image']+'.mp3" controls>', 
                    shape='box', color=row['color'])
    
for _, row in e.iterrows():
    width = 1
    ls = "solid" 
    if row['relation'] == "der":
        width = 6
    if row['relation'] == "close":
        width = 3
        
    if row['relation'] == "rel":
        net.add_edge(row['source'], row['target'],
                    dashes="dot")
    elif row['relation'] == "der" or row['relation'] == "close":
        net.add_edge(row['source'], row['target'],
                        width=width)
    else:
        net.add_edge(row['source'], row['target'], label=row['relation'],
                        width=width)

# Export to HTML
net.toggle_stabilization(True)
net.show('tree_visualization.html', notebook=False)
